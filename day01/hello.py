#EASY
#print "Hello, World!"

print("Hello, World!")


#print "your age"
age = input(int("Enter your age: "))
print(f"Your age is: {age}")

#store city name in variable and print it
city = "mumbai"
print(f"City name is: {city}")

#print your favorite programming language
favorite_language = "Python"
print(f"My favorite programming language is: {favorite_language}")      

#print three variable in one statement
name = "Alice"
age = 21
city = "New York"
print(f"My name is {name}, I am {age} years old, and I love {favorite_language} and I live in {city}.")

#BEGINEER
#take your name as input and print it
name = input("Enter your name: ")
print(f"Hello, {name}!")

#take your age as input and print it
age = input(int("enter your age : "))
print(f"ENTER YOUR AGE :{age}")

#take your city as input and print it
city = input("enter your city : ")
print(f"ENTER YOUR CITY :{city}")

#print all detail using f string
print(f"My name is {name}, I am {age} years old, and I live in {city}.")

#swap two numbers using a temporary variable
a = 5
b = 10
temp = a 
a = b
b = temp
print(f"After swapping: a = {a}, b = {b}")  

#INTERMEDIATE
#add two number
num1 = 10 
num2 = 10
print(f"sum of {num1} and {num2} is : {num1 +num2}")

#add two number using input
num1 = int(input("Enter first number: "))   
num2 = int(input("Enter second number: "))
sum = num1 + num2
print(f"sum of {num1} and {num2} is : {sum}")

#average of three number
num1 = 10
num2 = 20
num3 = 30
avg = (num1 + num2 + num3) / 3
print(f"average of three number : {avg}")

num1 = int(input("enter your first number : "))
num2 = int(input("enter your second number : "))
num3 = int(input("enter your third number : "))
avg = (num1 + num2 + num3) / 3
print(f"average of three number : {avg}")

#convert temperature from celsius to fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")   

#convert kilometers to meters
kilometers = float(input("Enter distance in kilometers: "))
meters = kilometers * 1000
print(f"Distance in meters: {meters}")  


#convert minutes to hour
minutes = float(input("Enter time in minutes: "))
hours = minutes / 60
print(f"Time in hours: {hours}")
