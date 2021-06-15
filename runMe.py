from data.config import Config

config = Config('config.cfg')
print('As there is a GUI being implimented the option for old mode will soon be decrepitated. Please start using the new mode as the old one will be removed in the next release.')
i = input('Run in old mode? (y/N): ')
if i == 'y' or i == 'Y':
    from util.menu_old import Menu
    menu = Menu(config)
else:
    from util import GUI
#from util import GUI
