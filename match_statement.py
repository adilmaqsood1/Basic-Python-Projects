# Input product_code and quantity
product_code = int(input("Enter product code (1-5): "))
quantity = int(input("Enter quantity sold: "))

# Initialize retail_price
retail_price = 0

# Use match statement to determine retail price based on product_code
match product_code:
    case 1:
        retail_price = quantity * 2.99
    case 2:
        retail_price = quantity * 4.50
    case 3:
        retail_price = quantity * 9.99
    case 4:
        retail_price = quantity * 4.49
    case 5:
        retail_price = quantity * 7.00
    case _:
        print("Error: Invalid product code or quantity")
        exit()

# Display the retail value of the purchase
if retail_price > 0:
    print(f"The retail value of the purchase is ${retail_price}")
else:
    print("Error: Invalid product code or quantity")
