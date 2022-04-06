a=int(input("輸入"))
for i in range(a+1):  
    if i%2!=0:
        print(" ")
        for u in range(a,i,-2):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
for i1 in range(a,0,-1):  
    if i1%2!=0:
        print(" ")
        for u1 in range(a,i1,-2):
            print(" ",end="")
        for j1 in range(i1):
            print("*",end="")