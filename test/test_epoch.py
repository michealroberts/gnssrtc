# **************************************************************************************

# @package        gnssrtc
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest
from datetime import datetime, timedelta, timezone

from gnssrtc import EPOCH_NTP_1900

# **************************************************************************************

now = datetime.now(tz=timezone.utc)

# **************************************************************************************


class TestEpochNTP1900(unittest.TestCase):
    def test_epoch_ntp_1900(self):
        self.assertEqual(EPOCH_NTP_1900.year, 1900)
        self.assertEqual(EPOCH_NTP_1900.month, 1)
        self.assertEqual(EPOCH_NTP_1900.day, 1)
        self.assertEqual(EPOCH_NTP_1900.hour, 0)
        self.assertEqual(EPOCH_NTP_1900.minute, 0)
        self.assertEqual(EPOCH_NTP_1900.second, 0)
        self.assertEqual(EPOCH_NTP_1900.tzinfo.utcoffset(None), timedelta(0))
        self.assertEqual(EPOCH_NTP_1900.tzinfo.tzname(None), "UTC")
        self.assertEqual(EPOCH_NTP_1900.timestamp(), -2208988800.0)
        self.assertEqual(
            EPOCH_NTP_1900.strftime("%Y-%m-%d %H:%M:%S"), "1900-01-01 00:00:00"
        )
        self.assertEqual(EPOCH_NTP_1900.isoformat(), "1900-01-01T00:00:00+00:00")


# **************************************************************************************
