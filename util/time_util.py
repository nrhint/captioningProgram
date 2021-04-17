def convert_time(timeInSec):
    hr = int(timeInSec//(60*60))
    mn = int((timeInSec-(hr*60*60))//60)
    sec = int((timeInSec-((hr*60*60)+mn*60))//1)
    ms = str(round(timeInSec-int(timeInSec), 3))[2:]
    return "%s:%s:%s,%s"%(str(hr).zfill(2), str(mn).zfill(2), str(sec).zfill(2), ms)

def secondsToFrame(timeInSeconds, fps):
    return int(timeInSeconds*fps)

def frameToSeconds(frameNumber, fps):
    return round(frameNumber/fps, 3)