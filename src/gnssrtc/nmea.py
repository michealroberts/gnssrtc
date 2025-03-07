# **************************************************************************************

# @package        gnssrtc
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from datetime import datetime, timezone
from re import MULTILINE, compile
from typing import List, Literal, Optional, TypedDict, cast

# **************************************************************************************


class GPCGGNMEASentence(TypedDict):
    # Message ID $GPGGA:
    id: str

    # UTC datetime of position fix:
    utc: datetime

    # Latitude (in decimal degrees):
    latitude: float

    # Longitude (in decimal degrees):
    longitude: float

    # Orthometric height using MSL reference (in meters):
    altitude: float

    # GPS quality indicator, e.g.,:
    # 0: Fix not valid
    # 1: GPS fix
    # 2: Differential GPS fix (DGNSS), SBAS, OmniSTAR VBS, Beacon, RTX in GVBS mode
    # 3: Not applicable
    # 4: RTK Fixed, xFill
    # 5: RTK Float, OmniSTAR XP/HP, Location RTK, RTX
    # 6: INS Dead reckoning
    # 7: Manual input mode (fixed position)
    # 8: Simulator mode
    # 9: WAAS (SBAS)
    quality_indicator: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Number of SVs in use, range from 00 through to 24+:
    number_of_satellites: int

    # Horizontal dilution of precision:
    hdop: float

    # Geoid separation (in meters):
    geoid_separation: float

    # Age of differential GPS data record, Type 1 or Type 9:
    dgps_age: Optional[float]

    # The reference station ID, range 0000 to 4095:
    reference_station_id: Optional[str]

    # The checksum of the message (starts with "*"):
    checksum: str


# **************************************************************************************

GPCGG_NMEA_MESSAGE_REGEX = compile(
    r"^\$([A-Z]{5}),([^*]+)\*([0-9A-Fa-f]{2})$", MULTILINE
)

# **************************************************************************************


def parse_gpcgg_nmea_coordinate(
    value: str, direction: Literal["N", "S", "E", "W"]
) -> float:
    degrees = int(float(value) // 100)
    minutes = float(value) - (degrees * 100)

    ddegrees = degrees + (minutes / 60.0)

    if direction in ("S", "W"):
        ddegrees = -ddegrees

    return ddegrees


# **************************************************************************************


def parse_gpcgg_nmea_sentence(value: str) -> "GPCGGNMEASentence":
    # Ensure that our string value starts with a $ sign:
    if not value.startswith("$"):
        raise ValueError("Invalid NMEA sentence: must start with '$'")

    # Use the regex to match and extract the message parts
    match = GPCGG_NMEA_MESSAGE_REGEX.match(value)

    # If we can not verify a match, then the NMEA sentence by definition is invalid:
    if not match:
        raise ValueError("Invalid NMEA sentence: regex did not match")

    # Extract the message header ID from the matched groups:
    id = match.group(1)

    # Extract the checksum from the matched groups:
    checksum = "*" + match.group(3)

    # Extract all of the data parts from final matched group:
    parts: List[str] = match.group(2).split(",")

    # Ensure that the number of parts matches with the expected number of parts of a
    # typical NMEA value. For a typical GPGGA sentence, we expect at least 15 fields
    # (the last one contains the checksum):
    if len(parts) < 14:
        raise ValueError("Invalid NMEA sentence: incorrect number of fields")

    # UTC datetime of position fix; using a default date of 1900-01-01:
    time = datetime.strptime(parts[0], "%H%M%S.%f")

    now = datetime.now(timezone.utc)

    utc = datetime(
        now.year,
        now.month,
        now.day,
        time.hour,
        time.minute,
        time.second,
        time.microsecond,
        timezone.utc,
    )

    # Ensure that we have a valid latitude direction part:
    if parts[2] not in ["N", "S"]:
        raise ValueError("Invalid NMEA latitude direction part")

    latitude = parse_gpcgg_nmea_coordinate(parts[1], cast(Literal["N", "S"], parts[2]))

    # Ensure that we have a valid longitude direction part:
    if parts[4] not in ["E", "W"]:
        raise ValueError("Invalid NMEA longitude direction part")

    longitude = parse_gpcgg_nmea_coordinate(parts[3], cast(Literal["E", "W"], parts[4]))

    # Cast our quality indicator to the Literal int between 0 .. 9:
    quality_indicator = cast(Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], int(parts[5]))

    # Ensure that it is one of the prescribed values:
    if quality_indicator not in {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:
        raise ValueError("Quality indicator must be between 0 and 9")

    # Differential GPS Age (parts[12]); if empty, set to None:
    dgps_age = float(parts[12]) if parts[12] != "" else None

    # Reference Station ID (parts[13]); if empty, set to None:
    reference_station_id = parts[13] if parts[13] != "" else None

    return GPCGGNMEASentence(
        id=f"${id}",
        utc=utc,
        latitude=latitude,
        longitude=longitude,
        altitude=float(parts[8]),
        quality_indicator=quality_indicator,
        number_of_satellites=int(parts[6]),
        hdop=float(parts[7]),
        geoid_separation=float(parts[10]),
        dgps_age=dgps_age,
        reference_station_id=reference_station_id,
        checksum=checksum,
    )


# **************************************************************************************
