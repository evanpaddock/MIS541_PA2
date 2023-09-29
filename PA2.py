import time
from datetime import date
from operator import itemgetter
from string import punctuation


def Main():
    ClearScreen()

    global cars, positiveWords, reviews

    cars = []
    positiveWords = []
    reviews = []

    ReadInFile("cars.txt", cars)
    ReadInFile("positive_word_dictionary.txt", positiveWords)
    ReadInFile("reviews.txt", reviews)

    AsciiArtMenu()
    DisplayMenu()
    menuChoice = input("Please make a selection: ")

    ClearScreen()

    while menuChoice != "4":
        RouteEm(menuChoice)

        DisplayMenu()
        menuChoice = input("Please make a selection: ")
        ClearScreen()


def ClearScreen():
    print("\n" * 50)


def AsciiArtMenu():
    print(
        R"""  
        _______
       //  ||\ \
 _____//___||_\ \___
 )  _          _    \
 |_/ \________/ \___|
___\_/________\_/______
          """
    )


def DisplayMenu():
    print(
        "Danish's Car Emporium\n\n"
        "1. Car Inventory Menu\n"
        "2. Review Menu\n"
        "3. Reports Menu\n"
        "4. Exit the Application\n"
    )


def RouteEm(menuChoice):
    if menuChoice == "1":
        CarInventory()
        ClearScreen()
        ReadInFile("cars.txt", cars)
    elif menuChoice == "2":
        Review()
        ClearScreen()
        ReadInFile("reviews.txt", reviews)
    elif menuChoice == "3":
        Reports()
        ClearScreen()
    else:
        print("Invalid Menu Choice. Please try again.")
    print()


