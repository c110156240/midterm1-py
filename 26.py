o=0
while o!=1:
    a=input("檢測的字串(end結束)")
    if  a == "end":
        o=1
    if a != "end":
        b=input("檢測的字元")
        c=0
        for i in range(len(a)):
            if b==a[i]:
                c=c+1
        print("字元%s出現次數%d"%(b,c))

print("檢測結束")