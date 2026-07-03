'''
## 📋 Day 3 — Assignment

`day3.py` file banao `python-foundations/` folder mein.

**Scenario:** Tum ek DE ho aur tumhe ek **employee salary processing pipeline** banani hai.

python
# Ye variables use karo
'''
employee_id = "EMP-001"
employee_name = "Avinash"
base_salary = 45000
performance_score = 85        # 0 to 100
years_of_experience = 3
department = "Engineering"
is_on_probation = False


'''
**Tasks:**

1. **Bonus calculate karo** using if-elif-else:
   - performance_score >= 90 → bonus = 20% of base_salary
   - performance_score >= 75 → bonus = 15% of base_salary
   - performance_score >= 60 → bonus = 10% of base_salary
   - Below 60 → bonus = 0
'''
if performance_score >= 90:
    bonus = (base_salary*20)/100
elif performance_score >= 75:
    bonus = (base_salary*15)/100
elif performance_score >= 60:
    bonus = (base_salary*10)/100
else:
    bonus = 0


'''
2. **Experience level** assign karo:
   - 0-1 years → "Junior"
   - 2-4 years → "Mid-Level"
   - 5-9 years → "Senior"
   - 10+ years → "Lead"
'''
if years_of_experience < 2:
    level = "Junior"
elif years_of_experience < 5:
    level = "Mid-Level"
elif years_of_experience < 10:
    level = "Senior"
else:
    level = "Lead"

'''
3. **Salary processing check** karo:
   - Agar probation par hai → "Salary on Hold"
   - Warna → "Cleared for Payment"
'''
if is_on_probation:
    salary_processing = "Salary on Hold"
else:
    salary_processing = "Cleared for Payment"


'''
4. **Total payout** calculate karo:
   - total_payout = base_salary + bonus (sirf agar probation nahi hai)
   - Probation par hai to total_payout = 0

'''
if is_on_probation:
    total_payout = 0
else:
    total_payout = base_salary + bonus


'''
5. **Ek line mein** (ternary) — tax_bracket:
   - total_payout > 50000 → "High Tax Bracket"
   - warna → "Standard Tax Bracket"
'''
tax_bracket = "High Tax Bracket" if total_payout > 50000 else "Standard Tax Bracket"


'''
6. Sab print karo clean summary mein
'''
print(f"--- Employee Salary Report ---")
print(f"Employee ID      : {employee_id}")
print(f"Name             : {employee_name}")
print(f"Department       : {department}")
print(f"Base Salary      : ₹{base_salary}")
print(f"Performance      : {performance_score}/100")
print(f"Bonus            : ₹{bonus}")
print(f"Experience Level : {level}")
print(f"Salary Status    : {salary_processing}")
print(f"Total Payout     : ₹{total_payout}")
print(f"Tax Bracket      : {tax_bracket}")
