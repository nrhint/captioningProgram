##Nathan Hinton
##This is a wrapper module for the program to be given a filename and it will write the caption ro that path

import sys
import subprocess
from time import sleep
import generateSrt
import fix_caps

##Keywords: path to convert, [outputFilename]
print("Converting from video to srt...")
output = generateSrt.convert(sys.argv[1])
print(output)

print("Reformatting SRT file to have caps in the right places...")
fix_caps.fix_caps(output, sys.argv[2])

with open(filename, 'w') as file:
        file.write(data)