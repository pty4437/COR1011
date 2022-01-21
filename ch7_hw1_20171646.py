L = [1,3,5,7,9]

tmp = L[0]

L[0:len(L)-1] = L[1:len(L)]

L[len(L)-1] = tmp

print(L)
    
