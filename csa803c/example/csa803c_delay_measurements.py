#!/usr/bin/python3

def delayMeasurements(instr):
    print("Example 6: Taking Delay Measurements")
    print("Ensure that the cable is connected and the scope's parameters are")
    print("set accordingly : (major menu UTILITY, minor menu RS232 Parameters)")
    print(" Baud 9600, Echo OFF, Stop Bits 1, Parity NONE, Flagging HARD")
    print(" Delay 0, EOL String CR/LF, Verbose OFF")
    input(" Press Enter when ready")
    #a=''
    #while  a != "COM1" and a != "COM2":
    #    a = input("Press Enter for using COM1 (default), else type COM2")
    #    if a == "":
    #        a = "COM1"
    #print("We are opening %s at 9600 baud, no parity, and 1 stop bit."%a)
    #instr = OPEN A:9600,N,8,1
    input("Press Enter to ask for the scope's ID")
    instr.write(b"ID?\r\n")
    response=instr.read()
    print(response)
    print("Press Enter after making the following connections :")
    print(" Use a power splitter or a power 'T' connecter to connect a 2ns and a 5ns")
    print(" cable to channel 1 and 2 of sampling head 1.")
    input(" Connect the 'T' or splitter to the CALIBRATOR of the 11800")
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
    instr.write(b"TRACE1 DESCRIPTION:'m1'\r\n")
    input("Press Enter to set the trigger to the INTERNAL.")
    instr.write(b"TRIGGER SOURCE:INTERNAL\r\n")
    input("Press Enter to set to the time base to 10ns/div")
    instr.write(b"TBMAIN TIME:10E-9\r\n")
    input("Press Enter to turn on the cursor readout.")
    instr.write(b"CURSOR READOUT:ON\r\n")
    input("Press Enter to select horizontal bars.")
    instr.write(b"CURSOR TYPE:HBARS\r\n")
    input("Press Enter to move the bars near the middle of the CRT.")
    instr.write(b"H1BAR YDIV:1;H2BAR YDIV:-1\r\n")
    input("Press Enter to go to paired cursors on trace 1.")
    instr.write(b"CURSOR TYPE:PAIRED\r\n")
    input("Press Enter to position the cursors on divisions 1 and 9.")
    instr.write(b"DOT1ABS XDIV:-4;DOT2ABS XDIV:4\r\n")
    instr.write(b"DOT1ABS? YCOORD;DOT2ABS? YCOORD;PP?\r\n")
    response=instr.readline()
    print("Here are the vertical values from each cursor:")
    print(response)
    #M$=MID$(RESPONSE$,INSTR(RESPONSE$,"):"))+1)
    #PP=ABS(VAL(M$)--VAL(MID$(M$,INSTR(M$,"):"))+1)))
    print("Here is the Peak to Peak value from the cursors:");PP
    #M$=MID$(RESPONSE$,INSTR(RESPONSE$,")PP"))+1)
    #PP=VAL(MID$(M$,INSTR(M$,") "))+1))
    print("Here is the Peak to Peak value from the measurement system:");PP
    input("Press Enter to create a second trace on the lower graticule.")
    instr.write(b"TRACE2 DESC:'M2';DISPLAY GRAT:DUAL;ADJTRA1 GRLOC:UPPER;ADJTRA2 GRLOC:LOWER\r\n")
    instr.write(b"SELECT TRACE1;CURSOR TYPE:SPLIT,REFERENCE:TRACE2\r\n")
    print("You may use the cursors to make a timing measurement, but we will")
    print(" show you how to make accurate automatic measurements with the ")
    print(" measurement system.")
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
        xonxoff=1,          # enable software flow control
        rtscts=0            # enable RTS/CTS flow control
        )
    delayMeasurements(s)
