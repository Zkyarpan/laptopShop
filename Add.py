import datetime
import Sell


def addLaptopStock(laptopList):
    laptopNumber = int(input("Enter SN number of laptops: "))
    if laptopNumber < 1 or laptopNumber > len(laptopList):
        print("Invalid laptop SN number. Please try again.")
        print("_______________________________________\n")
        return

    laptopStock = int(input("Enter the quantity you want to add: "))
    shippingCompany = input("Enter shipping company: ")
    shippingCost = int(input("Enter total cost of shipping: "))

    for i in range(len(laptopList)):
        if (i+1 == laptopNumber):
            a = int(laptopList[i][3])
            a += laptopStock
            laptopList[i][3] = a
            Sell.updateStock(laptopList)
            addLaptopStockDetails(
                laptopList, laptopNumber, laptopStock, shippingCompany, shippingCost)
            print("_______________________________________\n")
            print(laptopList[i][0]+" is added Successfully")
            print("Please check your Laptops.txt file")
            print("Display the list of laptops to see the newly added quantity")
            print("_________________________________________________________")


def addLaptopStockDetails(laptopList, laptopNumber, StockAmount, laptopShippingCompany, laptopShipppingCost):
    k = datetime.datetime.now()
    for i in range(len(laptopList)):
        if (i+1 == laptopNumber):
            Name = laptopList[i][0]
            company = laptopList[i][1]
            price = laptopList[i][2]
            quantity = laptopList[i][3]
            gen = laptopList[i][4]
            graphicsCard = laptopList[i][5]

    f = "Add" + Name + ".txt"
    f = open(f, "w")
    f.write("\n")
    f.write('''\t\t                             laptop Added                  \n''')
    f.write("\n"+"\t\t__________________________________________________________________________")
    f.write("\n"+"\t\t                          Laptop Name       : "+Name)
    f.write("\n"+"\t\t                          Laptop company    : "+company)
    f.write("\n"+"\t\t                          Laptop Price      : "+price)
    f.write("\n"+"\t\t                          Laptop Quantity   : "+str(quantity))
    f.write("\n"+"\t\t                          Generation        : "+gen)
    f.write("\n"+"\t\t                          Graphics Card     : "+graphicsCard)
    f.write("\n"+"\t\t                          Stock added       : "+str(StockAmount))
    f.write("\n"+"\t\t                          Shipping Company  : " +
            laptopShippingCompany)
    f.write("\n"+"\t\t                          Shipping Cost     : $" +
            str(laptopShipppingCost))
    f.write("\n"+"\t\t                          Delivery Date     : " +
            str(k.year)+" - "+str(k.month)+" - "+str(k.day))
    f.write("\n"+"\t\t                          Delivery Time     : " +
            str(k.hour)+" : "+str(k.minute))
    f.write("\n"+"\t\t__________________________________________________________________________")
    f.write("\n"+"\t\t          __________________________________________________              ")
    f.write("\n"+"\t\t__________________________________________________________________________")

    f.close()
