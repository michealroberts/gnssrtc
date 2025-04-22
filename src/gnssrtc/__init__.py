# **************************************************************************************

# @package        gnssrtc
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from .epoch import (
    EPOCH_NTP_1900,
    EPOCH_UNIX_1970,
    NTP_UNIX_DELTA,
)
from .gps import (
    BaseDeviceState,
    GPSUARTDeviceInterface,
)
from .nmea import GPCGGNMEASentence
from .zda import GPZDANMEASentence

# **************************************************************************************

__version__ = "0.3.0"

# **************************************************************************************

__license__ = "MIT"

# **************************************************************************************

__all__: list[str] = [
    "EPOCH_NTP_1900",
    "EPOCH_UNIX_1970",
    "NTP_UNIX_DELTA",
    "BaseDeviceState",
    "GPCGGNMEASentence",
    "GPSUARTDeviceInterface",
    "GPZDANMEASentence",
]

# **************************************************************************************
