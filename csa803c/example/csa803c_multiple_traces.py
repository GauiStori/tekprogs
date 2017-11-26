#!/usr/bin/python3


def multipleTraces(instr):
    print("Example 2: Managing Multiple Traces")
    print("Ensure that the cable is connected and the scope's parameters are")
    print("set accordingly : (major menu UTILITY, minor menu RS232 Parameters)")
    print(" Baud 19200, Echo OFF, Stop Bits 1, Parity NONE, Flagging HARD")
    print(" Delay 0, EOL String CR/LF, Verbose OFF")
    input(" Press Enter when ready")
    input("Press Enter to ask for the scope's ID")
    instr.write(b"ID?\r\n")
    response=instr.readline()
    print(response)
    print("Press Enter after making the following connections :")
    print(" Connect a 500kHz to 5MHz signal (.5V to 1V PP) to channel 1 (head 1).")
    print(" Connect trigger out of your signal source to the TRIGGER INPUT of the scope.")
    print(" Use a power splitter or a power 'T' connecter to connect your trigger out")
    input(" to channel 2 (head 1)")
    input("Press Enter to initialize scope.")
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
    input("Press Enter to set the trigger to EXTERNAL")
    instr.write(b"TRIGGER SOURCE:EXTERNAL\r\n")
    input("Press Enter to manually set the size and position of the trace.")
    instr.write(b"TBMAIN TIME:2E-6;MAINPOS 55E-9;CHM1 SENSI:.2,OFFSET:-1\r\n")
    input("Press Enter to send 'AUTOSET' to the trace in period mode.")
    instr.write(b"AUTOSET MODE:PERIOD,START\r\n")
    input("Press Enter to send 'AUTOSET' in the edge mode")
    instr.write(b"AUTOSET MODE:EDGE,START\r\n")
    input("Press Enter to setup trace2 from sampling head 1, channel 2.")
    instr.write(b"TRACE2 DESCRIPTION:'M2';AUTOSET HORIZ:OFF,START,HORIZ:ON\r\n")
    input("Press Enter to select trace1 as the highlighted trace.")
    instr.write(b"SELECT TRACE1\r\n")
    print("Now we will ask for the trace count and their numbers.")
    input("Also, we will ask for their descriptions. (Press Enter)")
    instr.write(b"TRANUM?;TRALIST?\r\n")
    response=instr.readline()
    print(response)
    instr.write(b"TRA1? DESCR;TRA2? DESCR\r\n")
    response=instr.readline()
    print(response)
    input("Press Enter to create the second graticule")
    instr.write(b"DISP GRAT:DUAL\r\n")
    input("Press Enter to move trace1 to the upper graticule")
    instr.write(b"ADJTRACE1 GRLOC:UPPER\r\n")
    input("Press Enter to reduce back to the single graticule")
    instr.write(b"DISP GRAT:SINGLE\r\n")
    input("Press Enter to remove TRACE1 and TRACE2.")
    instr.write(b"REMOVE TRACE1,TRACE2\r\n")
    print("Example Completed.")

if __name__=="__main__":
    import serial
    serial_dev='/dev/ttyUSB0'
    s = None
    s = serial.Serial(serial_dev,
        baudrate=19200,         # baudrate
        bytesize=serial.EIGHTBITS,  # number of databits
        parity=serial.PARITY_NONE,  # enable parity checking
        stopbits=serial.STOPBITS_ONE,   # number of stopbits
        timeout=1,         # set a timeout value, None for waiting forever
        xonxoff=0,          # enable software flow control
        rtscts=1            # enable RTS/CTS flow control
        )
    multipleTraces(s)
