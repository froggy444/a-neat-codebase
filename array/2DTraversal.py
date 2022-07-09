def create2DMatrix:
    mylist = [[0 for x in range(columns)] for x in range(rows)]
    for i in range(rows):
        for j in range(columns):
            mylist[i][j] = '%s,%s'%(i,j)
    print mylist

def traverse2DMatrix:
    for j in range(columns):
       for i in range(rows):
         print mylist[i][j]

