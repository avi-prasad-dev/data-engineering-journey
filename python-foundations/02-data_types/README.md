# Topic #2: Data Types
## What is a Data Type?

A data type tells Python what kind of data a value represents.

Example:
    age: int = 38
    name: str = "Avinash"
    salary: float = 50000.50
    is_employed: bool = True

### Python needs to know:

- Is this a number?
- Is this text?
- Is this True/False?

That's the purpose of data types.

## Why Are Data Types Important?
Imagine a bank application.
    
    account_balance = 50000

Balance should be a number.
But if someone stores:

    account_balance = "fifty thousand"

Mathematical calculations become impossible.

Data types help Python handle data correctly.


## Real-World Analogy

Think of a warehouse.

Different boxes contain different things:

📦 Electronics

📦 Clothes

📦 Food

The warehouse staff must know what's inside each box.

Similarly, Python must know what type of data it's handling.

## Industry Use Case

Backend applications constantly use data types.

User API response:

    user_id: int = 101
    user_name: str = "Avinash"
    salary: float = 45000.75
    is_active: bool = True

Databases, APIs, and business logic all depend on correct data types.

## Major Python Data Types

Integer (int)

Whole numbers.
    
    age: int = 38
    marks: int = 90
    year: int = 2026
    temperature: int = -5

Float (float)

Numbers with decimal points.

    salary: float = 45000.50

### Examples:

    pi: float = 3.14
    height: float = 5.9

String (str)

Text data.

    name: str = "Avinash"

### Examples:

    city: str = "Lucknow"
    course: str = "Python"

## Boolean (bool)

Only two values:
    True
    False

### Examples:

    is_logged_in: bool = True
    is_admin: bool = False

## Using type()

Python provides a function called type().

It tells us the data type of a value.

### Example:
    age: int = 38

    print(type(age))

### Output:

    <class 'int'>


### Basic Example

    name: str = "Avinash"
    age: int = 38
    salary: float = 45000.50
    is_employed: bool = True

    print(name)
    print(age)
    print(salary)
    print(is_employed)

### Intermediate Example

    employee_name: str = "Avinash"
    experience_years: int = 5
    monthly_salary: float = 35000.75
    is_active: bool = True

    print(type(employee_name))
    print(type(experience_years))
    print(type(monthly_salary))
    print(type(is_active))