from Invoice import invoice


def sellLaptops(laptopsList):
    name = input("Enter Customer Name:")
    try:
        number = int(input("Enter Laptops SN Number:"))
        quantity = int(input("Enter Quantity:"))

        for i, laptop in enumerate(laptopsList):
            if laptop[0] == number:  # Compare serial numbers
                stock = int(laptop[3])
                if quantity > stock:
                    print("\nInsufficient Quantity!!")
                    print("Available quantity in store:", stock)
                    return

                laptopsList[i][3] = str(stock - quantity)  # Update stock
                updateStock(laptopsList)
                invoice(number, name, laptopsList, quantity)
                print("\t______________________________________________________________")
                print("\tCongratulations! The " +
                      laptop[1] + " laptop is now in the hands of " + name + ".")
                print("\t    __________Your invoice is ready for review__________ ")
                print("\t__________please take a moment to check it over___________")
                print("\t____________________________________________________________")
                return
        print("_______________________________________________________________________")
        print("We apologize, but the laptop you are seeking is not currently available.")

    except ValueError:
        print("Integer Value should be entered for Laptops numbers and Quantity")


def updateStock(laptopsList):
    with open("Laptops.txt", "w") as update:
        for i in range(len(laptopsList)):
            for j in range(6):
                if j == 5:
                    update.write(str(laptopsList[i][j]))
                else:
                    update.write(str(laptopsList[i][j])+',')
    update.close()
