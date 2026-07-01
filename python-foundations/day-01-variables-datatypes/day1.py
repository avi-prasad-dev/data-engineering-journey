# Day 1 — Variables, Data Types, Type Conversion
# Data Engineering Journey — Avinash

# ===== VARIABLES AND DATA TYPES =====
order_id = 12271824          # int
customer_name = "Avinash"    # str
order_amount = 455.00        # float
is_delivered = False         # bool

# ===== F-STRING PRINTING =====
print(f"Order ID: {order_id}")
print(f"Customer: {customer_name}")
print(f"Amount: ₹{order_amount}")
print(f"Delivered: {is_delivered}")
print(f"Order {order_id} for {customer_name} worth ₹{order_amount} — Delivered: {is_delivered}")

# ===== TYPE CHECKING =====
print(type(order_id))
print(type(customer_name))
print(type(order_amount))
print(type(is_delivered))

# ===== TYPE CONVERSION =====
raw_order_id = "12271824"
raw_amount = "455.00"
raw_delivered = "False"

order_id_converted = int(raw_order_id)
order_amount_converted = float(raw_amount)

# IMPORTANT: bool("False") = True (wrong way)
# Correct way to convert string to boolean:
is_delivered_correct = raw_delivered.lower() == "true"

print(type(order_id_converted))
print(type(order_amount_converted))
print(f"Correct boolean conversion: {is_delivered_correct}")  # False ✅

# ===== REAL DE USE CASE =====
statuses = ["True", "False", "True"]
for status in statuses:
    delivered = status.lower() == "true"
    print(f"Delivered: {delivered}")