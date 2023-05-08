from Read import readLaptopList, displayLaptop
import Add
import Sell


def selectOptions(): 
    try:
        flag = True
        while flag:
            print('''
                  
                  
                  
                  
                  
                            ____________________________________________________  

                                    ____________Laptop Store____________
                            ____________________________________________________
          
                                        Press 1 : Display available Laptops 
                                        Press 2 : Sell Laptops
                                        Press 3 : Add Laptops
                                        Press 4 : Exit
                            ____________________________________________________
                            ____________________________________________________
                                 
                                 ''')
            selectOption = input(
                '''Please select number of your choice :''')
            if selectOption == "1":
                displayLaptop(readLaptopList())
                print(''' 
                      ___________________________________________
                               Press 1: For selling Laptops
                            ________ Press 0: Exit ________''')
                userInput = input("\nTo proceed, please provide a value :")
                if userInput == "1":
                    Sell.sellLaptops(readLaptopList())
                elif userInput == "0":
                    print('''   
                         __________Dear, Valued Customer__________ 
                      _____________Thank you for visiting____________
                          __________Please visit again__________     ''')
                else:
                    print("Invalid input. Please enter a value between 0 and 1")

            elif selectOption == "2":
                displayLaptop(readLaptopList())
                print("\nTo sell laptop please follow the following instruction")
                print("______________________________________________________\n")
                Sell.sellLaptops(readLaptopList())

            elif selectOption == "3":
                displayLaptop(readLaptopList())
                print("\nTo add laptop please follow the following instruction")
                print("_____________________________________________________\n")
                Add.addLaptopStock(readLaptopList())

            elif selectOption == "4":
                flag = False
                print('''
                     __________Dear, Valued Customer__________ 
                  _____________Thank you for visiting____________
                       __________Please visit again__________  
                      ''')

            else:
                print("Error: Input must be a valid format. Please try again.")

    except ValueError:
        print("Oops! The value you entered is not an integer")


selectOptions()
