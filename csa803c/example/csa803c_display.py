#!/usr/bin/python3

import serial

def displayTrace(instr):
    print("Example 1: Displaying a Trace\n")
    print("Ensure that the cable is connected and the scope's parameters are")
    print("set accordingly : (major menu UTILITY, minor menu RS232 Parameters)")
    print(" Baud 9600, Echo OFF, Stop Bits 1, Parity NONE, Flagging HARD")
    print(" Delay 0, EOL String CR/LF, Verbose OFF")
    #input(" Press Enter when ready")
    #a=''
    #while  a != "COM1" and a != "COM2":
    #    a = input("Press Enter for using COM1 (default), else type COM2")
    #    if a == "":
    #        a = "COM1"
    #print("We are opening %s at 9600 baud, no parity, and 1 stop bit."%a)
    input("Press Enter to ask for the scope's ID")
    instr.write(b"ID?\r\n")
    response = instr.readline()
    print(response)
    a=input("Press Enter after connecting the CALIBRATOR to channel 1 (head 1)")
    a=input("Press Enter to initialize scope.")
    instr.write(b"INIT\r\n")
    a=''
    while a != 'y' and a != 'Y' and a != 'n' and a != 'N':
        a=input("Do you want to watch the commands in DEBUG mode ? (y/n)")
        if a == 'y' or a == 'Y':
            instr.write(b"DEBUG RS232:ON\r\n")
        else:
            instr.write(b"DEBUG RS232:OFF\r\n")
    input("Press Enter to setup trace1 from sampling head 1, channel 1.")
    instr.write(b"TRACE1 DESCRIPTION:'M1'\r\n")
    input("Press Enter to set the trigger to INTERNAL.")
    instr.write(b"TRIGGER SOURCE:INTERNAL\r\n")
    input("Press Enter to manually set the size and position of the trace.")
    instr.write(b"TBMAIN TIME:10E-9;MAINPOS 55E-9;CHM1 SENSI:.1,OFFSET:0\r\n")
    input("Press Enter to send 'AUTOSET' to the scope")
    instr.write(b"AUTOSET START\r\n")
    print("Example Completed.")

if __name__=="__main__":
    serial_dev='/dev/ttyUSB0'
    s = None
    s = serial.Serial(serial_dev,
        baudrate=19200,         # baudrate
        bytesize=serial.EIGHTBITS,  # number of databits
        parity=serial.PARITY_NONE,  # enable parity checking
        stopbits=serial.STOPBITS_ONE,   # number of stopbits
        timeout=1,         # set a timeout value, None for waiting forever
        xonxoff=1,          # enable software flow control
        rtscts=0            # enable RTS/CTS flow control
        )
    displayTrace(s)
