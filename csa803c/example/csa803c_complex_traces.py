#!/usr/bin/python3

def complexTraces(instr):
    print("Example 3: Defining Complex Traces\n")
    print("Ensure that the cable is connected and the scope's parameters are")
    print("set accordingly : (major menu UTILITY, minor menu RS232 Parameters)")
    print(" Baud 9600, Echo OFF, Stop Bits 1, Parity NONE, Flagging HARD")
    print(" Delay 0, EOL String CR/LF, Verbose OFF")
    input(" Press Enter when ready")
    #A$='")'
    #WHILE A$<>")COM1") AND A$<>")COM2") AND A$<>")com2")
    #input("Press Enter for using COM1 (default), else type COM2. ")
    #IF A$='")' THEN A$=")COM1")
    #WEND
    #print("We are opening ");A$;") at 9600 baud, no parity, and 1 stop bit.")
    #OPEN A$+"):9600,N,8,1") AS #1
    print("Press Enter to ask for the scope's ID")
    instr.write(b"ID?\r\n")
    response=instr.readline()
    print(response)
    print("Press Enter after making the following connections :")
    print(" Use a power splitter or a power 'T' connecter to connect a 2ns and a 5ns")
    print(" cable to channel 1 and 2 of sampling head 1.")
    input(" Connect the 'T' or splitter to the CALIBRATOR")
    input("Press Enter to initialize scope.")
    instr.write(b"INIT\r\n")
    a=''
    while a != 'y' and a != 'Y' and a != 'n' and a != 'N':
        a=input("Do you want to watch the commands in DEBUG mode ? (y/n)")
        if a == 'y' or a == 'Y':
            instr.write(b"DEBUG RS232:ON\r\n")
        else:
            instr.write(b"DEBUG RS232:OFF\r\n")
    input("Press Enter to setup 2 traces from channel 1 & 2.")
    instr.write(b"TRACE1 DESCRIPTION:'M1';TRACE2 DESC:'M2'\r\n")
    input("Press Enter to set the trigger to INTERNAL.")
    instr.write(b"TRIGGER SOURCE:INTERNAL\r\n")
    input("Press Enter to set the main timebase to 10ns/div.")
    instr.write(b"TBMAIN TIME:10E-9;CHM1 SENSITIVITY:100E-3;CHM2 SENSITIVITY:100E-3\r\n")
    input("Press Enter to create trace3 as the difference of channel 1 & 2")
    instr.write(b"TRACE3 DESCRIPTION:'M1-M2'\r\n")
    input("Press Enter to remove traces 1 and 2.")
    instr.write(b"REMOVE TRACE1,TRACE2\r\n")
    input("Press Enter to make a window on trace 3.")
    instr.write(b"TRACE4 DESCRIPTION:'M1-M2 ON WIN'\r\n")
    input("Press Enter to change the window time base and position.")
    instr.write(b"TBWIN TIME:1E-9;WIN4 POS:73E-9\r\n")
    input("Press Enter to make a second window on trace 3.")
    instr.write(b"TRACE5 DESCRIPTION:'M1-M2 ON WIN'\r\n")
    input("Press Enter to change the window position on trace 5.")
    instr.write(b"WIN5 POS:86E-9\r\n")
    input("Press Enter to add trace separation to Trace 4 and 5.")
    instr.write(b"ADJTRACE4 TRSEP:-1;ADJTRACE5 TRSEP:1\r\n")
    print("Example Completed.")
    #CLOSE 1
    #LOAD ")MENU.BAS"),R


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
    complexTraces(s)
    
