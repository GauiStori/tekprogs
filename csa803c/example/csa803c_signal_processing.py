#!/usr/bin/python3

def doSignalProcessing(instr):
    print("Example 4: Using Signal Processing & Transferring a Waveform\n")
    print("* * * You must have invoked BASIC with a COM buffer of 5000 bytes")
    print("* * * to run this example.")
    print("* * * Sample invocation: BASIC /C:5000 or BASICA /C:5000 or QB /C:5000")
    print("* * * If you have not invoked BASIC in this way, this example WILL NOT RUN;")
    print("* * * get out of BASIC and re--invoke.\n")
    print("Ensure that the cable is connected and the scope's parameters are")
    print("set accordingly : (major menu UTILITY, minor menu RS232 Parameters)")
    print("  Baud 19200,  Echo OFF,  Stop Bits 1,  Parity NONE,  Flagging HARD") 
    print("  Delay 0,    EOL String CR/LF,        Verbose OFF")
    input("  Press Enter when ready")
    input("Press Enter to ask for the scope's ID")
    instr.write(b"ID?\r\n")
    response=instr.readline()
    print(response)
    print("Press Enter after making the following connections :")
    print(" Connect a 50 MHz sine wave, 50 mV p--p, to channel 2.")
    print(" Connect the Calibrator signal to channel 1.")
    input("Press Enter to initialize scope.")
    instr.write(b"INIT\r\n")
    a=''
    while a != 'y' and a != 'Y' and a != 'n' and a != 'N':
        a=input("Do you want to watch the commands in DEBUG mode ? (y/n)")
        if a == 'y' or a == 'Y':
            instr.write(b"DEBUG RS232:ON\r\n")
        else:
            instr.write(b"DEBUG RS232:OFF\r\n")
    input("Press Enter to set the trigger to INTERNAL.")
    instr.write(b"TRIGGER SOURCE:INTERNAL\r\n")
    input("Press Enter to define an averaged and a normal summation--trace with M1 and M2")
    instr.write(b"TRACE1 DESCR:'M1+M2';TRACE2 DESCR:'AVG(M1+M2)'\r\n")
    input("Press Enter to set the time base and vertical size of trace 2")
    instr.write(b"TBMAIN TIME:10E--9;CHM1 SENSI:.2;CHM2 SENSI:.2\r\n")
    input("Press Enter to set the number of averages to 12.")
    instr.write(b"NAVG 12\r\n")
    input("Press Enter to begin a conditional acquisition.")
    print("The average countdown will be complete when 'n' = zero.")
    instr.write(b"CONDACQ TYPE:AVG\r\n")
    for i in range(1000):
        instr.write(b"CONDACQ? REMAINING\r\n")
        response=instr.readline()
        print(response)
        #REMAINING=VAL(MID$(RESPONSE$,INSTR(RESPONSE$,"):"))+1))
    input("\nPress Enter to send the 512 point curve to the PC.")
    #GOSUB 805
    input("Press Enter to turn the average function off for TRACE2.")
    instr.write(b"AVG OFF;CONDACQ TYPE:CONTINUOUS\r\n")
    input("Press Enter to set the display for infinite persistence.")
    instr.write(b"DISPLAY TYPE:INFINITE\r\n")
    input("Press Enter to set the display to variable persistence.")
    instr.write(b"DISPLAY TYPE:VARIABLE\r\n")
    input("Press Enter to set the display to color graded.")
    instr.write(b"DISPLAY TYPE:GRADED\r\n")
    input("Press Enter to set the display back to normal.")
    instr.write(b"DISPLAY TYPE:NORMAL\r\n")
    print("Press Enter to smooth channel 1.")
    input(" (note: Turning on smoothing for CHM1 also smooths CHM2)")
    instr.write("CHM1 SMOOTHING:ON;CHM2? SMOOTHING\r\n")
    response=instr.readline()
    print(response)
    input("Press Enter to turn off the smoothing.")
    instr.write("CHM1 SMOOTHING:OFF;CHM2? SMOOTHING")
    response=instr.read()
    print(response)
    input("Press Enter to set the main record to 2048 and the window to 5120")
    instr.write("TBMAIN LENGTH:2048;TBWIN LENGTH:5120")
    input("Press Enter to send the 2048 point curve to the PC.")
    #GOSUB 810
    print("Example Completed.")
    return
    """# The following line sets the output waveform to be TRACE2; the waveform
    # will be sent in 16 bit binary format and each word will be sent as low
    # order byte followed by high order byte; lastly, ask for the data.
    instr.write("OUTPUT TRACE2;ENCDG WAV:BIN;BYT.OR LSB;CURVE?")
    # read one byte off the bus
    A$=INPUT$(1,#1)
    # loop until we see the percent sign
    WHILE A$<>")%") : A$=INPUT$(1,#1) :WEND
    # next, read in the data length count (always in MSB,LSB word format)
    HB$=INPUT$(1,#1) : LB$=INPUT$(1,#1)
    # compute the byte count
    BYTE.CNT%=ASC(HB$)*256+ASC(LB$)
    # convert the byte count into waveform point count
    NR.PT%=(BYTE.CNT%--1)/2 : DIM WFM%(NR.PT%)
    # read in the waveform in one word at a time
    FOR I%=1 TO NR.PT% : WFM%(I%)=CVI(INPUT$(2,#1)) :print(".");: NEXT
    # lastly, read in the checksum (non--zero only for stored waveforms)
    LINE INPUT #1,CHKSUM$
    print()
    input("Waveform copy complete. Press Enter to graph.")
    # check for graphics adapter
    DEF SEG = (&H40)
    CRTTYPE = PEEK(&H49)
    DEF SEG = 0
    IF CRTTYPE =7 THENprint("Graphics not available.") : ERASE WFM% : RETURN
    # switch to 640x200 (try SCREEN 9 for EGA if you use QuickBASIC)
    SCREEN 2
    # set the screen to be zero +/-- 32k by record--length (e.g. 1024)
    WINDOW(1,--32767)--(nr.pt%,32767)
    # plot each point as a pixel
    for i in range(i%=1 TO nr.pt% : PSET(i%,wfm%(i%)) : NEXT
    input("Press Enter to clear the screen.")
    # remove the waveform array and set the screen back to text
    ERASE WFM% : SCREEN 0
    RETURN"""

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
    doSignalProcessing(s)

