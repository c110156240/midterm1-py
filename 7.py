a=input("輸入")
b=a.split(",")
if b[0]=="186":
    c=int(b[1])*0.09
    d=c/186
    if d>1:
        c=c*0.8
        print("通話費%.2f"%(c))
    else:
        c=c*0.9
        print("通話費%.2f"%(c)) 
elif b[0]=="386":
    c=int(b[1])*0.08
    d=c/386
    if d>1:
        c=c*0.7
        print("通話費%.2f"%(c))
    else:
        c=c*0.8
        print("通話費%.2f"%(c)) 
elif b[0]=="586":
    c=int(b[1])*0.07
    d=c/386
    if d>1:
        c=c*0.6
        print("通話費%.2f"%(c))
    else:
        c=c*0.7
        print("通話費%.2f"%(c)) 
else:
    c=int(b[1])*0.06
    d=c/786
    if d>1:
        c=c*0.5
        print("通話費%.2f"%(c))
    else:
        c=c*0.6
        print("通話費%.2f"%(c))     



    
              