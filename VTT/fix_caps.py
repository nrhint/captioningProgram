##Nathan Hinton
##This will take a file that is inputed and capatalize words

##TODO:
##Read the words to change from a file

def fix_caps(data, filename = 'output.srt'):
    words = {'god':'God', 'book of mormon':'Book of Mormon', 'church of':'Church of', 'latter day saints':'Latter-day Saints', 'jesus':'Jesus', 'christ':'Christ', 'joseph smith':'Joseph Smith', 'joseph\'s':'Joseph\'s', 'holy bible':'Holy Bible', ' he ':' He ', ' his ':' His ', 'him':'Him', 'father':'Father', 'profits':'prophets', 'holy ghost':'Holy Ghost', ' i ':' I ', ' lord ':' Lord ', 'savior':'Savior'}
    keys = words.keys()

    for key in keys:
       while key in data:
           print('replacing %s occourance(s) of %s'%(data.count(key), key))
           data = data.replace(key, words[key])

    with open(filename, 'w') as file:
        file.write(data)
