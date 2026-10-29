#list

even=[2,4,6,8,10]
print(even)

even.append(12)
print(even)

even.insert(0,0)
print(even)

even.remove(12)
even.pop(0)
print(even)

odd=[]
for i in range(1,11,2):
    odd.append(i)
print(odd)


#tuples

names=("Mohan","Majid","Vishwa","Chetan","Gopi","Dhaya")
print(names)

city=()
for i in range(5):
    c=input("enter the city:")
    city = city + (c,)
print(city)

#set

numbers = {10, 20, 30, 40}
print(numbers)
print(len(numbers))


num=set()
for i in range(5):
    n=int(input("enter a number:"))
    num.add(n)
print(num)


