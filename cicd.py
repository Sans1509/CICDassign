Array=[5,10,40,30,20]
n=len(Array)
array1=[0]*n

for z in range(0,n,1):
    array1[z]=Array[z]
array1.sort()
print(array1)

m=len(array1)
print(m)

for i in range(0,m,1):
    for j in range(0,m,1):
        if (array1[i]==Array[j]):
            Array[j] = i
print(Array)
print("Auto trigger check")
