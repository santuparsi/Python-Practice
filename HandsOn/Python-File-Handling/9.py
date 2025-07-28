import os
if(os.path.exists('note3.txt')):
    os.remove()
else:
    print('file not exisit')
# delete folder
os.rmdir('MyFolder')