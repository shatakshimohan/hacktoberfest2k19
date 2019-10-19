n= int (input('enter integer:'))
print('factors are:')
i=1
while (i<=n):
    k=0
    if(n%1==0):
        j=1
        while(j<=1):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            print(i)
    i=i+1
