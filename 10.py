n=input("輸入ｎ、ｍ").split(" ")
a=[]
while int(n[0])!=0 and int(n[1])!=0:
    for i in range(int(n[0])):
        a.append(input("輸入矩陣值第i列為").split(" "))
    for j in range(int(n[1])):
        b=[]
        for o in range(int(n[0])):
            b.append(a[o][j])
        print("輸出矩陣第%s列為%s"%(j,str(b)))
    break

