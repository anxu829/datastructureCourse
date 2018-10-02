string  = ''
maxN = 3
def recursive(string , deep , maxN ):
    if deep == maxN:
        print(string)
    else:
        for i in range(10):
            temp = string + str(i)
            recursive(temp,deep +1 , maxN)
recursive('',0,2)
