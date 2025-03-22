# **************************************************************************************

# @package        gnssrtc
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import time

from gnssrtc.gps import GPSUARTDeviceInterface

# **************************************************************************************

gps = GPSUARTDeviceInterface(port="/dev/serial0", baudrate=9600)

# **************************************************************************************

if __name__ == "__main__":
    gps.connect()

    try:
        while gps.is_ready():
            print("GPS module over serial 0 UART is ready")

            data = gps.get_nmea_data()

            if data:
                print(data)

            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        gps.disconnect()

# **************************************************************************************
