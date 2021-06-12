from os import O_SHORT_LIVED
from data.config import Config

config = Config('config.cfg')
i = input('Run in old mode? (y/N): ')
if i == 'y' or i == 'Y':
    from util.menu_old import Menu
    menu = Menu(config)
else:
    from util import GUI
#from util import GUI
