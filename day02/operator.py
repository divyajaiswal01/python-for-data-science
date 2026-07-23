#arithmatic operators
a = 10
b = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# calculator using user input 
num1 = int(input("Enter first value : "))
num2 = int(input("Enter second value : "))
sum = num1 + num2
print(f"sum of num1 and num2 {sum}")
sub = num1 - num2
print(f"sub of num1 and num2 {sub}")
mul = num1 * num2   
print(f"mul of num1 and num2 {mul}")
div = num1 / num2
print(f"div of num1 and num2 {div}")
floor_div = num1 // num2
print(f"floor_div of num1 and num2 {floor_div}")


#camparison operators
x = 10
y = 20
print(x == y)
print(x != y)
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)

#take a number from user and check which number is greater
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if(num1 > num2):
    print(f"num1 is grater than num2")
elif(num1 < num2):
    print(f"num2 is grater than num1")
else:
    print(f"num1 and num2 are equal")


#crhck if personm is eligible for voting or not
age = int(input("enter your age : "))
if(age >= 18):
    print(f"you are eligible for voting")
else:
    print(f"you are not eligible for voting")


#logical operators
x = True
y = False
print(x and y)
print(x or y)
print(not x)

a = 10
b = 20
print(a > 5 and b > 15)
print(a > 5 or b < 15)
print(a !=10)

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
if(a > 0 and b > 0):
    print(f"both numbers are positive")
elif(a < 0 and b < 0):
    print(f"both numbers are negative")
else:
    print(f"numbers have different signs")

#assignment operators
x = 10
x += 5  # x = x + 5
print(x)
x -= 3  # x = x - 3
print(x)
x *= 2  # x = x * 2
print(x)
x /= 2  # x = x / 2
print(x)


#identity operators
a = 10
b = 10
print(a is b)
print(a is not b)
print(a == b)
print(a != b)
print(a is 10)


#membership operators
list = [1, 2, 3, 4, 5]
print(3 in list)
print(6 not in list)

fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)
print("mango" not in fruits)

name = "divya"
print("d" in name)
