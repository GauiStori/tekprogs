#!/usr/bin/python3

import sys
import usbtmc

fname = sys.argv[1]

osc = usbtmc.Instrument("USB::0x0699::0x03a4::INSTR")
#osc.write("SAVE:IMAGE myimage.png")
osc.write("HARDCOPY:INKSAVER ON")
osc.write("SAVE:IMAGE:FILEFORMAT PNG")
osc.write("HARDCOPY START")
picture = osc.read_raw()

f=open(fname,'wb')
f.write(picture)
f.close()
