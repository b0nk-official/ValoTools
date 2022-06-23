# Main File for ValoTools

# Imports
from os import system as runCommand
from time import sleep as wait

# Functions
def selectUI():
    runCommand("title \"ValoTools | Selecting UI Type\"")
    print("ValoTools\n---------------------------\nSelect your UI type.\n1. Text-based\n2. Graphics-based\n")

    uiChoice = input()

    if uiChoice == "1":
        print("Loading text-based ui...")
        wait(1)
        textUI()
    elif uiChoice == "2":
        print("Graphics-based ui is in progress, loading text-based ui...")
        wait(1)
        textUI()
    else:
        print("Not a valid option. Select 1 or 2.")
        selectUI()

def textUI():
    runCommand("cls")
    print("Running text-based ui...")
    wait(0.5)
    runCommand("start text_ui.py")

# Call Function
selectUI()