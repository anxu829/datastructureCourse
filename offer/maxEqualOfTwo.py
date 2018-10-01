lis1 = ['A','B','A','C','D','E','F']
lis2 = ['A','B','C','D','A','E','F']

len_lis1 = len(lis1)
len_lis2 = len(lis2)
A = [ [0 for j in range(len_lis2) ] for i in range(len_lis1)]
max_ = -1
for  i in range(len_lis1):
    for j in range(len_lis2):
        if i == 0:
            A[i][j] = 1
        elif j == 0:
            A[i][j] = A[i-1][j]
        else:
            if lis1[i] == lis2[j] :
                A[i][j] = A[i-1][j-1] +1
            else:
                A[i][j] = A[i][j-1]
        if A[i][j] > max_:
            max_ = A[i][j]
