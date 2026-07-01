# Day 1 — Python Basics: Variables & Data Types

---

## 📌 1. Variable kya hota hai?

**Simple words mein:**
Variable ek "dabba" hai jisme aap data rakhte ho. Dabba ka naam aap dete ho, aur usme koi bhi value store kar sakte ho.

**DE mein kyun zaroori hai:**
Jab hum pipeline mein data process karte hain — jaise kisi order ka amount, customer ka naam, ya delivery status — ye sab variables mein store hota hai taaki hum usse use, check, aur transform kar sakein.

**Syntax:**
```python
variable_naam = value
```

**Example:**
```python
order_id = 12271824
customer_name = "Avinash"
order_amount = 455.00
is_delivered = False
```

**Rules for naming variables:**
- Sirf letters, numbers, underscore _ allowed hai
- Number se shuru nahi ho sakta (1name ❌, name1 ✅)
- Spaces nahi (order id ❌, order_id ✅)
- Case sensitive hai (Name aur name alag hain)

---

## 📌 2. Data Types

Python mein 4 basic data types hote hain jo DE mein sabse zyada use hote hain:

### 🔢 Integer (int)
- Poore numbers — decimal nahi
- Use: row count, IDs, age, year

```python
total_rows = 1000
order_id = 12271824
year = 2024
```

### 🔢 Float
- Decimal numbers
- Use: price, percentage, latitude/longitude

```python
price = 49.99
completion_rate = 87.5
order_amount = 455.00
```

### 📝 String (str)
- Text data — hamesha quotes mein (single ya double dono chalte hain)
- Use: naam, city, status, category

```python
company = "Google"
status = 'active'
customer_name = "Avinash"
```

### ✅ Boolean (bool)
- Sirf 2 values — True ya False (capital T aur F zaroori)
- Use: flags, conditions (is_active, has_error, is_delivered)

```python
is_processed = True
has_error = False
is_delivered = False
```

---

## 📌 3. type() Function

Kisi bhi variable ka type check karne ke liye:

```python
print(type(order_id))        # <class 'int'>
print(type(customer_name))   # <class 'str'>
print(type(order_amount))    # <class 'float'>
print(type(is_delivered))    # <class 'bool'>
```

**DE mein use:** Jab CSV se data aata hai aur aapko verify karna ho ki data sahi type mein convert hua ya nahi — `type()` se check karte hain.

---

## 📌 4. print() aur f-strings

### Simple print:
```python
print(order_id)         # 12271824
print(customer_name)    # Avinash
```

### f-string (formatted print) — sabse important:
```python
print(f"Order ID: {order_id}")
print(f"Customer: {customer_name}")
print(f"Amount: {order_amount}")
print(f"Delivered: {is_delivered}")

# Ek line mein poora summary
print(f"Order {order_id} for {customer_name} worth ₹{order_amount} — Delivered: {is_delivered}")
```

**f-string kya hai:** f"..." ke andar curly braces {} mein variable naam likhte hain — Python automatically uski value wahan daal deta hai.

**DE mein use:** Pipeline logs likhne ke liye — "Processing order 12271824... Done." — ye sab f-strings se hota hai.

---

## 📌 5. Type Conversion

Real pipelines mein CSV se data aata hai to **sab kuch string hota hai** — chahe number ho ya boolean. Aapko sahi type mein convert karna padta hai.

### String → Integer:
```python
raw_id = "12271824"
order_id = int(raw_id)
print(type(order_id))    # <class 'int'>
```

### String → Float:
```python
raw_amount = "455.00"
order_amount = float(raw_amount)
print(type(order_amount))    # <class 'float'>
```

### ⚠️ Boolean Trap — Common Mistake:
```python
raw_delivered = "False"

# GALAT TARIKA ❌
is_delivered = bool(raw_delivered)
print(is_delivered)    # True — WRONG! Kyun? Kyunki bool() sirf dekhta hai
                       # "kya string mein kuch hai?" — "False" word hai to True

# SAHI TARIKA ✅
is_delivered = raw_delivered.lower() == "true"
print(is_delivered)    # False — CORRECT!
```

**Rule yaad rakho:** `bool()` se kabhi string convert mat karo. Hamesha string comparison use karo.

---

## 📌 6. Real DE Example — Sab ek saath

```python
# CSV se aaya raw data (sab string mein)
raw_order_id = "12271824"
raw_customer_name = "Avinash"
raw_order_amount = "455.00"
raw_is_delivered = "False"

# Sahi types mein convert karo
order_id = int(raw_order_id)
customer_name = raw_customer_name           # already string hai
order_amount = float(raw_order_amount)
is_delivered = raw_is_delivered.lower() == "true"

# Verify karo
print(f"Order ID: {order_id} | Type: {type(order_id)}")
print(f"Customer: {customer_name} | Type: {type(customer_name)}")
print(f"Amount: {order_amount} | Type: {type(order_amount)}")
print(f"Delivered: {is_delivered} | Type: {type(is_delivered)}")

# Summary log
print(f"\n✅ Order {order_id} for {customer_name} worth ₹{order_amount} — Delivered: {is_delivered}")
```

---

## ⚠️ Common Mistakes

| Mistake | Galat | Sahi |
|---|---|---|
| Boolean trap | `bool("False")` → True | `"false" == "true"` → False |
| Integer se float | `455` | `455.00` ya `float(455)` |
| String without quotes | `name = Avinash` ❌ | `name = "Avinash"` ✅ |
| Boolean small letter | `true` / `false` ❌ | `True` / `False` ✅ |

---


