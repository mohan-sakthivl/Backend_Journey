num=int(input("Enter the number:"))
temp=num
x=0

while(num>0):
    a=num%10
    x=x*10+a
    num=num//10
if temp == x:
    print("Palindrome")
else:
    print("Not a Palindrome")
