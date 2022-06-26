# Main File for ValoTools

# Imports
from os import system as runCmd
from time import sleep as wait
from random import choice
from text_ui import textUI as startTextUI, loadingAnim as loadingAnimTextUI
from values import getVersionNum

# Variables
versionNum = getVersionNum()

# Functions
def selectUI():
    runCmd("title ValoTools - Selecting UI Type")
    print("ValoTools " + versionNum + "\n---------------------------\nSelect your UI type.\n1. Text-based\n2. Graphics-based\n")

    uiChoice = input()

    if uiChoice == "1":
        print("\nLoading text-based ui...")
        wait(1)
        loadingAnimTextUI()
        startTextUI()
    elif uiChoice == "2":
        print("\nGraphics-based ui is in progress, loading text-based ui...")
        wait(1)
        loadingAnimTextUI()
        startTextUI()
    else:
        runCmd("cls")
        selectUI()

# Call Function
selectUI()