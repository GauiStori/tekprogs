#!/usr/bin/python3

def deltaDelayMeasurement(instr):
    print("Example 7: Taking Delta--Delay Measurements")
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
    response=instr.readline()
    print(response)
    print("Press Enter after making the following connections :")
    print(" Use a power splitter or a power 'T' connecter to connect a 2ns and a 5ns")
    print(" cable to channel 1 of sampling head 1 (connect the 2ns cable first).")
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
    instr.write(b"TRACE1 DESCRIPTION:'M1'\r\n")
    input("Press Enter to set the trigger to the INTERNAL.")
    instr.write(b"TRIGGER SOURCE:INTERNAL\r\n")
    input("Press Enter to set to the time base to 10ns/div")
    instr.write(b"TBMAIN TIME:10E-9\r\n")
    input("Press Enter to change the measurement to h/w mode.")
    instr.write(b"MPARAM1 MMODE:HW\r\n")
    input("Press Enter to set the MSLIST to CROSS and save the value in memory.")
    instr.write(b"MSLIST1 CROSS;REFSET1 CURRENT:CROSS\r\n")
    input("Press Enter to turn COMPARE ON and bring up the measure menu.")
    instr.write(b"COMPARE ON;MSYS ON\r\n")
    input("Press Enter after removing the 2ns cable and connecting the 5ns cable.")
    input("Press Enter to ask the scope for the time difference between the cables.")
    instr.write(b"CROSS?\r\n")
    response=instr.readline()
    print(response)
    print(" (in seconds)")
    input("Press Enter to change the Prop--Velocity to FEET.")
    print(" (the default velocity is .7 * (speed of light)")
    instr.write(b"GRATICULE XUNIT:FEET\r\n")
    input("Press Enter after reconnecting the 2ns cable to CH1.")
    input("Press Enter to save the CROSS value in memory (in feet).")
    instr.write(b"REFSET1 CURRENT:CROSS\r\n")
    input("Press Enter after removing the 2ns cable and connecting the 5ns cable.")
    input("Press Enter to ask the scope for the feet difference between the cables.")
    instr.write(b"CROSS?\r\n")
    response=instr.readline()
    print(response)
    print("(in feet)")
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
    deltaDelayMeasurement(s)

