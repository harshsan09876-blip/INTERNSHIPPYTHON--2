# Day 15 - Shopping Bill Generator

# Input and print the customer name
customer_name = input("Enter the customer name: ")
print("Customer:", customer_name)


# ENLIST THE ITEMS - COST PRICE
mehendi = float(input("Enter the cost price of Mehendi: "))
turmeric = float(input("Enter the cost price of Turmeric: "))
kesar = float(input("Enter the cost price of Kesar: "))
towel = float(input("Enter the cost price of Towel: "))


# STORE THE ORIGINAL PRICE
mehendi_op = float(input("Enter the original price of Mehendi: "))
turmeric_op = float(input("Enter the original price of Turmeric: "))
kesar_op = float(input("Enter the original price of Kesar: "))
towel_op = float(input("Enter the original price of Towel: "))


# DISPLAY AVAILABLE PRODUCTS
print("\nAvailable Products:")
print("1. Mehendi")
print("2. Turmeric")
print("3. Kesar")
print("4. Towel")


# LET CUSTOMER CHOOSE THE PRODUCT
product = input("\nEnter the product name: ").lower()


# SELECT PRODUCT AND CALCULATE ORIGINAL TOTAL
match product:

    case "mehendi":
        print("Mehendi selected")
        quantity = int(input("Enter quantity: "))
        original_total = quantity * mehendi_op
        cost_total = quantity * mehendi

    case "turmeric":
        print("Turmeric selected")
        quantity = int(input("Enter quantity: "))
        original_total = quantity * turmeric_op
        cost_total = quantity * turmeric

    case "kesar":
        print("Kesar selected")
        quantity = int(input("Enter quantity: "))
        original_total = quantity * kesar_op
        cost_total = quantity * kesar

    case "towel":
        print("Towel selected")
        quantity = int(input("Enter quantity: "))
        original_total = quantity * towel_op
        cost_total = quantity * towel

    case _:
        print("Invalid product selected.")
        exit()


# DISPLAY ORIGINAL CALCULATION
print("\nOriginal Total =", original_total)


# BARGAINING / NEGOTIATION
final_sp = float(input("Enter final price after bargaining: "))


# CUSTOMER SAVING
customer_saving = original_total - final_sp


# SELLER PROFIT OR LOSS
profit_loss = final_sp - cost_total


# FINAL BILL
print("\n" + "=" * 45)
print("              FINAL BILL")
print("=" * 45)

print("Customer Name :", customer_name)
print("Product       :", product.title())
print("Quantity      :", quantity)
print("Original Total: ₹", original_total)
print("Final SP      : ₹", final_sp)
print("-" * 45)


# CUSTOMER SAVING
if customer_saving > 0:
    print("Customer Saving: ₹", customer_saving)
elif customer_saving < 0:
    print("Extra Amount Paid: ₹", abs(customer_saving))
else:
    print("No Saving")


# SELLER PROFIT / LOSS
if profit_loss > 0:
    print("Seller Profit : ₹", profit_loss)
elif profit_loss < 0:
    print("Seller Loss   : ₹", abs(profit_loss))
else:
    print("No Profit/Loss")


print("-" * 45)
print("Final Billing Amount: ₹", final_sp)
print("=" * 45)

print("Thank you for shopping!")