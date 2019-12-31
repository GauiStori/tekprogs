The tool is written in "C" and must be compiled adding a file (gpib-32.obj) for the used GPIB adapter.
If you have trouble doing it I can attach a version compiled for NI GPIB adapters, it definitely works for 
NI GPIB-USB-HS and the old NI GPIB PCII/IIA, I don't know if it works with other non NI adapters.

The command to be given to back up the NVRAM is:
tektool -r nvram.bin -b 0x04000000 -l 0xa0000
Where: 
-r : Read command
nvram.bin: Backup file name
-b 0x04000000: NVRAM start address 
-l 0xa0000: NVRAM file lenght 

The starting address is right for TDS784D/TDS794D and my TDS784C.
Check on TDS620A service manual that the start address is the same otherwise you save the wrong data.


Additions by Gudjon:

The instrument must have primary address 1.

I have tested it on Linux and it works until reading the first response.
The password may be wrong or there is a problem with the memory alignment in
the struct. I tried the program on a 64 bit computer.

It should work with any GPIB adapter.

For the TDS694C the command line is:
tektool -r file.bin -b 0x04000000 -l 0x20000
