
def Main():
    ClearScreen()
    cars = []
    postiveWords = []
    reviews = []

    ReadInFile("cars.txt", cars)
    ReadInFile("positive_word_dictionary.txt", postiveWords)
    ReadInFile("reviews.txt", reviews)

    AsciiArtMenu()
    DisplayMenu()
    menuChoice = input('Please make a selection: ')

    ClearScreen()

    while(menuChoice != "4"):
        RouteEm(menuChoice)
     
        DisplayMenu()
        menuChoice = input('Please make a selection: ')
        ClearScreen()

    WriteOutFile("cars.txt", cars)
    WriteOutFile("positive_word_dictionary.txt", postiveWords)
    WriteOutFile("reviews.txt", reviews)

def ClearScreen():
    print("\n" * 50) 

def AsciiArtMenu():
    print(R"""  
        _______
       //  ||\ \
 _____//___||_\ \___
 )  _          _    \
 |_/ \________/ \___|
___\_/________\_/______
          """)
    
def DisplayMenu():
    print('Danish\'s Car Emporium\n\n'
          '1. Car Inventory Menu\n'
          '2. Review Menu\n'
          '3. Reports Menu\n'
          '4. Exit the Application\n')
    
def RouteEm(menuChoice):
    if(menuChoice == "1"):
        CarInventory()
        ClearScreen()
    elif(menuChoice == "2"):
        Review()
        ClearScreen()
    elif(menuChoice == "3"):
        print("Reports")
        input()
        ClearScreen()
    else:
        print("Invalid Menu Choice. Please try again.")
    print()

def CarInventory():
    def DisplayMenu():
        print("Car Inventory\n\n"
              "1. Add a car to the inventory\n"
              "2. Edit a car's data in the inventory\n"
              "3. Delete a car from the inventory\n"
              "4. Exit the inventory menu and return to the main menu\n")
    
    def RouteEm(menuChoice):
        if(menuChoice == "1"):
            print("Add Car")
            # n,t,manyear,price
        elif(menuChoice == "2"):
            print("Edit Car")
            # nameofcar to be edited
        elif(menuChoice == "3"):
            print("Delete Car")
            # nameofcar to be deleted
        else:
            print("Invalid choice. Please try again.\n")

    DisplayMenu()
    userChoice = input("Please make a selection: ")

    ClearScreen()

    while(userChoice != "4"):
        RouteEm(userChoice)

        DisplayMenu()
        userChoice = input("Please make a selection: ")
        ClearScreen()

def Review():
    def DisplayMenu():
        print("Review\n\n"
              "1. Add a review\n"
              "2. Exit the review menu and return to the main menu\n")
    
    def RouteEm(menuChoice):
        if(menuChoice == "1"):
            print("Add a review")
            # i1-5,comment 1-100 chars, auto date mm-dd-yyyy
        else:
            print("Invalid choice. Please try again.\n")

    DisplayMenu()
    userChoice = input("Please make a selection: ")

    ClearScreen()

    while(userChoice != "2"):
        RouteEm(userChoice)

        DisplayMenu()
        userChoice = input("Please make a selection: ")
        ClearScreen()

def Reports():
    def DisplayMenu():
        print("Reports\n\n"
              "1. A report displaying the rating statistics for a given year (average, lowest and highest rating)\n"
              "2. A report displaying the individual reviews, number of reviews and average rating for each car\n"
              "3. A report displaying each review comment with positive words and the number of such comments\n"
              "4. Exit the inventory menu and return to the main menu\n")
    
    def RouteEm(menuChoice):
        if(menuChoice == "1"):
            print("Stastics per year")
        elif(menuChoice == "2"):
            print("Indivual review, number of reviews and average rating for each car")

        elif(menuChoice == "3"):
            print("review comments with positive words and the number of comments")
        else:
            print("Invalid choice. Please try again.\n")

    DisplayMenu()
    userChoice = input("Please make a selection: ")

    ClearScreen()

    while(userChoice != "4"):
        RouteEm(userChoice)

        DisplayMenu()
        userChoice = input("Please make a selection: ")
        ClearScreen()

def ReadInFile(fileName, listToReadTo):
    f = open(fileName, "r")
    line = f.readline()
    while(line != ""):
        print(line)
        line = line.strip('\n')
        line = line.strip()
        item = line.split('#')
        listToReadTo.append(item)
        line = f.readline()
        
    f.close()

def WriteOutFile(fileName, listToReadFrom):
    f = open(fileName, "w")
    for unit in listToReadFrom:
        for item in unit:
            f.write(item)
            if(item != unit[-1]):
                f.write("#")
        f.write("\n")
    f.close()

Main()