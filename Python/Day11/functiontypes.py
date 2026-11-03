#No parameters, no return value

def armstrong():
    num = int(input("Enter number: "))#153 #123
    temp = num
    s=0
    p = len(str(num))
    while num>0:
        r = num % 10
        s = s + (r ** p)
        num=num//10
    
    if temp == s:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

armstrong()#Armstrong number
armstrong()#Not an Armstrong number

#With parameters, without return

def armstrong(num):
    temp = num
    s=0
    p = len(str(num))
    while num>0:
        r = num % 10
        s = s + (r ** p)
        num=num//10
    
    if temp == s:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")


armstrong(153)#Armstrong number
armstrong(1634)#Armstrong number
armstrong(123)# Not an Armstrong number

#Without parameters, with return
def armstrong():
    num=int(input("Enter a number:"))
    temp = num
    s=0
    p = len(str(num))
    while num>0:
        r = num % 10
        s = s + (r ** p)
        num=num//10
    
    if temp == s:
        return "Armstrong number"
    else:
        return "Not an Armstrong number"


print(armstrong())

#With parameters, with return
def armstrong(num):
    temp = num
    s=0
    p = len(str(num))
    while num>0:
        r = num % 10
        s = s + (r ** p)
        num=num//10
    
    if temp == s:
        return "Armstrong number"
    else:
        return "Not an Armstrong number"

num=int(input("Enter a number:"))
print(armstrong(num))







