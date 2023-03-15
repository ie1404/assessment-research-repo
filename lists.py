# #lists, arrays
# #empty list
# fruits=[];
# fruits=["apple","pineapple","banana","lemon"]
# #display list
# print(fruits);

# #add items
# fruits.append("orange")
# fruits.append("Pear")
# fruits.append("Appricot")

# print(fruits);

# #delete the element
# fruits.pop(1)
# print(fruits);

# generate random numbers
import random
numbers=[]
for i in range(100):
    numbers.append(random.randint(0,1000))

print(numbers)

# for n in numbers:
#     if n>500:
#         print(n)
    
    
max_number=0
for n in numbers:
    if n>max_number:
        max_number=n

print("max number = ",max_number)


# min_number=0
# for n in numbers:
#     if n<min_number:
#         min_number=n
min_number=min(numbers)
print("min number = ",min_number)