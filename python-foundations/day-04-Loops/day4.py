## 📋 Day 4 — Assignment
'''
`day4.py` file banao `python-foundations/` folder mein.

**Scenario:** Tum ek DE ho. Tumhare paas ek company ke **5 employees ka data** hai. Tumhe ek **payroll processing pipeline** banani hai.
'''

employees = [
    {"emp_id": "EMP-001", "name": "Avinash",  "salary": 45000, "attendance": 26, "department": "Engineering"},
    {"emp_id": "EMP-002", "name": "Rahul",    "salary": 38000, "attendance": 20, "department": "Sales"},
    {"emp_id": "EMP-003", "name": "Priya",    "salary": 52000, "attendance": 28, "department": "Engineering"},
    {"emp_id": "EMP-004", "name": "Amit",     "salary": 31000, "attendance": 15, "department": "HR"},
    {"emp_id": "EMP-005", "name": "Sneha",    "salary": 67000, "attendance": 30, "department": "Management"},
]

total_payroll = 0
engineering_count = 0
skipped_employees = []


# **Tasks:**
# '''
# 1. Har employee ke liye loop chalao aur ye calculate karo:
#    - `working_days = 30` (total working days)
#    - `per_day_salary = salary / working_days`
#    - `actual_salary = per_day_salary * attendance`

for employee in employees:
    emp_id = employee["emp_id"]
    name = employee["name"]
    salary = employee["salary"]
    attendance = employee["attendance"]
    department = employee["department"]

    working_days = 30
    per_day_salary = salary / working_days
    actual_salary = per_day_salary * attendance


# 2. Attendance check karo:
#    - attendance < 20 → `status = "WARNING"` — skip this employee (continue use karo)
#    - warna → `status = "OK"`

    if attendance < 20:
        status = "WARNING"
        skipped_employees.append(name)
        continue
    else:
        status = "OK"

# 3. Department bonus add karo:
#    - "Engineering" → 10% of actual_salary
#    - "Management" → 15% of actual_salary
#    - Baaki → 5% of actual_salary

    if department == "Engineering":
        dept_bonus = (actual_salary * 10)/100
    elif department == "Management":
        dept_bonus = (actual_salary * 15)/100
    else:
        dept_bonus = (actual_salary * 5)/100

# 4. `total_payout = actual_salary + dept_bonus`

    total_payout = actual_salary + dept_bonus

# 5. Ye counters track karo:
#    - `total_payroll = 0` — sab employees ka total payout
#    - `engineering_count = 0` — Engineering department mein kitne
#    - `skipped_employees = []` — WARNING wale employees ki list
    total_payroll += total_payout
    if department == "Engineering":
        engineering_count += 1

    


# Task 6 — Employee summary
    print(f"Employee ID         : {emp_id}")
    print(f"Name                : {name}")
    print(f"Department          : {department}")
    print(f"Attendance          : {attendance}/30")
    print(f"Status              : {status}")
    print(f"Actual Salary       : ₹{actual_salary:.2f}")
    print(f"Department Bonus    : ₹{dept_bonus:.2f}")
    print(f"Total Payout        : ₹{total_payout:.2f}")
    print("-" * 40)

# Task 7 — Pipeline report
print(f"\n--- Pipeline Report ---")
print(f"Total Payroll        : ₹{total_payroll:.2f}")
print(f"Engineering Headcount: {engineering_count}")
print(f"Skipped Employees    : {skipped_employees}")