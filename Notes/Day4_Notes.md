# Day 4 — Python Loops (for / while)
# Data Engineering Journey — Avinash
# Date: 4 July

---

## 📌 1. Loops kya hote hain?

**Simple words mein:**
Loop ka matlab hai — ek kaam baar baar karo jab tak condition poori na ho.

**DE mein kyun zaroori hai:**
Pipeline mein hazar ya lakhon rows hoti hain. Tum manually har row process nahi kar sakte — loop automatically har row par same logic apply karta hai.

Real example:
- 10,000 orders ki CSV hai — har order par discount calculate karo
- 50 files hain — sab ko ek ek karke load karo
- 1 lakh customers hain — sabka status check karo

---

## 📌 2. for Loop

**Syntax:**
```python
for item in collection:
    # har item par ye karo
    code_here
```

### Basic example:
```python
cities = ["Delhi", "Mumbai", "Bangalore", "Hyderabad"]

for city in cities:
    print(f"Processing city: {city}")
```

**Output:**
```
Processing city: Delhi
Processing city: Mumbai
Processing city: Bangalore
Processing city: Hyderabad
```

---

## 📌 3. range() — Numbers par loop

```python
# range(stop) — 0 se start, stop tak (stop included nahi)
for i in range(5):
    print(i)        # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(1, 6):
    print(i)        # 1, 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)        # 0, 2, 4, 6, 8
```

### DE mein use — batch processing:
```python
total_records = 1000
batch_size = 100

for batch_start in range(0, total_records, batch_size):
    batch_end = batch_start + batch_size
    print(f"Processing records {batch_start} to {batch_end}")
```

---

## 📌 4. Loop with List of Dictionaries (Most Important for DE)

Real data pipelines mein data aisa hota hai — list of dictionaries.
Har dictionary ek row hoti hai.

```python
orders = [
    {"order_id": "ORD-001", "amount": 1500, "status": "delivered"},
    {"order_id": "ORD-002", "amount": 450,  "status": "pending"},
    {"order_id": "ORD-003", "amount": 2200, "status": "delivered"},
    {"order_id": "ORD-004", "amount": 80,   "status": "cancelled"},
]

for order in orders:
    print(f"Order: {order['order_id']} | Amount: ₹{order['amount']} | Status: {order['status']}")
```

---

## 📌 5. Loop + Conditionals (Pipeline Logic)

Ye combination DE mein sabse zyada use hota hai:

```python
orders = [
    {"order_id": "ORD-001", "amount": 1500, "status": "delivered"},
    {"order_id": "ORD-002", "amount": 450,  "status": "pending"},
    {"order_id": "ORD-003", "amount": 2200, "status": "delivered"},
    {"order_id": "ORD-004", "amount": 80,   "status": "cancelled"},
]

total_revenue = 0
delivered_count = 0
failed_orders = []

for order in orders:
    order_id = order["order_id"]
    amount = order["amount"]
    status = order["status"]

    # Category assign karo
    if amount >= 2000:
        tier = "Platinum"
    elif amount >= 1000:
        tier = "Gold"
    elif amount >= 500:
        tier = "Silver"
    else:
        tier = "Regular"

    # Revenue count karo sirf delivered orders ka
    if status == "delivered":
        total_revenue += amount
        delivered_count += 1
    elif status == "cancelled":
        failed_orders.append(order_id)

    print(f"{order_id} | ₹{amount} | {tier} | {status}")

print(f"\n--- Pipeline Summary ---")
print(f"Total Revenue    : ₹{total_revenue}")
print(f"Delivered Orders : {delivered_count}")
print(f"Failed Orders    : {failed_orders}")
```

---

## 📌 6. while Loop

**Syntax:**
```python
while condition:
    # condition True hone tak chalega
    code_here
```

```python
retry_count = 0
max_retries = 3

while retry_count < max_retries:
    print(f"Connecting to database... Attempt {retry_count + 1}")
    retry_count += 1

print("Max retries reached.")
```

