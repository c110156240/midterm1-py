a=input("請輸入第一組數字")
b=input("請輸入第2組數字")
a1=0
b1=0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]==b[j]:
            if i==j:
                a1+=1
                break
            else:
                b1+=1
                break
if a1==4:
    print("4A0B 全對")
else:
    print("%dA%dB加油"%(a1,b1))
            










