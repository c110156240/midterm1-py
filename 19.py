a=int(input("測試資料量"))
b=[]
for i in range(a):
    b.append(input("資料").split(" "))
    if b[i][0]=='O':
        if b[i][1]=='O':
            if b[i][2]=='O':
                print("yes")
            else:
                print("impossible")
        elif b[i][1]=='A':
            if b[i][2]=='O' or b[i][2]=='A':
                print("yes")
            else:
                print("impossible")
        elif b[i][1]=="B":
            if b[i][2]=="O" or b[i][2]=="B":
                print("yes")
            else:
                print("impossible")
        else:
            if b[i][2]=="O" or b[i][2]=="AB":
                print("yes")
            else:
                print("impossible")
    elif b[i][0]=="A":
        if b[i][1]=="A":
            if b[i][2]=="A" or b[i][2]=="O":
                print("yes")
            else:
                print("impossible")
        elif b[i][1]=="B":
            print("yes")
        else:
            if b[i][2]=="O":
                print("impossible")
            else:
                print("yes")
    elif b[i][0]=="B":
        if b[i][1]=="B":
            if b[i][2]=="B" or b[i][2]=="O":
                print("yes")
            else:
                print("impossible")
        else:
            if b[i][2]=="O":
                print("impossible")
            else:
                print("yes")   
    elif b[i][0]=="AB":
        if b[i][2]=="O":
            print("impossible")
        else:
            print("yes")                                                        