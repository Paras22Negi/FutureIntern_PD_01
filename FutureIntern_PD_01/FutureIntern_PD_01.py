def calculator():
    print("welcome to the calculator")
    print("1.addition:")
    print("2.subtraction:")
    print("3.multiplication:")
    print("4.division")

    a=int(input("choose the action (1/2/3/4):"))
    num1=float(input("enter first number:"))
    num2=float(input("enter second number:"))
    def add():
        b=float(num1+num2)
        print(str(num1)+"+"+str(num2)+"="+str(b))
    def sub():
        b=float(num1-num2)
        print(str(num1)+"-"+str(num2)+"="+str(b))
    def multiply():
        b=float(num1*num2)
        print(str(num1)+"*"+str(num2)+"="+str(b))
    def devide():
        if num2==0:
            print("'not defined'second number can't be 0")
        else:
            b = float(num1 / num2)
            print(str(num1) + "/" + str(num2) + "=" + str(b))
    if a==1:
        add()
    elif a==2:
        sub()
    elif a==3:
        multiply()
    elif a==4:
        devide()
    else:
        print("invalid choice")
x=input("do you want to use calculator(Y/N): ")
if x.lower()=="y":
    while True:
        calculator()
        x=input("do you want to use calculator again(Y/N)")
        if x.lower()=="y":
            continue
        else:
            break
print ("calculator exited")