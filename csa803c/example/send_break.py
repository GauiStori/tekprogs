#!/usr/bin/python3

import serial, struct

serial_dev = "/dev/ttyUSB0"
s = serial.Serial(serial_dev,
    baudrate=19200,         # baudrate
    bytesize=serial.EIGHTBITS,  # number of databits
    parity=serial.PARITY_EVEN,  # enable parity checking
    stopbits=serial.STOPBITS_ONE,   # number of stopbits
    timeout=None,         # set a timeout value, None for waiting forever
    xonxoff=0,          # enable software flow control
    rtscts=1            # enable RTS/CTS flow control
    )

s.send_break(1)
s.readline() #Flush buffer
