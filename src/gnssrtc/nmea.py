# **************************************************************************************

# @package        gnssrtc
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from datetime import datetime
from typing import Literal, Optional, TypedDict

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
