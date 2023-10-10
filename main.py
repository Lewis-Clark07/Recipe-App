#imports
import csv # a python module that is used to assist with the reading of csv files by seperating values by commas
import numpy as np # a python module that is used to carry out mathmatical function. It is used in this program to generate a linear sequence
#Global Variables

#Global Constants

def Main(): #declaring the main function that will run the whole program
    choice = input("Would you like to add or view a recipe(A or V): ")
    match choice.upper():
        case "A":
            Recipe_Add()
        case "V":
            Recipe_View()
        
def Recipe_Add():
    Repeat = True
    Ingredient_List = []
    Quantitiy_List = []
    Unit_List = []
    Ingredient = ""
    Amount = 0
    Unit = ""
    Recipe_Name = str(input("Enter the name of the recipe you wish to add: "))
    Serving_Size = str(input("Enter the serving size of the recipe: "))
    while Repeat == True:
        Ingredient = str(input("Enter an ingredient: "))
        Amount = str(input(f"Enter the amount of {Ingredient} needed(no unit of measurement): "))
        Unit = str(input(f"Enter the unit for the {Ingredient}: "))
        Ingredient_List.append(Ingredient)
        Quantitiy_List.append(Amount)
        Unit_List.append(Unit)
        Choice = input("Would you like to add another Ingredient(Y or N): ")
        if Choice.upper() == "Y":
            Repeat = True
        elif Choice.upper() == "N":
            Repeat = False
        else:
            print("Please only use single characters.")
    print(Ingredient_List)
    print(Quantitiy_List)
    print(Unit_List)
    File = open(f"Recipe App\{Recipe_Name}.csv","a")
    File.write(f"{Serving_Size}")
    for i in range(Ingredient_List.__len__()):
        File.write(f",{Ingredient_List[i]}")
        File.write(f",{Quantitiy_List[i]}")
        File.write(f",{Unit_List[i]}")
    File.close()


def Recipe_View():
    Recipe_Name = str(input("Enter the name of the recipe you wish to view: "))
    Serving_Size = int(input("Enter the serving size of the recipe: "))
    with open(f"Recipe App\{Recipe_Name}.csv") as File:
        Reader = csv.reader(File, delimiter=",")
        for Row in Reader:
            print(Row)
        New_Amounts(Recipe_Name)


def New_Amounts(Recipe_Name):
    New_Amount_List = []
    with open(f"Recipe App\{Recipe_Name}.csv") as File:
        Reader = csv.reader(File, delimiter=",")
        print(np.arange(2, 100, 3))
        for i in range(File.__len__()):
            print(i)

Main()