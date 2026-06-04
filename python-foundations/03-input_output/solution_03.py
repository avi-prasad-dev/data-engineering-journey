'''
## Create a program that asks the user for:

    Name
    Age
    City

## Then print:
    Hello Avinash
    You are 38 years old.
    You live in Bangalore.
'''

name: str = str(input("Enter Your name: "))
age: int = int(input("Enter your Age: "))
city: str = str(input("Enter your city: "))

print(f"Hello {name}")
print(f"You are {age} years old")
print(f"You live in {city}")