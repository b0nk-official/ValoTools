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
basicStrats = [
    "TO YOUR REFT - Put your headsets backwards.",
    "PLEASURE SEEKER - When you get a kill, you have to wait for a teammate to give you the gawk-gawk before you can move again.",
    "CQB KINGS - Shotgun only.",
    "WHAT ARE YOU AIMING AT - Put your sensitivity on the highest it can go.",
    "CROSSHAIR PLACEMENT KING - Put your sensitivity on the lowest it can go.",
    "BRING A KILLJOY - When round starts, be in your spawn. Only move out when the spike is planted.",
    "GHETTO LOOKIN AHH - You are only allowed to spend as much as the poorest player has.",
    "FLABBERMOUTH GHOSTS - Only dead players are allowed to comm or speak."
]
ascentStrats = [
    "FUCK THEM DOORS - On attackers, destroy all doors before you can plant. On defenders, destroy all doors before you can defuse."
]

# Functions
def selectFunc():
    runCommand("cls")
    print("ValoTools\n---------------------------\nSelect what you want to use.\n1. Random Loadout\n2. Random Agent\n3. Random Map (Custom Game)\n4. Random Strat\nx. Exit ValoTools\n")

    selectedFunc = input()

    return selectedFunc

def randStrat(): # Random Strat
    def actualRandStrat():
        print("\nWhat map are you on? (WARNING: RECOMMENDED TO HAVE A FIVE-STACK)\n")

        mapSelection = input()

        if mapSelection in allMaps:
            if mapSelection == allMaps[0]: # Ascent
                for x in basicStrats:
                    print("\n" + choice(ascentStrats))
                    anotherStrat(mapSelection)
        else:
            print("Not a valid option.")
            actualRandStrat()
    
    def actualRandStratMapDetermined(mapSelected):
        if mapSelected == allMaps[0]: # Ascent
            for x in basicStrats:
                print("\n" + choice(ascentStrats))
                anotherStrat(mapSelected)
    
    def anotherStrat(mapSelected):
        print("\nWould you like another strat? (y/n)")
        extraStrat = input()

        if extraStrat == "y":
            actualRandStratMapDetermined(mapSelected)
        elif extraStrat == "n":
            textUInoAnim()
            runCommand("exit")
        else:
            print("\nNot a valid option.")
            input()
            anotherStrat(mapSelected)

    actualRandStrat()
            
def loadingAnim(): # Loading Animation when booting the text UI
    runCommand("cls")
    print("Running text-based ui...")
    wait(0.5)
    runCommand("cls")
    wait(0.1)

def textUI(): # Start text UI from UI selection menu
    loadingAnim()
    runCommand("title ValoTools")
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
        elif selectedFunc == "4":
            randStrat()
        elif selectedFunc == "x": # Exit Program
            runCommand("exit")
        else:
            print("\nNot a valid option.\n")
            input()
            runCommand("cls")
            getSelectedFunc()
    
    getSelectedFunc()

def textUInoAnim(): # Return to text UI from a different command
    runCommand("title ValoTools")
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
        elif selectedFunc == "4":
            randStrat()
        elif selectedFunc == "x": # Exit Program
            runCommand("exit")
        else:
            print("\nNot a valid option.\n")
            input()
            runCommand("cls")
            getSelectedFunc()
    
    getSelectedFunc()