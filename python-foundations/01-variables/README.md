# Phase 1 — Topic #1: Variables
## 1. Concept Explanation
### What is a Variable?
A variable is a named container used to store data in memory.

Think of it like a labeled box.

#### Example:
> name = "Avinash"

#### Here:
    - Variable Name → name
    - Value → "Avinash"

Python stores the value and lets us access it using the variable name.

## Why Variables Are Important

#### Without variables:
    print("Avinash")
    print("Avinash")
    print("Avinash")

If the name changes, you must update it everywhere.

#### With variables:
    name = "Avinash"

    print(name)
    print(name)
    print(name)

#### Change once:
    
    name = "John"

Everything updates automatically.

## Real World Analogy

#### Imagine a bank locker.

#### Locker Number:
    
    ABG101

### Contents
    Rs. 50,000

### Variable:
    balance = 50,000

Locker Number -> Variable Name

Money -> Value

## Industry Use Case
Backend APIs constantly store data in variables

#### Example:

    user_name = "Avinash"
    email = "avinash@gmail.com"
    age = 25

These values later come from:

- Database
- User Input
- API Request
- Authentication System

Variables are literally everywhere.

## 3. Type Hints
Even for variables we use type hints.

### Integer
    age: int = 25

### Float
    salary: float = 35000.00

### String
    name: str = "Best time ever"

### Boolean
    is_active: bool = True

## Basic Examples
    
    name: str = "Name"

    print(name)

## Intermediate Example

    name: str = "Name"
    age: int = 38
    salary: float = 35000.00

    print(name)
    print(age)
    print(salary)

## Real World Example

    user_id: int = 101
    username: str = "Username"
    is_verified: bool = True

    print(user_id)
    print(username)
    print(is_verified)
