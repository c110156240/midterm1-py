a=input("請輸入考試次數及學生數").split(" ")
b=[]
c=[]
d=0
for i in range(int(a[0])):
    b.append(input("比率"))
for j in range(int(a[1])):
    c.append(input("成績").split(" "))
for y in range(int(a[1])): 
    for x in range(int(a[0])):
        d=d+float(c[y][x])*float(b[x])
e=d/int(a[1])
e1=round(e,2)
print("全班的總平均{:.2f}".format(e1))