def CarInventory():
    def DisplayMenu():
        print(
            "Car Inventory\n\n"
            "1. Add a car to the inventory\n"
            "2. Edit a car's data in the inventory\n"
            "3. Delete a car from the inventory\n"
            "4. Exit the inventory menu and return to the main menu\n\n"
            "5. View all cars currently in inventory\n"
        )

    def AddCar():
        carName = GetCarName()

        isInInventory = CheckIfCarExists(carName, cars)

        ClearScreen()

        if isInInventory:
            print("Car already exists. Reverting to inventory menu...")
            time.sleep(2)
        else:
            carType = GetType()

            ClearScreen()

            carYearOfManufacture = GetManufactureYear()

            ClearScreen()

            carPrice = GetPrice()

            ClearScreen()

            cars.append([carName, carType, carYearOfManufacture, carPrice])
            WriteOutFile("cars.txt", cars)

            print("Car added to inventory successfully!")
            print("Reverting to inventory menu...")
            time.sleep(2)

    def EditCar():
        print("Available cars: ")
        WriteCarNames()

        print("\nWhat is the name of the car you want to edit?")
        carName = input("Name: ")

        isInInventory = CheckIfCarExists(carName, cars)

        ClearScreen()

        if isInInventory:
            foundCar = FindCar(carName)

            updatedCar = list(foundCar)

            # Stores the fields for a car in order of how they are stored
            carFieldNames = ["Name", "Type", "Year of Manufacture", "Price"]

            # Stores methods to use if user answers yes to editing a field
            fieldMethods = [GetCarName, GetType, GetManufactureYear, GetPrice]
            count = 1

            for field in foundCar[1:]:
                ClearScreen()

                print(
                    f"Current {carFieldNames[count]}: {field}. Do you want to change this?"
                )
                wantToEdit = input("(yes/no): ")

                ClearScreen()

                if wantToEdit == "yes":
                    print(f"Please enter a new {carFieldNames[count]}.\n")

                    # updates the car they are changing by calling the method to update it.
                    updatedCar[count] = fieldMethods[count]()

                count += 1

            index = 0
            while index < len(cars):
                if cars[index][0] == foundCar[0]:
                    cars[index] = updatedCar
                index += 1

            WriteOutFile("cars.txt", cars)

            print(f"{carName} edited successfully! Reverting to inventory menu...")
            time.sleep(2)
        else:
            print(
                f"{carName} does not exist in inventory. Reverting to inventory menu..."
            )
            time.sleep(2)

    def DeleteCar():
        print("Available cars: ")

        # Prints car names
        for car in cars:
            print(car[0])

        print("\nWhich car would you like to delete?")
        carName = input("Car Name: ")

        isInInventory = CheckIfCarExists(carName, cars)

        if isInInventory:
            index = 0
            while index < len(cars):
                if cars[index][0] == carName:
                    cars.remove(cars[index])
                index += 1

            WriteOutFile("cars.txt", cars)

            print("Car deleted successfully! Reverting to inventory menu...")
            time.sleep(2)
        else:
            print("Car does not exist in inventory. Reverting to inventory menu...")
            time.sleep(2)

    def IsValidCarType(carTypeToCheck):
        validTypes = ["sedan", "hatchback", "suv", "truck", "van", "convertable"]
        isValid = False

        for carType in validTypes:
            if carType == carTypeToCheck:
                isValid = True

        return isValid

    def RouteEm(menuChoice):
        if menuChoice == "1":
            AddCar()
            ClearScreen()
        elif menuChoice == "2":
            EditCar()
            ClearScreen()
        elif menuChoice == "3":
            DeleteCar()
            ClearScreen()
        elif menuChoice == "5":
            WriteAllCarInfo()
            ClearScreen()
        else:
            print("Invalid choice. Please try again.\n")

    def IsValidPriceFormat(price):
        try:
            float(price)
            return True
        except Exception:
            return False

    def GetType():
        print("What is the type of the car?")
        carType = input("Type: ")

        while not IsValidCarType(carType):
            ClearScreen()

            print("Car Type must be a valid car type. Please try again.\n")
            print("What is the type of the car?")
            carType = input("Type: ")

        return carType

    def GetManufactureYear():
        print("What is the year of manufacture of the car?")
        carYearOfManufacture = input("Year of manufacture: ")

        while not IsValidYearFormat(carYearOfManufacture) or not (
            2010 <= int(carYearOfManufacture) < 2020
        ):
            ClearScreen()

            print("Year of manufacture must be between 2010 and 2020.\n")
            print("What is the year of manufacture of the car?")
            carYearOfManufacture = input("Year of manufacture: ")

        return carYearOfManufacture

    def GetPrice():
        print("What is the price of the car?")
        carPrice = input("Price: ")

        while not IsValidPriceFormat(carPrice) or float(carPrice) <= 0.00:
            ClearScreen()

            print(f"Car Price must be more than $0.00")
            print("What is the price of the car?")
            carPrice = input("Price: ")

        return carPrice

    DisplayMenu()
    userChoice = input("Please make a selection: ")
    ClearScreen()

    while userChoice != "4":
        RouteEm(userChoice)

        DisplayMenu()
        userChoice = input("Please make a selection: ")
        ClearScreen()


