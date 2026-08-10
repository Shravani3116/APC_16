cart = []


cart.append("Apple")
cart.append("Milk")
cart.append("Bread")


print("Shopping Cart:", cart)


item = input("Enter item to search: ")

if item in cart:
    print("Item found")
else:
    print("Item not found")


item = input("Enter item to remove: ")

if item in cart:
    cart.remove(item)
    print("Item removed")
else:
    print("Item not found")

print("Updated Cart:", cart)
