l = [2,3,1,0,2,5,3]
final = -1
for idx in range(len(l)):
    while( not l[idx] == idx):
        val = l[idx]
        if l[val] == val:
            final = val
            break 
        else:
            l[val] , l[idx] =  l[idx]   , l[val] 
    if final != -1:
        break

