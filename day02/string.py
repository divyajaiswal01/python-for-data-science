#string
name = "divya"
print(name)
print(name[0])
print(name[1])
print(name[-1])
print(name[0:3])
print(name[0 :])


#take a name as input and print first and last character of the name
name = input("Enter your name : ")
print(f"first character of your name is : {name[0]}")
print(f"last character of your name is : {name[-1]}")
print(f"length of your name is : {len(name)}")

#take a name as input and print the name in reverse order
name = input("Enter your name : ")
print(f"your name in reverse order is : {name[::-1]}")


#swap case of a string
name = input("Enter a string : ")
print(f"original string : {name}")
print(f"string in swap case : {name.swapcase()}")


step slicing
string[start:end:step]
Step means
How many positions to move each time.

name = "divya"
step_slicing = name[0:5:2]
print(f"step slicing result : {step_slicing}")

#omit start in slicing
name = "divya"
start_omit = name[:2]
print(f"slicing with omitted start index : {start_omit}")

#omit end in slicing
name = "divya"
end_slicing = name[2:]
print(f"slicing end index omitting : {end_slicing}")

#omiting both start and end in slicing
name = "divya"
print(name[:])

#negative slicing
name = "divya"
negative_slicing = name[-2:]
print(f"negative slicing : {negative_slicing}")

#reverse string
name = "divya"
reverse_string = name[::-1]
print(f"reverse string : {reverse_string}")

#practice question 
#take a first 3 letter and letter from last name 
first_name = "divya"
last_name = "jaiswal"
print(f"first three letter of first name : {first_name[0:3]} ")
print(f"last three letter of lastname : {last_name[-3:]}")