def Review():
    def DisplayMenu():
        print(
            "Review\n\n"
            "1. Add a review\n"
            "2. Exit the review menu and return to the main menu\n"
        )

    def RouteEm(menuChoice):
        if menuChoice == "1":
            AddAReview()
            # i1-5,comment 1-100 chars, auto date mm-dd-yyyy
        else:
            print("Invalid choice. Please try again.\n")

    def AddAReview():
        def GetRating():
            print("What rating do you give?(1-5)")
            rating = input("Rating: ")

            while not IsValidRating(rating):
                ClearScreen()
                print("Rating must be an integer between 1 and 5.\n")
                print("What rating do you give?(1-5)")
                rating = input("Rating: ")
            return rating

        def IsValidRating(rating):
            try:
                int(rating)
                return True
            except Exception:
                return False

        def IsValidComment(comment):
            if 0 < len(comment) < 100:
                return True
            else:
                return False

        def GetComment():
            print("Please leave your comment (1-100 characters).")
            comment = input("Comment: ")

            while not IsValidComment(comment):
                ClearScreen()
                print("Comments must be between 0 and 100 characters.\n")
                print("What comment do you give?")
                comment = input("Comment: ")
            return comment

        print("Available cars: ")
        WriteCarNames()
        print("")

        carName = GetCarName()
        isInInventory = CheckIfCarExists(carName, cars)

        ClearScreen()

        if isInInventory:
            serialNumber = str(len(reviews) + 1)

            rating = GetRating()

            ClearScreen()

            comment = GetComment()

            ClearScreen()

            today = date.today()
            dateMDY = today.strftime("%m-%d-%Y")

            reviews.append([serialNumber, carName, dateMDY, rating, comment])

            WriteOutFile("reviews.txt", reviews)

            print("Review has been added successfully!")
            print("Reverting to review menu...")
            time.sleep(2)
        else:
            print(f"{carName} does not exist in inventory. Reverting to review menu...")
            time.sleep(2)

    DisplayMenu()
    userChoice = input("Please make a selection: ")

    ClearScreen()

    while userChoice != "2":
        RouteEm(userChoice)

        ClearScreen()
        DisplayMenu()
        userChoice = input("Please make a selection: ")
        ClearScreen()


def Reports():
    def DisplayMenu():
        print(
            "Reports\n"
            "1. A report displaying the rating statistics for a given year (average, lowest and highest rating)\n"
            "2. A report displaying the individual reviews, number of reviews and average rating for each car\n"
            "3. A report displaying each review comment with positive words and the number of such comments\n"
            "4. Exit the inventory menu and return to the main menu\n"
        )

    def RouteEm(menuChoice):
        if menuChoice == "1":
            RatingStatisticsByYear()
            ClearScreen()
        elif menuChoice == "2":
            RatingsByCar()
            ClearScreen()
        elif menuChoice == "3":
            ReviewsWithPositiveWords()
            ClearScreen()
        else:
            print("Invalid choice. Please try again.\n")

    def WriteOutReport(message, fileName):
        f = open(fileName, "w")

        for submessage in message:
            for line in submessage:
                f.write(line)

        f.close()

    def RatingStatisticsByYear():
        print("What year do you want to report?")
        year = input("Year: ")

        while not IsValidYearFormat(year) or not 2015 <= int(year) <= 2020:
            ClearScreen()

            print("Invalid Year. Must be between 2015 and 2020.\n")

            print("What year do you want to report?")
            year = input("Year: ")

        ClearScreen()

        # Sorts reviews by year - elem[2][-4:] targets a specific elements year from the last 4 characters '06-20-2020' = '2020'
        reviewsByYear = sorted(reviews, key=lambda elem: elem[2][-4:])

        minRating = 0
        maxRating = 0
        avgRating = 0
        count = 0

        for review in reviewsByYear:
            if count == 0 and year == review[2][-4:]:
                minRating = int(review[3])
                maxRating = int(review[3])
                avgRating = int(review[3])
                count += 1
            elif year == review[2][-4:]:
                avgRating += int(review[3])
                count += 1

                if minRating > int(review[3]):
                    minRating = int(review[3])

                if maxRating < int(review[3]):
                    maxRating = int(review[3])
        if count != 0:
            message = (
                f"Rating Stats for the year of {year}:\n"
                f"Max Rating: {maxRating}\n"
                f"Min Rating: {minRating}\n"
                f"Avg Rating: {avgRating/count}\n"
            )
        else:
            message = f"There were 0 reviews for the year of {year}\n"

        WriteOutReport(message, f"rating_statistics_{year}.txt")

        print(message)
        input("Press any key to continue...")

    def ReviewsWithPositiveWords():
        def ContainsPositiveWord(listOfWords):
            for word in listOfWords:
                for listOfpositiveWords in positiveWords:
                    for positiveWord in listOfpositiveWords:
                        if word.strip(punctuation).lower() == positiveWord:
                            return True
            return False

        message = []

        for review in reviews:
            comment = review[4]
            wordsInComment = comment.split(" ")
            isPositiveComment = ContainsPositiveWord(wordsInComment)
            if isPositiveComment:
                message.append(
                    [
                        f"Car: {review[1]}\nReview Date: {review[2]}\nRating: {review[3]}\nComment: {review[4]}\n\n"
                    ]
                )
        if len(message) == 0:
            message = ["There were no comments with positive words."]

        WriteOutReport(message, "comments_with_positive_words.txt")

        for line in message:
            for item in line:
                print(item)
        input("Press any key to continue...")

    def RatingsByCar():
        reviewsByCar = sorted(reviews, key=itemgetter(1))

        currentCar = reviewsByCar[0][1]
        count = 1
        sumOfReviewRatings = int(reviewsByCar[0][3])

        message = []
        commentsForCurrentCar = [reviewsByCar[0][4]]

        for review in reviewsByCar[1:]:
            if review[1] == currentCar:
                count += 1
                sumOfReviewRatings += int(review[3])
                commentsForCurrentCar.append(review[4])
            else:
                message.append(
                    [
                        f"Car: {currentCar} | Number of Reviews: {count} |  Average Rating: {sumOfReviewRatings/count}\n\n",
                    ]
                )
                for comment in commentsForCurrentCar:
                    message[len(message) - 1].append(comment + "\n")

                count = 1
                sumOfReviewRatings = int(review[3])
                commentsForCurrentCar = [review[4]]
                currentCar = review[1]

        message.append(
            [
                f"\nName: {currentCar} | Number of Reviews: {count} |  Average Rating: {sumOfReviewRatings/count}\n",
            ]
        )
        for comment in commentsForCurrentCar:
            message[len(message) - 1].append(comment + "\n")

        WriteOutReport(message, "avg_rating_by_car.txt")

        for carList in message:
            for item in carList:
                print(item)
        input()

    DisplayMenu()
    userChoice = input("Please make a selection: ")

    ClearScreen()

    while userChoice != "4":
        RouteEm(userChoice)

        DisplayMenu()
        userChoice = input("Please make a selection: ")
        ClearScreen()


