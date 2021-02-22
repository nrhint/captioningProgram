def convert_time(timeInSec):
    hr = int(timeInSec//(60*60))
    mn = int((timeInSec-(hr*60*60))//60)
    sec = int((timeInSec-((hr*60*60)+mn*60))//1)
    ms = str(round(timeInSec-int(timeInSec), 3))[2:]
    return "%s:%s:%s,%s"%(str(hr).zfill(2), str(mn).zfill(2), str(sec).zfill(2), ms)

def write_file(file_path, file_name, file_extension, output):
    try:
        try:
            open('%s/%s.%s'%(file_path, file_name, file_extension), 'w').write(output)
        except FileNotFoundError:
            import os
            os.mkdir(file_path)
            open('%s/%s.%s'%(file_path, file_name, file_extension), 'w').write(output)
    except:
        print('Cannot write because file "%s/%s.%s" not found'%(file_path, file_name, file_extension))
        raise Exception


def generateSRTAdvanced(dataIn, ccLength = 10):
    text = ''
    ccNumber = 0
    for caption in dataIn:
        lineOfText = caption[2]
        start = caption[0]
        if start < 0:
            start = 0
        end = caption[1]
        words = lineOfText.count(' ')
        divisions = (words//ccLength)+1
        words = lineOfText.split(' ')
        duration = end-start
        smallDuration = duration/divisions
        for div in range(0, divisions):
            tend = (div+1)*ccLength
            tstart = div*ccLength
            if div == divisions:
                captionText = words[tstart:]
            else:
                captionText = words[tstart:tend]
            finalCaptionText = ''
            for w in captionText:
                finalCaptionText += str(w)+' '
            text += str(ccNumber)+'\n'
            text += convert_time(start+(smallDuration*div))+' --> '+convert_time(start+(smallDuration*(div+1)))+'\n'
#            print(div, convert_time(start+(smallDuration*div))+' --> '+convert_time(start+(smallDuration*(div+1)))+'\n')
            text += str(finalCaptionText)+'\n'
            print(finalCaptionText)
            text += '\n'
            ccNumber += 1
    return text
