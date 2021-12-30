##Nathan Hinton
##This is a wrapper module for the program to be given a filename and it will write the caption ro that path

import sys
import test_srt
import fix_caps
import tkinter.filedialog
import tkinter as tk


def convertFromVoice():
    window = tk.Tk()

    window.title("Change format from VTT to SRT")

    filename = tkinter.filedialog.askopenfile()
    file = filename.read()

    ##Keywords: path to convert, [outputFilename]
    print("Converting from video to srt...")
    output = test_srt.convert(sys.argv[1])
    print(output)

    print("Reformatting SRT file to have caps in the right places...")
    fix_caps.fix_caps(output, sys.argv[2])

