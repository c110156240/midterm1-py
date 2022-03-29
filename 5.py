a=int(input("請輸入階層值"))
b=1
c=1
while b<a:
    b=b*c
    c=c+1
print("超過"+str(a)+"的階層為"+str(c-1))
    
