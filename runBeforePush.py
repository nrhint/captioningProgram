##Generate the tree file for the updater to know where to lookfor files when updating

import os

exclude = ['.\\.git', '.\\.vscode', '\\__pycache__', '.\\output', '__pycache__']

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
from util.file_util import write_file
write_file('.', 'tree', 'tree', text)