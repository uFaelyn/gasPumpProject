import info

# Deciding on the discount based on the card number, and returning it at as a float.
def getDiscount(startPrice, card) -> float:
        if card <= 4000:
                price = startPrice - startPrice * 0.02
        elif card <= 7000 and card > 4000:
                price = startPrice - startPrice * 0.03
        else:
                price = startPrice - startPrice * 0.04
        return price

# Taking the final price per gallon, and multiplying it by the amount of gallons the user wishes to purchase.
def totalPrice(endingPrice):
        gallons = int(input("How many gallons do you wish to purchase? \n"))
        tPrice = endingPrice * gallons
        return tPrice

# Assigns the list in get_octanes() to the variable gasPrice. 
gasPrice = info.get_octanes()

# While loop
keepRunning = True
while keepRunning:
        # User can decide whether to accept the discount, decline it, or exit the program all together. 
        # Also ensures it is not case sensitive.
        answer = input("Would you like to use your discount? \n (Y)es \n (N)o \n E(x)it \n")
        answer = answer.lower()

        # Logic for the answer
        if answer == "y":
                
                # Gets the card number from the user, ensuring it is not below 1000 and above 9999
                cards = 0
                while cards == 0:
                        cardNum = int(input("Please enter your card number"))
                        if cardNum >= 1000 or cardNum <= 9999:
                                cards = 1
                        else:
                                print("Invalid card number")
                        
                        # Lists the grades out alongside the prices, and returns the users choice.
                        gradeToUse = info.get_octane(gasPrice)

                        # Handles the price, applying the discount and printing the selection alongside the discounted price.
                        startingPrice = gradeToUse.price
                        endingPrice = getDiscount(startingPrice, cardNum)
                        print("\n", f"{gradeToUse.accountName} | Discount Price : {endingPrice}", "\n")
                        keepRunning = False
        elif answer == "n":
                
                # Skips the discount and goes straight into processing the price.
                gradeToUse = info.get_octane(gasPrice)
                startingPrice = gradeToUse.price 
                endingPrice = startingPrice
                print("\n")
        elif answer == "x":
                # Exits the program
                keepRunning = False
        else:
                # Passive aggresive computers are the best
                print("What..?")

# Calls the totalPrice funtion from earlier, and combines the discounted price with the gallons they purchased. Prints it out and closes.
total = totalPrice(endingPrice)
print(f"Your total cost is {total} \n", "Thank you come again")