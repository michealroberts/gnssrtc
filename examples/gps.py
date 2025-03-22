# **************************************************************************************

# @package        gnssrtc
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import time

from serial import Serial

from gnssrtc.gps import GPSUARTDeviceInterface

# **************************************************************************************

ser = Serial("/dev/ttyAMA10", 9600, timeout=1)

# **************************************************************************************

ser.reset_input_buffer()

# **************************************************************************************

# cmd1 enable GPS+BD+Galileo+QZSS:
cmd1 = b"\x06\x3e\x3c\x00\x00\x20\x20\x07\x00\x08\x10\x00\x01\x00\x01\x01\x01\x01\x03\x00\x00\x00\x01\x01\x02\x04\x08\x00\x00\x00\x01\x01\x03\x08\x10\x00\x01\x00\x01\x01\x04\x00\x08\x00\x00\x00\x01\x03\x05\x00\x03\x00\x01\x00\x01\x05\x06\x08\x0e\x00\x00\x00\x01\x01"

# cmd2 enable NMEA version 4.10 to ouput BD sentences:
cmd2 = b"\xb5\x62\x06\x17\x14\x00\x00\x41\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00"

# Please refer the file of u-blox 8 /u-blox M8 Receiver description Including protocol specification in www.u-blox.com for more info

# two 8bit crc var
ck_a = 0
ck_b = 0


# func of calculating the cmd1 CRC value
def calcu_crc(cmdx):
    global ck_a
    global ck_b
    ck_a = 0
    ck_b = 0
    for i in cmdx:
        # print(i,' ',end='')
        ck_a = ck_a + i
        ck_b = ck_b + ck_a


# calculate the the cmd1
calcu_crc(cmd1)

# combine the cmd1 bytes,like that header + conten + crc
cmd1 = b"\xb5\x62" + cmd1 + bytes([ck_a & 0xFF, ck_b & 0xFF])

# calculate the the cmd2
calcu_crc(cmd2)

# combine the cmd2 bytes,like that header + conten + crc
cmd2 = b"\xb5\x62" + cmd2 + bytes([ck_a & 0xFF, ck_b & 0xFF])

ser.write(cmd1)

ser.write(cmd2)

# **************************************************************************************

gps = GPSUARTDeviceInterface(port="/dev/ttyAMA10", baudrate=9600, timeout=1)

# **************************************************************************************

if __name__ == "__main__":
    gps.connect()

    version = gps.get_firmware_version()

    print(f"Firmware version: {version}")

    while True:
        data = ser.read_all()
        if data:
            print("Received:", data)
        else:
            print("No data received...")
        time.sleep(1)

    try:
        while gps.is_ready():
            data = gps.get_nmea_data()

            if data:
                print(data)

            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        gps.disconnect()

# **************************************************************************************
