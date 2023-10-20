import csv
import math
import numpy as np

def Main():
    choice = input("Would you like to add or view a recipe (A or V): ")
    if choice.upper() == "A":
        Recipe_Add()
    elif choice.upper() == "V":
        Recipe_View()

def Recipe_Add():
    Repeat = True
    Ingredient_List = []
    Quantitiy_List = []
    Unit_List = []
    Ingredient = ""
    Amount = 0
    Unit = ""
    Recipe_Name = input("Enter the name of the recipe you wish to add: ")
    Serving_Size = input("Enter the serving size of the recipe: ")

    while Repeat:
        Ingredient = input("Enter an ingredient: ")
        Amount = float(input(f"Enter the amount of {Ingredient} needed (no unit of measurement): "))
        Unit = input(f"Enter the unit for the {Ingredient}: ")

        Ingredient_List.append(Ingredient)
        Quantitiy_List.append(Amount)
        Unit_List.append(Unit)

        choice = input("Would you like to add another Ingredient (Y or N): ")
        if choice.upper() == "Y":
            Repeat = True
        elif choice.upper() == "N":
            Repeat = False
        else:
            print("Please only use single characters.")

    with open(f"{Recipe_Name}.csv", "a", newline="") as File:
        writer = csv.writer(File)
        writer.writerow([Serving_Size] + Ingredient_List + Quantitiy_List + Unit_List)

def Recipe_View():
    Recipe_Name = input("Enter the name of the recipe you wish to view: ")
    Serving_Size = int(input("Enter the serving size of the recipe: "))
    New_Amount_List = New_Amounts(Recipe_Name, Serving_Size)

    with open(f"{Recipe_Name}.csv") as File:
        reader = csv.reader(File, delimiter=",")
        print(f"To make the recipe for {Recipe_Name} for {Serving_Size} people you will need:")
        for Row in reader:
            for i in range(1, len(Row), 3):
                print(f"{Row[i]}: {New_Amount_List[i // 3]}{Row[i + 2]}")

def New_Amounts(Recipe_Name, Serving_Size):
    New_Amount_List = [] #cake.csv
    with open(f"{Recipe_Name}.csv") as File:
        reader = csv.reader(File, delimiter=",")
        for Row in reader:
            for i in range(2, len(Row), 3):
                New_Amount = int(Row[i]) / int(Row[0]) * Serving_Size
                New_Amount_List.append(New_Amount)
    return New_Amount_List

Main()