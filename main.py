import tkinter as tk
from util.formatConverter import Convert
from VTT import convert

window = tk.Tk()

window.title("Caption stuff")

greeting = tk.Label(text="Welcome! Please pick an option:")
greeting.pack()

srtFromVoice = tk.Button(text = "Autogenerate captions", width = 50, height = 0, bg = 'lightblue', fg = 'white', command = convert.convertFromVoice)
srtFromVoice.pack()

convertFormat = tk.Button(text = "Convert from vtt to srt format", width = 50, height = 0, bg = 'lightblue', fg = 'white', command = Convert)
convertFormat.pack()

##Tranform times...

window.mainloop()
window.quit()

#     elif i == "2":
#         formatConverter.run()
#     elif i == "3":
#         remapTimes.run()
#     elif i == "4":
#         autoGenCaptions.run()
#     elif i == "e":
#         run = False
#     else:
#         print("Input error. Please try again")
# print("Thank you!")
