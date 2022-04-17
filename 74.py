b=["red","blue","red","green"]
c=0

for i in range(10):
    a=input("color").split(" ")
    c=c+1
    e=str()
    for j in range(4):
        if a[j] in b:
            if a[j]==b[j]:
                e=e+str(1)
            else:
                e=e+str(2)
        else:
            e=e+str(3)
    if e=="1111":
        print("正確答案")
        break
    else:
        print(e)
if c==10:
    print("挑戰失敗")