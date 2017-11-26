#!/usr/bin/python3

#LOCATE ,,1,0,7
def traceCompare(instr):
    print("Example 8: Comparing Traces")
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
    print(" Connect a 500kHz to 5MHz sinewave signal (.5V to 1V PP) to channel 1.")
    input(" Connect trigger out of your signal source to the TRIGGER INPUT of the scope.")
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
    input("Press Enter to send 'AUTOSET' to the scope")
    instr.write(b"AUTOSET MODE:PERIOD,START\r\n")
    input("Press Enter to store trace1 to sto1.")
    instr.write(b"STORE TRA1:STO1\r\n")
    input("Press Enter to remove trace 1.")
    instr.write(b"REMOVE TRACE1\r\n")
    input("Press Enter to recall sto1.")
    instr.write(b"TRACE1 DESCR:'STO1'\r\n")
    input("Press Enter to create a difference trace showing only the noise.")
    instr.write(b"TRACE1 DESC:'STO1-M1'\r\n")
    input("Press Enter to find the RMS value of the noise over the WHOLE record.")
    instr.write(b"MPARAM1 DAINT:WHOLE;MSLIST1 RMS;MEAS1?\r\n")
    response=instr.readline()
    print(response)
    print("Example Completed.")
    input("Press enter to return to menu")
    #CLOSE 1

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
    traceCompare(s)
