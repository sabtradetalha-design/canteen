# Campus Canteen Billing System

print("===================================")
print("     CAMPUS CANTEEN BILLING")
print("===================================")
print("Menu:")
print("1. Burger       - PKR 350")
print("2. Sandwich     - PKR 250")
print("3. Fries        - PKR 150")
print("4. Tea          - PKR 100")
print("0. Checkout")
print("-----------------------------------")

subtotal = 0
total_quantity = 0

while True:
    choice = input("Select an item (1-4) or 0 to checkout: ")

    if choice == "0":
        break
    elif choice == "1":
        item_name = "Burger"
        price = 350
    elif choice == "2":
        item_name = "Sandwich"
        price = 250
    elif choice == "3":
        item_name = "Fries"
        price = 150
    elif choice == "4":
        item_name = "Tea"
        price = 100
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or 0.")
        continue

    quantity_text = input("Enter quantity for " + item_name + ": ")

    if not quantity_text.isdigit():
        print("Invalid quantity. Please enter a whole number greater than 0.")
        continue

    quantity = int(quantity_text)

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        continue

    item_total = price * quantity
    subtotal = subtotal + item_total
    total_quantity = total_quantity + quantity

    print(item_name + " x " + str(quantity) + " added: PKR " + str(item_total))
    print("Current subtotal: PKR " + str(subtotal))
    print("-----------------------------------")

print()
print("============= FINAL BILL =============")
print("Total quantity of items:", total_quantity)
print("Subtotal: PKR", format(subtotal, ".2f"))

if subtotal >= 1000:
    discount = subtotal * 0.10
    print("Discount (10%): PKR", format(discount, ".2f"))
else:
    discount = 0
    print("Discount: PKR 0.00")

final_bill = subtotal - discount
print("Final bill: PKR", format(final_bill, ".2f"))
print("Thank you for visiting the campus canteen!")
print("======================================")
