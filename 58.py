b=[]
for i in range(10):
    b.append(int(input("輸入")))
b.sort()
print("最大的3個數字%d,%d,%d"%(b[-1],b[-2],b[-3]))
print("最小的3個數字%d,%d,%d"%(b[0],b[1],b[2]))