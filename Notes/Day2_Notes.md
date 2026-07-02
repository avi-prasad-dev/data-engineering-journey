# Day 2 — Python Operators
# Data Engineering Journey — Avinash
# Date: 2 July

---

## 📌 1. Operators kya hote hain?

**Simple words mein:**
Operators wo symbols hain jo data par operations perform karte hain — jaise math mein +, -, × hota hai.

**DE mein kyun zaroori hai:**
Pipeline mein decisions lene hote hain — "agar amount 500 se zyada hai to premium category mein daalo" — ye sab operators se hota hai.

---

## 📌 2. Arithmetic Operators (Math wale)

```python
a = 100
b = 30

print(a + b)    # 130  → Addition
print(a - b)    # 70   → Subtraction
print(a * b)    # 3000 → Multiplication
print(a / b)    # 3.33 → Division (hamesha float deta hai)
print(a // b)   # 3    → Floor Division (sirf poora number)
print(a % b)    # 10   → Modulus (remainder / baki)
print(a ** 2)   # 10000 → Power (a ka square)
```

### DE mein use:
```python
total_sales = 150000
num_orders = 320

# Average order value nikalna
avg_order_value = total_sales / num_orders
print(f"Average Order Value: ₹{avg_order_value:.2f}")  # :.2f = 2 decimal places

# Ye check karna ki orders even hain ya odd
print(num_orders % 2)   # 0 = even, 1 = odd

# Percentage nikalna
target = 200000
achievement = (total_sales / target) * 100
print(f"Target Achievement: {achievement:.1f}%")
```

---

## 📌 3. Comparison Operators (Compare karne ke liye)

Ye hamesha **True ya False** return karte hain.

```python
a = 100
b = 30

print(a == b)    # False → Equal to
print(a != b)    # True  → Not equal to
print(a > b)     # True  → Greater than
print(a < b)     # False → Less than
print(a >= 100)  # True  → Greater than or equal to
print(a <= 99)   # False → Less than or equal to
```

### DE mein use:
```python
order_amount = 750
threshold = 500

print(order_amount > threshold)     # True — premium order hai
print(order_amount == threshold)    # False — exactly 500 nahi hai
print(order_amount >= threshold)    # True — 500 ya usse zyada
```

---

## 📌 4. Logical Operators (Multiple conditions ek saath)

```python
# and — dono conditions True honi chahiye
print(True and True)    # True
print(True and False)   # False

# or — koi ek condition True ho
print(True or False)    # True
print(False or False)   # False

# not — ulta kar deta hai
print(not True)         # False
print(not False)        # True
```

### DE mein use:
```python
order_amount = 750
is_premium_customer = True
is_delivered = False

# AND — dono conditions check karo
print(order_amount > 500 and is_premium_customer)   # True

# OR — koi ek condition
print(order_amount > 1000 or is_premium_customer)   # True

# NOT — ulta
print(not is_delivered)    # True — matlab abhi deliver nahi hua
```

---

## 📌 5. Assignment Operators (Shortcut operators)

```python
count = 0

count += 1      # count = count + 1  →  1
count += 1      # count = count + 1  →  2
count -= 1      # count = count - 1  →  1
count *= 3      # count = count * 3  →  3
count /= 3      # count = count / 3  →  1.0
count //= 1     # count = count // 1 →  1

print(count)
```

### DE mein use:
```python
total_amount = 0

# Multiple orders process karte waqt amount add karte rehte hain
total_amount += 450.00
total_amount += 1200.50
total_amount += 89.99

print(f"Total: ₹{total_amount}")    # ₹1740.49
```

---

## 📌 6. Real DE Example — Sab ek saath

```python
# E-commerce order processing scenario
order_id = "ORD-001"
order_amount = 1250.00
customer_type = "premium"
is_verified = True
items_count = 5
discount_percent = 10

# Arithmetic
discount_amount = (order_amount * discount_percent) / 100
final_amount = order_amount - discount_amount

# Comparison
is_large_order = order_amount > 1000
is_eligible_for_free_shipping = order_amount >= 500

# Logical
is_priority_order = is_large_order and is_verified

# Assignment operator
total_processed = 0
total_processed += final_amount

# Summary
print(f"--- Order Summary: {order_id} ---")
print(f"Original Amount  : ₹{order_amount}")
print(f"Discount (10%)   : ₹{discount_amount}")
print(f"Final Amount     : ₹{final_amount}")
print(f"Large Order?     : {is_large_order}")
print(f"Free Shipping?   : {is_eligible_for_free_shipping}")
print(f"Priority Order?  : {is_priority_order}")
print(f"Total Processed  : ₹{total_processed}")
```

---

## ⚠️ Common Mistakes

| Mistake | Galat | Sahi |
|---|---|---|
| Assignment vs Comparison | `a = b` (assign) | `a == b` (compare) |
| Division result | `10 / 2` = 5.0 (float) | `10 // 2` = 5 (int) |
| AND vs OR confusion | `a > 5 and a > 10` | Pehle samjho dono chahiye ya ek |
| Negative modulus | `-7 % 3` = 2 (Python specific) | Dhyan rakho |

---

