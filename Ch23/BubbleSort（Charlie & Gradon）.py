# A project by Charlie and Gradon

A=[3,4,2,5,1]

for j in range(0,4):
    for i in range (0,4):
        if A[i]>A[i+1]:
            a=A[i+1]
            A[i+1]=A[i]
            A[i]=a
print(A)
