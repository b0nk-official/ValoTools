# Text UI portion of ValoTools

# Imports
import random
from os import system as runCommand
from time import sleep as wait
from random import choice

# Variables
weapons = [
    "Classic",
    "Shorty",
    "Frenzy",
    "Ghost",
    "Sheriff",
    "Spectre",
    "Stinger",
    "Ares",
    "Phantom",
    "Vandal",
    "Operator",
    "Marshal",
    "Bucky",
    "Judge",
    "Guardian",
    "Odin",
    "Bulldog"
]
agents = [
    "Jett",
    "Phoenix",
    "Astra",
    "Viper",
    "Cypher",
    "Chamber",
    "Fade",
    "Sage",
    "Skye",
    "Brimstone",
    "Breach",
    "Yoru",
    "Omen",
    "Sova",
    "Reyna",
    "Raze",
    "Neon",
    "Killjoy",
    "KAY/O"
]
armorTypes = [
    "no",
    "Light",
    "Heavy"
]
allMaps = [
    "Ascent",
    "Haven",
    "Split",
    "Pearl",
    "Icebox",
    "Fracture",
    "Bind",
    "Breeze"
]

# Functions
def selectFunc():
    print("ValoTools\n---------------------------\nSelect what you want to use.\n1. Random Loadout\n2. Random Agent\n3. Random Map (Custom Game)\nx. Exit ValoTools\n")

    selectedFunc = input()
    possibleChoices = ["1", "2", "3", "x"]

    return selectedFunc

def textUI():
    runCommand("cls")
    print("Running text-based ui...")
    wait(0.5)
    runCommand("cls")
    wait(0.1)
    runCommand("title ValoTools")

    selectedFunc = ""

    def getSelectedFunc():
        selectedFunc = selectFunc()

        if selectedFunc == "1": # Random Loadout
            print("\n" + choice(weapons) + " with " + choice(armorTypes) + " armor.\n")
            input()
            runCommand("cls")
            getSelectedFunc()
        elif selectedFunc == "2": # Random Agent
            print("\n" + choice(agents) + "\n")
            input()
            runCommand("cls")
            getSelectedFunc()
        elif selectedFunc == "3": # Random Map for Custom Games
            print("\n" + choice(allMaps) + "\n") # do maps thing
            input()
            runCommand("cls")
            getSelectedFunc()
        elif selectedFunc == "x": # Exit Program
            runCommand("exit")
        else:
            print("\nNot a valid option.\n")
            input()
            runCommand("cls")
            getSelectedFunc()
    
    getSelectedFunc()