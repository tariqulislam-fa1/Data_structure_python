# Selection sorting in python.
n=int(input())
a=list(map(int,input("Enter array value: ").split()))[:n]

for i in range(n-1):
    for j in range(i+1,n,1):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]

print(a)