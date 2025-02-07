import settings
def readhighscore():
    return str(settings.highscore)


"""
file = open("text.txt", 'a+')


def appendscore(x):
    new = str(x) + '\n'
    file.write(new)


def readhighscore():
    file.seek(0)
    arr = []
    x = file.readline()
    while x != '':
        arr.append(x)
        x = file.readline()

    # To get first character
    newarr = []
    for i in arr:
        if i != '':
            newarr.append(int(i[0: len(i) - 1]))

    if len(newarr) == 0:
        newarr.append(0)

    x = max(newarr)
    return(x)
"""