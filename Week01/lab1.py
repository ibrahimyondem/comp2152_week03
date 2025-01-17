# Sample Coding Questions 01 Week 01
# Ibrahim Yondem

#Defining variables
arr = [1,4,7,9]

#Order of precedence
a = 1
b = 2
c = 3
d = 4

e =(a - (b ** c) //d) + (a % c)
print(e) # prints 0

#Formatting
temperature = 32.6
print(f"The temperature today is {temperature:.3f} degrees celsius")

##Common Functions
userAge = int(input("Please enter your age:"))
userAge += 22
print("Now showing the shop items filtered by age: " + str(userAge))