a=int(input("輸入x"))
b=int(input("輸入y"))
if a>0 and b>0:
    c=a*a+b*b
    print("該點位於第一象限，離原點距離為根號"+str(c))
elif  a<0 and b>0:
    c=a*a+b*b
    print("該點位於第二象限，離原點距離為根號"+str(c))
elif  a<0 and b<0:
    c=a*a+b*b
    print("該點位於第三象限，離原點距離為根號"+str(c)) 
elif  a>0 and b<0:
    c=a*a+b*b
    print("該點位於第四象限，離原點距離為根號"+str(c)) 










