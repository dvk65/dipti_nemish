def sstr(string, sw):
    lstr=string.split(" ")
    print(lstr)
    p=0
    for i in lstr:
        print
        if sw in i:
            p=lstr.index(i)+1
            break
        else:
            p=-1
    print(p)

sstr("i love eating burger","burg")