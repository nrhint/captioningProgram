##Nathan Hinton
##This will take a file that is inputed and capitalize words

def fix_caps(data, changeWords = True):
    if changeWords:
        words = {'god':'God', 'book of mormon':'Book of Mormon', 'church of':'Church of', 'latter day saints':'Latter-day Saints', 'jesus':'Jesus', 'christ':'Christ', 'joseph smith':'Joseph Smith', 'joseph\'s':'Joseph\'s', 'holy bible':'Holy Bible', ' he ':' He ', ' his ':' His ', 'him':'Him', 'father':'Father', 'profits':'prophets', 'holy ghost':'Holy Ghost'}
        keys = words.keys()

        for key in keys:
           while key in data:
               print('replacing %s occurrence(s) of %s'%(data.count(key), key))
               data = data.replace(key, words[key])
    return data
    
