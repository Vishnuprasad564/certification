cart = []

def addtoCart():
    name = input("Enter the product name: ")
    price = int(input("Enter its price: "))
    quantity = input("Enter quantity")

    item = {
        "Name":name,
        "Price":price,
        "Quantity":quantity
    }

    cart.append(item)
    print(f"{name} added to cart")

def viewCart():
    if not cart:
        print("Empty cart")

    else:
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item['name']} - ${item['price']} x {item['quantity']}")
        print("----------------------\n")

def removeCart():
    viewCart()
    if not  cart:
        print("Empty cart")
        return
    name = input("Enter item to be removed")
    for item in cart:
        if item["Name"] == name:
            cart.remove(item)
            print(f"{name} removed from your  cart")

while True:
    print("\n1.Add to cart\n2.Remove from cart\n3.View cart\n4.Exit")

    ch = input("Enter your choice")

    if ch == "1":
        addtoCart()

    elif ch == "2":
        removeCart()

    elif ch == "3":
        viewCart()

    elif ch == "4":
        print("Thenks")
        break
    else:
        print("Invalid choice")
