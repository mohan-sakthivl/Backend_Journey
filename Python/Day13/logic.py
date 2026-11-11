
#Armstrong number till 1000
for num in range(1,1001):
    temp=num
    s=0

    while(temp>0):
        r=temp%10
        s=r**3 + s
        temp=temp // 10

    if(num==s):
        print(num,"It is an Armstrong number")



#palindrome 1 to 1000
for num in range(1,1001):
    s=0
    temp=num

    while(temp>0):
        r=temp%10
        s=s*10 + r
        temp=temp//10

    if(s==num):
        print(s,"It is a palindrome")
