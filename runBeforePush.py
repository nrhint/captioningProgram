##Generate the tree file for the updater to know where to lookfor files when updating

import os

exclude = ['.\\.git', '.\\.vscode', '\\__pycache__', '.\\output', '__pycache__', 'test']

paths = []

for root, dirs, files in os.walk(".", topdown=False):
    if [ele for ele in exclude if(ele in root)]:
        pass
    else:
        print(root)
        for name in files:
            if [ele for ele in exclude if(ele in name)]:
                pass
            else:
                paths.append(os.path.join(root, name))
        for name in dirs:
            if [ele for ele in exclude if(ele in name)]:
                pass
            else:
                paths.append(os.path.join(root, name))

print(paths)
text = ''
for item in paths:
    text += str(item)+'\n'
from util.file_util import write_file, open_file
write_file('.', 'tree', 'tree', text)

##update the version file:
versionData = open_file('.', 'version', '')
change = int(input('1.2.3.4?  '))
if change < 4 : #If it is not 4: 
    if change < 3: #if it is 2 or 1
        if change < 2: #change must be 1
            newVersion = str(int(versionData[0])+1)+'.0.0.0'
        else: #change is 2
            newVersion = versionData[0:2]+str(int(versionData[2])+1)+'.0.0'
    else: #change is 3:
        newVersion = versionData[0:4]+str(int(versionData[4])+1)+'.0'
else:
    newVersion = versionData[0:6]+str(int(versionData[6])+1)
print('%s --> %s'%(versionData, newVersion))
write_file('.', 'version', '', newVersion)
print("finished. Please run git and merge with the master branch.")