##Nathan Hinton
##This is for opening and handeling files in a consistent manner
##Used

def open_file(file_path, file_name, file_extension):
    try:
        return open('%s/%s.%s'%(file_path, file_name, file_extension), 'r').read()
    except FileNotFoundError:
        print('File not found! Invalid path of %s/%s.%s'%(file_path, file_name, file_extension))
        return 'Error'

def write_file(file_path, file_name, file_extension, output):
    try:
        try:
            print('trying to write file at: %s'%('%s/%s.%s'%(file_path, file_name, file_extension)))
            open('%s/%s.%s'%(file_path, file_name, file_extension), 'w').write(output)
        except FileNotFoundError:
            import os
            os.mkdir(file_path)
            open('%s/%s.%s'%(file_path, file_name, file_extension), 'w').write(output)
    except Exception as e:
        print('unable to write file.\nError: %s\nPath: %s/%s.%s'%(e, file_path, file_name, file_extension))

def parse_config(configData):
    #See the config file for the exact information about what the numbers mean
    configData = configData.split('\n')
    finishedList = []
    for line in configData:
        try:
            if line[0] == '#':#A commented line
                pass
            else:
                try:
                    finishedList.append(int(line))
                except ValueError:
                    finishedList.append(line)
        except IndexError:#A blank line
            pass
    return finishedList

def parseVtt(filepath):
    pass