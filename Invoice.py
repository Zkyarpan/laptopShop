import datetime
import os.path


def invoice(userNumber, customerName, laptopsList, quantity):
    # get the laptop data for the selected userNumber
    selected_laptop = laptopsList[userNumber-1]
    Name = selected_laptop[0]
    company = selected_laptop[1]
    price = selected_laptop[2]
    gen = selected_laptop[4]
    graphicsCard = selected_laptop[5]

    # calculate the total price based on the quantity and laptop price
    total_price = int(price.strip('$')) * quantity

    # create a new invoice file for the customer or append to an existing one
    if not os.path.exists(customerName + ".txt"):
        f = open(customerName + ".txt", "w")
        f.write("_________________________________________________________________\n")
        f.write("                                        Date: {} / {} / {}\n".format(datetime.datetime.now().year,
                                                                                      datetime.datetime.now().month,
                                                                                      datetime.datetime.now().day))

        f.write("                                        PAN No. 90393923\n")
        f.write("  ______________      Laptop store        ______________    \n")
        f.write("  ______________      Ithari,Nepal        ______________    \n")
        f.write("                                        Contact No.: 9840471599\n")
        f.write("                                        ________________________\n")

        f.write("_________________________________________________________________\n")
        f.write("Customer's Name: {}\n".format(customerName))
        f.write("Name: {}\n".format(Name))
        f.write("Company: {}\n".format(company))
        f.write("Quantity: {}\n".format(quantity))
        f.write("Price: {}\n".format(price))
        f.write("Generation: {}\n".format(gen))
        f.write("Graphics Card: {}\n".format(graphicsCard))
        f.write("___________________________\n")
        f.write("Your total price is: ${}\n".format(total_price))
        f.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
        f.write("           _________Dear Valued Customer________\n")
        f.write("         _________Kindly check your Invoice________\n")
        f.write("             _______Thank you for your visit______\n")
        f.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
        f.close()
        print("\nInvoice has been created successfully!")
        f.write("______________________________________")

    else:

        f = open(customerName + ".txt", "a")
        f.write("_________________________________________________________________\n")
        f.write("Date: {} / {} / {}\n".format(datetime.datetime.now().year,
                                              datetime.datetime.now().month,
                                              datetime.datetime.now().day))
        f.write("                                        PAN No. 90393923\n")
        f.write("                     Laptop store                        \n")
        f.write("                     Ithari,Nepal                         \n")
        f.write("                                        Contact No.: 9840471599\n")
        f.write(
            "___________________________________________________________________ \n")
        f.write("Customer's Name: {}\n".format(customerName))
        f.write("Name: {}\n".format(Name))
        f.write("Company: {}\n".format(company))
        f.write("Quantity: {}\n".format(quantity))
        f.write("Price: {}\n".format(price))
        f.write("Generation: {}\n".format(gen))
        f.write("Graphics Card: {}\n".format(graphicsCard))
        f.write("____________________\n")
        f.write("Your total price is: ${}\n".format(total_price))
        f.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
        f.write("           _________Dear Valued Customer________\n")
        f.write("         _________Kindly check your Invoice________\n")
        f.write("             _______Please Visit Again______\n")
        f.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
        print("\nInvoice has been created successfully!")
        f.write("______________________________________")
        f.close()
