# Day 3 — Python Conditionals (if, elif, else)
# Data Engineering Journey — Avinash
# Date: 3 July

---

## 📌 1. Conditionals kya hote hain?

**Simple words mein:**
Conditionals se hum program ko "decision" lene dete hain.
"Agar ye condition sahi hai — to ye karo, warna wo karo."

**DE mein kyun zaroori hai:**
Pipeline mein data aata hai — har row par decision lena hota hai:
- Agar amount > 1000 → premium category
- Agar status == "failed" → error log mein daalo
- Agar stock < 10 → alert bhejo

Ye sab conditionals se hota hai.

---

## 📌 2. if — Basic Syntax

```python
if condition:
    # ye tab chalega jab condition True ho
    code_here
```

**Important:** Indentation (4 spaces ya 1 tab) zaroori hai — Python isi se samajhta hai ki kaunsa code if ke andar hai.

```python
order_amount = 1500

if order_amount > 1000:
    print("Premium order hai")   # ye chalega
```

---

## 📌 3. if-else

```python
if condition:
    # condition True ho to
else:
    # condition False ho to
```

```python
order_amount = 400

if order_amount > 1000:
    print("Premium order")
else:
    print("Regular order")    # ye chalega — 400 > 1000 False hai
```

---

## 📌 4. if-elif-else (Multiple conditions)

```python
if condition1:
    # condition1 True
elif condition2:
    # condition1 False, condition2 True
elif condition3:
    # condition1, 2 False, condition3 True
else:
    # sab False
```

### DE mein use — Order categorization:
```python
order_amount = 750

if order_amount >= 2000:
    category = "Platinum"
elif order_amount >= 1000:
    category = "Gold"
elif order_amount >= 500:
    category = "Silver"
else:
    category = "Regular"

print(f"Order Category: {category}")    # Silver
```

---

## 📌 5. Nested if (if ke andar if)

```python
is_verified = True
order_amount = 1500

if is_verified:
    if order_amount > 1000:
        print("Verified Premium Order")
    else:
        print("Verified Regular Order")
else:
    print("Unverified — Order on hold")
```

**Tip:** Zyada nested if se bachne ki koshish karo — code complex ho jaata hai. Logical operators (and, or) use karo jab ho sake.

```python
# Nested ki jagah — logical operator
if is_verified and order_amount > 1000:
    print("Verified Premium Order")
```

---

## 📌 6. Ternary Operator (One-liner if-else)

```python
# Normal if-else
if order_amount > 1000:
    label = "Premium"
else:
    label = "Regular"

# Same cheez — ek line mein
label = "Premium" if order_amount > 1000 else "Regular"

print(label)
```

DE mein ye bahut use hota hai — especially jab kisi column ki value set karni ho.

---

## 📌 7. Real DE Example — Data Validation Pipeline

```python
# Maan lo CSV se ek order row aaya
raw_data = {
    "order_id": "ORD-2024-001",
    "amount": 2500.00,
    "status": "delivered",
    "customer_type": "premium",
    "stock_remaining": 3
}

order_id = raw_data["order_id"]
amount = raw_data["amount"]
status = raw_data["status"]
customer_type = raw_data["customer_type"]
stock_remaining = raw_data["stock_remaining"]

# Validation 1 — Amount valid hai?
if amount <= 0:
    print(f"❌ ERROR: Invalid amount for {order_id}")

# Validation 2 — Order categorization
if amount >= 2000:
    order_tier = "Platinum"
elif amount >= 1000:
    order_tier = "Gold"
elif amount >= 500:
    order_tier = "Silver"
else:
    order_tier = "Regular"

# Validation 3 — Status check
if status == "delivered":
    is_complete = True
elif status == "processing":
    is_complete = False
else:
    is_complete = False
    print(f"⚠️ WARNING: Unknown status '{status}' for {order_id}")

# Validation 4 — Stock alert
if stock_remaining < 5:
    alert = "🚨 CRITICAL: Restock immediately"
elif stock_remaining < 10:
    alert = "⚠️ WARNING: Low stock"
else:
    alert = "✅ Stock OK"

# Ternary — customer priority
priority = "HIGH" if customer_type == "premium" else "NORMAL"

# Final Summary
print(f"\n--- Pipeline Report: {order_id} ---")
print(f"Amount       : ₹{amount}")
print(f"Order Tier   : {order_tier}")
print(f"Completed    : {is_complete}")
print(f"Stock Alert  : {alert}")
print(f"Priority     : {priority}")
```

---

## ⚠️ Common Mistakes

| Mistake | Galat | Sahi |
|---|---|---|
| Colon bhool gaye | `if x > 5` | `if x > 5:` |
| Indentation galat | Space inconsistent | Hamesha 4 spaces |
| = vs == | `if x = 5:` ❌ | `if x == 5:` ✅ |
| String comparison | `if status == delivered:` | `if status == "delivered":` |
| elif order | Wrong order | Pehle specific, phir broad |

---



`day3.py` file banao `python-foundations/` folder mein.

**Scenario:** Tum ek DE ho aur tumhe ek **employee salary processing pipeline** banani hai.

```python
# Ye variables use karo
employee_id = "EMP-001"
employee_name = "Avinash"
base_salary = 45000
performance_score = 85        # 0 to 100
years_of_experience = 3
department = "Engineering"
is_on_probation = False
```

**Tasks:**

1. **Bonus calculate karo** using if-elif-else:
   - performance_score >= 90 → bonus = 20% of base_salary
   - performance_score >= 75 → bonus = 15% of base_salary
   - performance_score >= 60 → bonus = 10% of base_salary
   - Below 60 → bonus = 0

2. **Experience level** assign karo:
   - 0-1 years → "Junior"
   - 2-4 years → "Mid-Level"
   - 5-9 years → "Senior"
   - 10+ years → "Lead"

3. **Salary processing check** karo:
   - Agar probation par hai → "Salary on Hold"
   - Warna → "Cleared for Payment"

4. **Total payout** calculate karo:
   - total_payout = base_salary + bonus (sirf agar probation nahi hai)
   - Probation par hai to total_payout = 0

5. **Ek line mein** (ternary) — tax_bracket:
   - total_payout > 50000 → "High Tax Bracket"
   - warna → "Standard Tax Bracket"

6. Sab print karo clean summary mein

**GitHub Push:**
```bash
git add .
git commit -m "Day 3: Conditionals - if, elif, else, nested, ternary"
git push origin main
```

Code + GitHub link yahan paste karo — tab Day 4 shuru hoga. 💪

---

*Notes by: DE Mentor | Day 3 of 112 | Roadmap: July–October*
