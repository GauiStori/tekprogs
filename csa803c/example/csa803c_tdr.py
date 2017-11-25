#!/usr/bin/python3

#LOCATE ,,1,0,7
def doTdrMeasurement(instr):
    print("Example 9: Taking TDR Measurements\n")
    print("Ensure that the cable is connected and the scope\'s parameters are")
    print("set accordingly : (major menu UTILITY, minor menu RS232 Parameters)")
    print("Baud 9600, Echo OFF, Stop Bits 1, Parity NONE, Flagging HARD")
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
    response = instr.readline()
    print(response)
    print("Press Enter after connecting your cables to the scope. Requirements:")
    input(" Connect a 5ns SMA cable to CHM1 (leave it open ended)")
    input("Press Enter to initialize scope")
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
    input("Press Enter to set the trigger to INTERNAL")
    instr.write(b"TRIGGER SOURCE:INTERNAL\r\n")
    input("Press Enter to turn on the TDR pulse")
    instr.write(b"CHM1 TDRSTATE:ON\r\n")
    input("Press Enter to change the x to FEET")
    instr.write(b"GRATICULE XUNIT:METER\r\n")
    input("Press Enter to calibrate CHM1 for TDR amplitude")
    instr.write(b"CALM1 TDRAMPLITUDE:350E-3\r\n")
    input("Press Enter to send AUTOSET")
    instr.write(b"AUTOSET START\r\n")
    input("Press Enter to put CROSS in the measurement list")
    instr.write(b"MSLIST1 CROSS\r\n")
    input("Press Enter to set the measurement parameters")
    instr.write(b"MPARAM1 MLEVELMODE:ABSOLUTE,REFLEVEL:-300E-3\r\n")
    input("Press Enter to save one timing value to memory")
    instr.write(b"REFSET1 CURRENT:CROSS\r\n")
    input("Press Enter to turn COMPARE ON")
    instr.write(b"COMPARE ON\r\n")
    input("Press Enter to adjust the reference level")
    instr.write(b"MPARAM1 REFLEVEL:-50E-3\r\n")
    input("Press Enter to ask the scope for the measurement")
    instr.write(b"MEAS1?;GRAT? XUNIT\r\n")
    response = instr.readline()
    print(response)
    print("Example Completed.")
    #CLOSE 1
    #LOAD ''MENU.BAS'',R
    

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
    doTdrMeasurement(s)

