#!/usr/bin/python3

import os
import csa803c_compare
import csa803c_delay_measurements
import csa803c_display
import csa803c_signal_processing
import csa803c_automated_measurements
import csa803c_complex_traces
import csa803c_delta_delay
import csa803c_multiple_traces
import csa803c_tdr
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

while True:
    os.system("clear")

    print("Examples Menu\n")
    print(" 1) Displaying a Single Waveform")
    print(" 2) Managing Multiple Waveforms")
    print(" 3) Defining Complex Waveforms")
    print(" 4) Using Signal Processing & Transferring a Waveform")
    print(" 5) Taking Automated Measurements")
    print(" 6) Taking Delay Measurements")
    print(" 7) Taking Delta--Delay Measurements From a Reference Trace")
    print(" 8) Comparing Displayed Traces to Stored Waveforms")
    print(" 9) Taking TDR Measurements")
    #PRINT
    print("Enter the number of the example you wish to run,")
    print("press 'Q' to quit without exiting BASIC,")
    print("or press 'S' to quit and exit BASIC.")
    prognum = input()
    if prognum == 'Q' or prognum == 'q':
        sys.exit(0)
    #IF LEFT$(PROGNUM$,1)=")S") OR LEFT$(PROGNUM$,1)=")s") THEN SYSTEM
    prognum = int(prognum)
    if prognum == 1:
        csa803c_display.displayTrace(s)
    elif prognum == 2:
        csa803c_multiple_traces.multipleTraces(s)
    elif prognum == 3:
        csa803c_complex_traces.complexTraces(s)
    elif prognum == 4:
        csa803c_signal_processing.doSignalProcessing(s)
    elif prognum == 5:
        csa803c_automated_measurements.doAutomatedMeasurements(s)
    elif prognum == 6:
        csa803c_delay_measurements.delayMeasurements(s)
    elif prognum == 7:
        csa803c_delta_delay.deltaDelayMeasurement(s)
    elif prognum == 8:
        csa803c_compare.traceCompare(s)
    elif prognum == 9:
        csa803c_tdr.doTdrMeasurement(s)
