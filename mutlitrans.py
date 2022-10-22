import copy

def shuffle(a):
    b=copy.deepcopy(a)
    z=0
    for row in range(len(a)-1,-1,-1):
        for col in range(len(a[row])):
            b[col][z]= a[row][col]
        z=z+1 
    print(b)    
a=[[1,2,3],[4,5,6],[7,8,9]]
print(a)
shuffle(a)