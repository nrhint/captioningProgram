##Nathan Hinton
##This will take a file given and will translate the times by a certain amount. 

############################################
##ALL TIMES ARE IN THOUSANDTHS OF A SECOND##
############################################

def stringToNumber(string):#Example strings: 00:00:01.120, 00:00:13.900, 00:04:17.899
    if len(string) != 12:
        print("You might have an error the string '%s' is more than 12 chars long."%string)
    hh = int(string[0:2])
    mm = int(string[3:5])
    ss = int(string[6:8])
    mmm = int(string[9:12])
    # print(hh, mm, ss, mmm)
    return hh*3600000+mm*60000+ss*1000+mmm

def numberToString(number):
    hh = number // 3600000
    mm = (number - (hh*3600000)) // 60000
    ss = ((number - (hh*3600000))-mm*60000) // 1000
    mmm = ((number - (hh*3600000))-mm*60000) % 1000
    # print(hh, mm, ss, mmm)
    if hh < 10:
        hh = "0%s"%hh
    if mm < 10:
        mm = "0%s"%mm
    if ss < 10:
        ss = "0%s"%ss
    if mmm < 100:
        if mmm < 10:
            mmm = "00%s"%mmm
        else:
            mmm = '0%s'%mmm

    return "%s:%s:%s:%s"%(hh, mm, ss, mmm)

def shiftTimes(times, shiftTime):
    result = []
    for time in times:
        tmp = stringToNumber(time)
        print(tmp, tmp + shiftTime)
        tmp += shiftTime
        result.append(numberToString(tmp))
    return result
