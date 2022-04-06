a=int(input("輸入"))
b=str(1)
w=0
b1=0
for t in range(3,a+1,2):
    b=b+str(t)
    b1+=1
for r in range(a-2,0,-2):
    b=b+str(r)
    b1+=1
if b1%2==0:
    w=b1/2
else:
    w=(b1-1)/2
w=int(w)
for i in range(1,a+1,2):
    for u in range(w):
        if i!=a: 
            print(" ",end="") 
            print(" ",end="") 
        else:
            print(" ",end="")
    if i!=a:
        print(i)
    else:
        print(b)
for f in range(a-2,0,-2):
    for f1 in range(w):
        print(" ",end="") 
        print(" ",end="")
    print(f)
