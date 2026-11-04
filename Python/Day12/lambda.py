#odd or even logic using lambda function

odd_even = lambda n: "Even" if n % 2 == 0 else "Odd"
n=int(input("Enter a number"))
print(odd_even(n)) 

#Sum of digits using a recursive function

def sod(n):
    if n==0:
        return 0
    else:
        result = (n % 10) + sod(n // 10)
        return result
    
n=int(input("Enter a number:"))   
result=sod(n)
print(result)
