a=input("請選擇主餐及升級的套餐")
b=input("是否升級成大杯飲料")
c=input("是否換成大薯")
d=0
if a[0]=="1":
    if a[1]=="A":
        d=72+55
    else:
        d=72+68
elif a[0]=="2":
    if a[1]=="A":
        d=62+55
    else:
        d=62+68    
elif a[0]=="3":
    if a[1]=="A":
        d=82+55
    else:
        d=82+68  
elif a[0]=="4":
    if a[1]=="A":
        d=44+55
    else:
        d=44+68  
else:
    if a[1]=="A":
        d=60+55
    else:
        d=60+68      
if b=="是":
    d=d+7

if c=="是":
    d=d+13
print("總共為%d元"%(d))