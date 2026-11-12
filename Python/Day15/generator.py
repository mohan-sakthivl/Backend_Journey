#Generate the multiplication table

def table(num):
    for i in range(1,11):
        yield num*i



num=int(input("Enter a number:"))
result=table(num)

for i in range(1, 11):
    print(num , "x" , i ,"=",next(result))

