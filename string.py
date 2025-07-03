#Strings

message = """Bob's World
is cool"""

print(message)

message = ' Hello '

print(message[0])
print(message[1])

print(message[-1])

print(len(message))

message = 'Hello World'

print(message.strip()) # Remove leading and trailing whitespace
print(message.lower()) # Convert all charcters to lowercase
print(message.split(',')) # split the string into a list based on the comma

print(message.upper()) # Convert all charcters to uppercase

#numeric Data

num = 3

print(type(num))

num2 = 3.14

print(type(num2))

#variables

my_variable = 10
total_count = 0
user = 'John'
sencond_variable = 10 



#operaters 

#Addition(+)
#Subtraction(-)
#Multiplication(*)
#Division (/)
# Modulus (%)
#Exponent (**)

x = 10
y = 2

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(5%2)
print(x**y)

x = 10
x -= 2
print(x)

#Operators with Strings 

str1 = 'Hello'
str2 = 'World'

print(str1 + " " + str2 + " " + str2)
print (str1 * 3)

#Control Statements 

num = 0

if num > 0:
    print("This number is positive")
elif num == 0:
    print("This number is zero")
    
else:
    print("This number is negative")
    
    #Control Statement
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
    
if num1 > num2: 
    print(num1, "is greater than" , num2)
elif num2 > num1:
    print(num2, "is greater than" , num1)
else:
    print("Both numbers are equal")
    
#Loops
    
fruits = ["apple", "banana", "strawberry"]

for fruit in fruits:
    print(fruit)
    
numbers = [1, 2, 3, 5]
    
for number in numbers:
    print(number)