def ReadInFile(fileName, listToReadTo):
    f = open(fileName, "r")
    line = f.readline()

    while line != "":
        line = line.strip("\n")
        line = line.strip()
        item = line.split("#")
        listToReadTo.append(item)
        line = f.readline()

    f.close()


def WriteOutFile(fileName, listToReadFrom):
    f = open(fileName, "w")

    for unit in listToReadFrom:
        for item in unit:
            f.write(item)
            if item != unit[-1]:
                f.write("#")
        f.write("\n")
    f.close()


def CheckIfCarExists(carName, carList):
    for car in carList:
        if car[0] == carName:
            return True
    return False


def FindCar(carName):
    for car in cars:
        if car[0] == carName:
            return tuple(car)


def GetCarName():
    print("What is the name of the car?")
    carName = input("Name: ")
    while len(carName) == 0:
        ClearScreen()

        print("Car Name must be 1 character or greator. Please try again.")
        print("What is the name of the car?")
        carName = input("Name: ")

    return carName


def WriteCarNames():
    # Prints car names
    for car in cars:
        print(car[0])


def IsValidYearFormat(year):
    try:
        int(year)
        return True
    except Exception:
        return False


def WriteAllCarInfo():
    attributeNames = ["Name", "Type", "Year", "Price"]

    for car in cars:
        count = 0
        for attribute in car:
            print(f"{attributeNames[count]}: {attribute} ", end="")
            count += 1
        print("")

    input("Press enter to continute...")


Main()
