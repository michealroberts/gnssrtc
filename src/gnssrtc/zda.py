# **************************************************************************************

# @package        gnssrtc
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from datetime import datetime
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
