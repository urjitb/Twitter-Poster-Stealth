import os
path = '/Users/urjitb/Documents/twitimgs/jpgs'
files = os.listdir(path)
i = 1

os.chdir(path)
for file in files:
    os.rename(file, str(i)+'tw.jpg')
    i = i+1