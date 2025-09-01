cart = ["jersey","shorts","boots","socks"]
print(cart[0])
print(cart[1:3])
print(cart)
item = input("Enter the item to be inserted: ")
if item in cart:
    print("item already exists! ")

else:
    cart.append(item)
print(cart)

rem = input("Do you want to remove any item y/n: ")
if rem == "y":
    delitem = input("Enter the item to be removed: ")
    if delitem in cart:
        cart.remove(delitem)
        print(f"{delitem} has been removed")
        print(cart)

    else:
        print("Item not in cart")
elif rem == "n":
    print("Bye")

else:
    print("Enter y/n")
