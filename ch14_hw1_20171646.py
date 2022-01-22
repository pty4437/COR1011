fp_r = open("L_In.txt","r")
index = fp_r.readline()

index = int(index)

A = fp_r.readline().split()

for i in range(0,6):
    A[i] = int(A[i])

B = fp_r.readline().split()

for i in range(0,7):
    B[i] = int(B[i])

sum_data = A[index] + B[index]

fp_w = open("L_Out.txt","w")
print("index = {}".format(index),file = fp_w)
print("A = ",file = fp_w,end = "")
print(A, file = fp_w)
print("B = ",file = fp_w,end = "")
print(B, file = fp_w)
print("A[{}] + B[{}] = ".format(index,index),file = fp_w, end = "")
print(sum_data, file=fp_w)

fp_w.close()
fp_r.close()
