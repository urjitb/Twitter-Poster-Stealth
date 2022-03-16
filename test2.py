file = open("tweets")
tweetlist = []
for st in file:
    if "https:" in st:
        tweetlist.append(st[0:len(st)-23])
    else:
         tweetlist.append(st)

print(tweetlist)