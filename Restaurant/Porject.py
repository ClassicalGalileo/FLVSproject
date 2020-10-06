from dishes import *
from drinks import *


tax = 1.065



def main():
    print("Welcome to the Chiara Bristo, here you'll find authentic French-Italian food")
    print("Here's our menu, have fun!")
    print("Press Enter to Continue... ")
    input()
    print(" ________________________________________________")
    print("    ITALIAN DISHES      |      FRENCH DISHES     ")
    print("                        |                        ")
    print("                 |LUNCH OPTIONS|                 ")
    print("                        |                        ")
    print("    Carbonara - $10     |      Onion Soup - $6.50")
    print("                        |                        ")
    print("    Pizza - $13.80      |      Pissaladiere - $5.30")
    print("                        |                          ")
    print("                 |DINNER OPTIONS|                  ")
    print("                        |                     ")
    print("    Risotto - $8.50     |      Basquaise - $9      ")
    print("                        |                     ")
    print("    Salami Salad - $13  |      Andouillette - $23")
    print("________________________|_________________________")
    print("Which one do you want? You may only choose one, since we are closing in about 20 minutes")
    dish = input("Answer: ")
    if (dish == "Carbonara"):
        plate = Carbonara.name
        costPlate = Carbonara.price
        pass

    if (dish == "Pizza"):
        plate = Pizza.name
        costPlate = Pizza.price
        pass

    if (dish == "Risotto"):
        plate = Risotto.name
        costPlate = Risotto.price
        pass

    if (dish == "Salami Salad"):
        plate = Salami.name
        costPlate = Salami.price
        pass

    if (dish == "Onion Soup"):
        plate = Onion_Soup.name
        costPlate = Onion_Soup.price
        pass

    if (dish == "Pissaladiere"):
        plate = Pissaladière.name
        costPlate = Pissaladiere.price
        pass

    if (dish == "Basquaise"):
        plate = Basquaise.name
        costPlate = Basquaise.price
        pass

    if (dish == "Andouillette"):
        plate = Andouillette.name
        costPlate = Andouillette.price
        pass


    print("Ok so what drinks want then? ")
    print("_________________|_________________")
    print("    PRODUCT      |     PRICE       ")
    print("_________________|_________________")
    print("                 |                 ")
    print("     Water       |      $3.50      ")
    print("                 |                 ")
    print("     Wine        |      $20        ")
    print("                 |                 ")
    print("     Soda        |      $2         ")
    print("                 |                 ")
    print("     Tea         |      $4         ")
    print("_________________|_________________")
    drinkChoice = input("Enter what you want ... ")

    if (drinkChoice == "Water"):
        liquid = Water.name
        costLiquid = Water.price
        

    if (drinkChoice == "Wine"):
        liquid = Wine.name
        costLiquid = Wine.price
        

    if (drinkChoice == "Soda"):
        liquid = Soda.name
        costLiquid = Soda.price
        

    if (drinkChoice == "Tea"):
        liquid = Tea.name
        costLiquid = Tea.price
        

    print("Great! " + str(plate) + ", and " + str(liquid) + " it is!")
    input("Press Enter to Continue...")
    print("Ok Sir/Ma'am, here's the bill: ")
    calculation_one = (costPlate + costLiquid)
    calculation_two = (calculation_one + (calculation_one*0.2)) * tax
    print(str(round(calculation_two, 2)) + " dollars, Thank you for coming.")


main()