### ⚠️ Infinite Loop — Danger!
```python
# Ye kabhi mat karo ❌
while True:
    print("ye kabhi band nahi hoga")
    # break nahi hai — infinite loop!
```

---

## 📌 7. break aur continue

### break — loop turant band karo:
```python
orders = ["ORD-001", "ORD-002", "ERROR", "ORD-004"]

for order in orders:
    if order == "ERROR":
        print(f"❌ Error found — stopping pipeline")
        break                    # loop band ho gaya
    print(f"Processing: {order}")
```

### continue — current iteration skip karo, loop chalti rahe:
```python
orders = [
    {"order_id": "ORD-001", "amount": 1500},
    {"order_id": "ORD-002", "amount": -50},    # invalid — skip karo
    {"order_id": "ORD-003", "amount": 2200},
]

for order in orders:
    if order["amount"] <= 0:
        print(f"⚠️ Skipping invalid order: {order['order_id']}")
        continue                 # is order ko skip karo, agle par jao
    print(f"✅ Processing: {order['order_id']} | ₹{order['amount']}")
```

---

## 📌 8. enumerate() — Index bhi chahiye saath mein

```python
files = ["orders.csv", "customers.csv", "products.csv"]

for index, filename in enumerate(files, start=1):
    print(f"File {index} of {len(files)}: {filename}")
```

**Output:**
```
File 1 of 3: orders.csv
File 2 of 3: customers.csv
File 3 of 3: products.csv
```

---

## 📌 9. Real DE Example — Complete Data Processing Pipeline

```python
# Raw data — CSV se aaya hua (sab string mein)
raw_transactions = [
    {"txn_id": "TXN-001", "amount": "2500.00", "status": "success",  "type": "credit"},
    {"txn_id": "TXN-002", "amount": "-100.00", "status": "success",  "type": "debit"},
    {"txn_id": "TXN-003", "amount": "750.50",  "status": "failed",   "type": "credit"},
    {"txn_id": "TXN-004", "amount": "1200.00", "status": "success",  "type": "credit"},
    {"txn_id": "TXN-005", "amount": "0.00",    "status": "success",  "type": "debit"},
]

# Initialize counters
total_credit = 0
total_debit = 0
failed_txns = []
skipped_txns = []
processed_count = 0

print("--- Starting Transaction Pipeline ---\n")

for i, txn in enumerate(raw_transactions, start=1):
    txn_id = txn["txn_id"]
    amount = float(txn["amount"])       # string → float conversion
    status = txn["status"]
    txn_type = txn["type"]

    # Validation — invalid amount skip karo
    if amount <= 0:
        skipped_txns.append(txn_id)
        print(f"⚠️  [{i}] Skipping {txn_id} — invalid amount: {amount}")
        continue

    # Failed transactions skip karo
    if status == "failed":
        failed_txns.append(txn_id)
        print(f"❌ [{i}] Failed txn: {txn_id}")
        continue

    # Process valid transactions
    if txn_type == "credit":
        total_credit += amount
    else:
        total_debit += amount

    processed_count += 1
    print(f"✅ [{i}] Processed {txn_id} | ₹{amount} | {txn_type}")

# Final Report
print(f"\n--- Pipeline Report ---")
print(f"Total Processed  : {processed_count}")
print(f"Total Credit     : ₹{total_credit}")
print(f"Total Debit      : ₹{total_debit}")
print(f"Net Balance      : ₹{total_credit - total_debit}")
print(f"Failed Txns      : {failed_txns}")
print(f"Skipped Txns     : {skipped_txns}")
```

---

## ⚠️ Common Mistakes

| Mistake | Galat | Sahi |
|---|---|---|
| Indentation | Loop body ka indent galat | Hamesha 4 spaces andar |
| Infinite while | `while True` bina break | Hamesha exit condition rakho |
| range off by one | `range(1, 5)` = 1,2,3,4 | Stop value included nahi |
| List modify during loop | Loop mein list change karna | Pehle copy banao |
| break vs continue confuse | Break = loop band, Continue = skip | Yaad rakho difference |

---

