# ===== ASSIGNMENT — PRODUCT WAREHOUSE =====

product_id = 12271824
product_name = "pen"
price = 145.25
in_stock = True
warehouse_code = 122824

# f-string se print karo
print(f"\n--- Product Summary ---")
print(f"Product ID: {product_id}")
print(f"Product Name: {product_name}")
print(f"Product Price: {price}")
print(f"Product Stock: {in_stock}")
print(f"Product Warehouse Code: {warehouse_code}")

# type() verify karo
print(type(product_id))
print(type(product_name))
print(type(price))
print(type(in_stock))
print(type(warehouse_code))


# Raw strings se convert karo
raw_price = "1299.50"
raw_in_stock = "True"

price_converted = float(raw_price)       # float mein
in_stock_converted = raw_in_stock.lower()=="true"    # sahi boolean method se

print(f"Converted Price: {price_converted} | Type: {type(price_converted)}")
print(f"Converted In Stock: {in_stock_converted} | Type: {type(in_stock_converted)}")