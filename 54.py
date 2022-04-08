a=float(input("請輸入路程公里數"))
if a<=1.5:
    a1=75
else:
    b=a-1.5
    if b%0.25==0:
        a1=75+(b/0.25*5)
    else:
        a1=75+((int(b/0.25)+1)*5)
print("所需車資為{:.0f}".format(a1))