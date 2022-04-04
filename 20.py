a=int(input("組數為"))
b=[]
c=[]
for i in range(a):
    b.append(input("第i組").split(" "))
    c.append(int(b[i][0])*250+int(b[i][1])*175)
for j in range(a):
    print("第%s組應收費用%d"%(j+1,c[j]))