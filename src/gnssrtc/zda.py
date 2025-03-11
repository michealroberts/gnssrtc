# **************************************************************************************

# @package        gnssrtc
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from datetime import datetime
from re import compile
from typing import TypedDict

# **************************************************************************************


class GPZDANMEASentence(TypedDict):
    # Message ID $GPZDA or $GNZDA:
    id: str

    # UTC datetime extracted from the ZDA message:
    utc: datetime

    # Local time zone offset in hours:
    local_zone_offset_hours: int

    # Local time zone offset in minutes:
    local_zone_offset_minutes: int

    # The checksum of the message (starts with "*"):
    checksum: str


# **************************************************************************************

GPZDA_NMEA_MESSAGE_REGEX = compile(
    r"^\$(GPZDA|GNZDA),"
    r"(\d{6}\.\d{1,2}),"
    r"(\d{2}),"
    r"(\d{2}),"
    r"(\d{4}),"
    r"([-+]?\d{1,2}),"
    r"(\d{2})"
    r"\*([0-9A-Fa-f]{2})$"
)

# **************************************************************************************
