cart = ["ball","bat","shoe","socks"]

while True:

    print("1.Add\n2.View\n3.Exit")
    ch = input("Enter your choice: ")

    if ch == "1":
        item = input("Enter the item to add: ")
        if item in cart:
            print("Item already in cart")
        else:
            cart.append(item)
            print(cart)

    elif ch == "2":
        print("Your cart")
        print(f"\n{cart}")

    elif ch == "3":
        print("Bye")
        break
    else:
        print("Enter valid choice")