##Nathan Hinton
##This is for updating the program and checking for updates

from requests import get as getUrl

def runUpdate(config):
    print('running updater...')
    if checkForUpdates(config):
        downloadUpdates()

def checkForUpdates(config):
    print('checking for updates...')
    url = 'https://github.com/nrhint/captioningProgram/blob/develop/version'
    data = getUrl(url)
    text = data.text
    pointer = text.index('id="LC1"')
    while text[pointer] != '>':
        pointer += 1
    start = pointer+1
    while text[pointer] != '<':
        pointer += 1
    end = pointer
    onlineVersion = text[start:end]
    print('most recent version: %s'%onlineVersion)
    print('your version is %s'%config.version)
    if onlineVersion != config.version:
        i = input('update the program? (Y/n)  ')
        if i != 'n':
            downloadUpdates()

def downloadUpdates():
    print('downloading updates...')
    baseUrl = 'https://raw.github.com/nrhint/captioningProgram/develop'
    tree = getUrl(baseUrl+'/tree.tree')
    tree = tree.text.split('\n')
    for path in tree:
        tmpUrl = baseUrl+str(path[1:])
        tmpUrl = tmpUrl.replace('\\', '/')
        print(tmpUrl)
        file = getUrl(tmpUrl)
        open(path, 'w').write(file.text)
        print("%s downloaded..."%tmpUrl)
    print('Finished downloading. Please restart the program...')
    from time import sleep
    sleep(3)
    quit()