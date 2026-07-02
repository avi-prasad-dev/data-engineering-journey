## 📋 Day 2 — Assignment
'''
Scenario:Tum ek Data Engineer ho. Tumhare paas ek product ka data hai. 
Neeche diye gaye variables use karke sab calculate karo:

**Tasks:**
1. discounted_price calculate karo
2. savings_amount calculate karo (kitne rupaye bache)
3. is_low_stock — True agar stock 10 se kam ho
4. is_deal_of_day — True agar featured bhi ho AND sale mein bhi ho
5. is_affordable — True agar discounted price 50000 se kam ho
6. Sab print karo ek clean summary mein f-strings se

'''
product_name = "Laptop"
original_price = 75000.00
discount_percent = 15
stock_quantity = 48
min_stock_threshold = 10
is_featured = True
is_in_sale = True

# Calculation using Arithmatic operators
saving_amount = (original_price * discount_percent)/100
final_amount = original_price - saving_amount

# Using Comparision operator
is_low_stock = stock_quantity < min_stock_threshold
is_affordable = final_amount < 50000

# Using Logical operator
is_deal_of_day = is_featured and is_in_sale

# Summary
print(f"--- Product Name    : {product_name} ---")
print(f"Original Amount     : ₹{original_price}")
print(f"Saving Amount       : ₹{saving_amount}")
print(f"Final Amount        : ₹{final_amount}")
print(f"Low Stock Alert     : {is_low_stock}")
print(f"Is affordable       : {is_affordable}")
print(f"Is in Deal Day      : {is_deal_of_day}")
