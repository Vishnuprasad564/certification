cart = []  # List to store items

while True:
    print("\n1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Calculate Total")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        cart.append({"name": name, "price": price, "quantity": quantity})
        print(f"{name} added to cart.")
    
    elif choice == '2':
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            print("\nYour Cart:")
            for i in range(len(cart)):
                item = cart[i]
                print(f"{i+1}. {item['name']} - {item['price']} x {item['quantity']}")
    
    elif choice == '3':
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            name = input("Enter item name to remove: ")
            found = False
            for item in cart:
                if item['name'] == name:
                    cart.remove(item)
                    print(f"{name} removed from cart.")
                    found = True
                    break
            if not found:
                print("Item not found.")
    
    elif choice == '4':
        total = 0
        for item in cart:
            total += item['price'] * item['quantity']
        print(f"Total amount: {total}")
    
    elif choice == '5':
        print("Thank you for shopping!")
        break
    
    else:
        print("Invalid choice. Please try again.")
