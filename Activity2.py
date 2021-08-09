intro = input("enter intro = ")
cc = 0
wc = 1
for i in intro:
    cc = cc+1
    if(i== " "):
        wc = wc+1
print("# of words in the intro are ")
print(wc)
print("# of characters in the intro are ")
print(cc)