#!/usr/bin/python3

#LOCATE ,,1,0,7
def doAutomatedMeasurements(instr):
    print("Example 5: Taking Automated Measurements\n")
    print("Ensure that the cable is connected and the scope's parameters are")
    print("set accordingly : (major menu UTILITY, minor menu RS232 Parameters)")
    print(" Baud 19200, Echo OFF, Stop Bits 1, Parity NONE, Flagging HARD")
    print(" Delay 0, EOL String CR/LF, Verbose OFF")
    input("Press Enter when ready")
    input("Press Enter to ask for the scope's ID")
    instr.write(b"ID?\r\n")
    response=instr.readline()
    print(response)
    print("Press Enter after making the following connections :")
    print(" Connect a 1 MHz sine wave, .5 to 1V P--P to channel 1.")
    print(" Connect the generator trigger out to the scope TRIGGER INPUT.")
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
    input("Press Enter to set the trigger to EXTERNAL.")
    instr.write(b"TRIGGER SOURCE:EXTERNAL\r\n")
    input("Press Enter to send 'AUTOSET' to the scope")
    instr.write(b"AUTOSET MODE:PERIOD,START\r\n")
    input("Press Enter to calculate RMS and FREQUENCY on the SELECTed TRACE.")
    instr.write(b"RMS?;FREQ?\r\n")
    response=instr.readline()
    print("(a histogram was calculated for each measurement query)")
    print(response)
    input("Press Enter to put RMS and FREQUENCY into the measure list for TRACE1.")
    instr.write(b"MSLIST1 RMS,FREQ\r\n")
    print("Press Enter to get the query results")
    a=input("(only one histogram is made for all measurements)")
    instr.write(b"MEAS1?\r\n")
    response=instr.readline()
    print(response)
    input("Press Enter to setup the statistical data.")
    instr.write(b"STATISTICS MEAS:RMS,N:24;MSYS ON\r\n")
    input("Press Enter to fetch the statistical data.")
    instr.write(b"STAT?\r\n")
    response=instr.readline()
    print(response)
    input("Press Enter to change the measurement zones on the trace.")
    instr.write(b"MPARAM1 LMZONE:15,RMZONE:85\r\n")
    input("Press Enter to measure CHM1 freq with s/w (using new zones).")
    instr.write(b"MPARAM1 MMODE:SW;MSLIST1 FREQ;MEAS1?\r\n")
    response=instr.readline()
    print(response)
    input("Press Enter to measure CHM1 freq with h/w (zones not used).")
    instr.write(b"MPARAM1 MMODE:HW;MEAS1?\r\n")
    response=instr.readline()
    print(response)
    input("Press Enter to remove TRACE 1")
    instr.write(b"REMOVE TRACE1\r\n")
    print("Example Completed.")
    # CLOSE 1
    # LOAD ")MENU.BAS"),R

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
    doAutomatedMeasurements(s)
