cart = []
while True:
    print("Menu\n1.Add item\n2.remove item\n3.view cart\n4.items in cart\n5.exit")
    ch = input("What would you like to do: ")
    if ch == "1":
        item = input("What would you like to add: ")
        cart.append(item)
        print(f"{item} was added")

    elif ch == "2":
        if not cart:
            print("Empty cart")

        else:
            item = input("What would you like to remove: ")
            if item in cart:
                cart.remove(item)
                print(f"{item} was removed")
            else:
                print("Item not found in cart")

    elif ch == "3":
        if cart:
            for i,item in enumerate(cart,1):
                print(f"{i}. {item}")

        else:
            print("Empty cart nenba")

    elif ch == "4":
        print(len(cart),"Items in cart")


    elif ch == "5":
        print("Nandri Nenba")
        break
    else:
        print("Invalid option")