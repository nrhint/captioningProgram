# from data.config import Config

# config = Config('config.cfg')
# i = input('Run in old mode? (y/N): ')
# if i == 'y' or i == 'Y':
#     from util.menu_old import Menu
#     menu = Menu(config)
# else:
#     from util import GUI
# #from util import GUI


##Start defining the new manus and functions:
##What I want:
##Timing for the videos, format converter

from menus import srtFromKeys, formatConverter

run = True

while run:
    print("""
1: create SRT file from keypresses
2: convert formats of SRT files
e: exit
""")
    i = input("")
    if i == "1":
        srtFromKeys.run()
    elif i == "2":
        formatConverter.run()
    elif i == "e":
        run = False
    else:
        print("Input error. Please try again")
print("Thank you!")