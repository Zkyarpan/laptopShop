from tabulate import tabulate


def readLaptopList():
    laptopsList = []
    file = open("laptops.txt", "r")
    lines = file.readlines()
    for line in lines:
        a = line.strip().split(', ')
        laptopsList.append(a)
    file.close()
    return laptopsList


def displayLaptop(laptopsList):
    # Adding S.No. to the laptops
    for i in range(len(laptopsList)):
        laptop = laptopsList[i]
        laptop.insert(0, i+1)

    headers = ['S.No.', 'Name', 'Company', 'Price',
               'Quantity', 'Generation', 'Graphics Card']
    table = laptopsList.copy()
    table.insert(0, headers)

    print("""\n\n                  << ______________ :: List of Available Laptops :: ______________ >>\n     """)

    print(tabulate(table, headers="firstrow", tablefmt="grid"))
