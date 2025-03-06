# **************************************************************************************

# @package        gnssrtc
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from gnssrtc.nmea import parse_gpcgg_nmea_coordinate

# **************************************************************************************


class TestParseGPCGGNMEACoordinate(unittest.TestCase):
    def test_north_coordinate(self):
        # NMEA coordinate "4916.45" with 'N' should compute to 49 + (16.45/60)
        value = "4916.45"
        direction = "N"
        expected = 49 + (16.45 / 60.0)
        result = parse_gpcgg_nmea_coordinate(value, direction)
        self.assertAlmostEqual(result, expected, places=6)

    def test_south_coordinate(self):
        # With 'S', the computed value should be negative.
        value = "4916.45"
        direction = "S"
        expected = -(49 + (16.45 / 60.0))
        result = parse_gpcgg_nmea_coordinate(value, direction)
        self.assertAlmostEqual(result, expected, places=6)

    def test_east_coordinate(self):
        # For an east coordinate, e.g. "12311.12", the calculation is 123 + (11.12/60)
        value = "12311.12"
        direction = "E"
        expected = 123 + (11.12 / 60.0)
        result = parse_gpcgg_nmea_coordinate(value, direction)
        self.assertAlmostEqual(result, expected, places=6)

    def test_west_coordinate(self):
        # For a west coordinate, the result should be negative.
        value = "12311.12"
        direction = "W"
        expected = -(123 + (11.12 / 60.0))
        result = parse_gpcgg_nmea_coordinate(value, direction)
        self.assertAlmostEqual(result, expected, places=6)

    def test_zero_coordinate(self):
        # Testing the edge-case where the coordinate value is "0"
        value = "0"
        direction = "N"
        expected = 0.0
        result = parse_gpcgg_nmea_coordinate(value, direction)
        self.assertEqual(result, expected)


# **************************************************************************************

if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
