# Text User Interface for ValoTools

# Imports
import random
import os
from time import sleep as wait
from random import choice
import values

# Variables

values.appendBasic()

weapons, allWeapons = values.getWeapons()
weaponStats = values.getWeaponStats()
agents = values.getAgents()
allMaps = values.getMaps()
armorTypes = values.getArmorTypes()
basicStrats = values.getBasicStrats()
ascentStrats = values.getAscentStrats()
havenStrats = values.getHavenStrats()
splitStrats = values.getSplitStrats()
pearlStrats = values.getPearlStrats()
iceboxStrats = values.getIceboxStrats()
fractureStrats = values.getFractureStrats()
bindStrats = values.getBindStrats()
breezeStrats = values.getBreezeStrats()

versionNum = values.getVersionNum()

# Functions
def selectFunc():
    os.system("cls && title ValoTools - Selecting Function && color 04")
    print("ValoTools " + versionNum + "\n---------------------------\nSelect what you want to use.\n1. Random Loadout\n2. Random Agent\n3. Random Map (Custom Game)\n4. Random Strat\n5. Weapon Stats\n")

    selectedFunc = input()

    return selectedFunc

def weaponStatsFunc(): # Get Weapon Stats
    os.system("cls && title ValoTools - Weapon Stats")
    print("What weapon do you need stats for? Type list for a list of weapons. (Stats provided by valorant.fandom.com)\n")

    selectedWep = input()

    if str.lower(selectedWep) == "list":
        os.system("cls")
        for x in allWeapons:
            print(x)
        input()

    if weaponStats.get(selectedWep):
        os.system("cls && title ValoTools - Viewing " + selectedWep + " Stats")
        print("Weapon Name: " + selectedWep)
        print("Damage: " + weaponStats[selectedWep]["damage"])
        print("Fire Mode: " + weaponStats[selectedWep]["fireMode"])
        print("Fire Rate: " + weaponStats[selectedWep]["fireRate"])
        print("Run Speed: " + weaponStats[selectedWep]["runSpeed"])
        print("Equip Speed: " + weaponStats[selectedWep]["equipSpeed"])
        print("Degree of First Shot: " + weaponStats[selectedWep]["firstShotAcc"])
        print("Reload Speed: " + weaponStats[selectedWep]["reloadSpeed"])
        print("Ammunition: " + weaponStats[selectedWep]["magSize"])
        
        def redoStatsFunc():
            print("\nDo you want to see the stats of another weapon? (y/n)")
            redoStats = input()

            if redoStats == "y":
                weaponStatsFunc()
            elif redoStats == "n":
                textUI()
            else:
                os.system("cls")
                redoStatsFunc()
        
        redoStatsFunc()
    else:
        weaponStatsFunc()

def randStrat(): # Random Strat
    os.system("title ValoTools - Random Strat")
    def actualRandStrat():
        os.system("cls")
        print("What map are you on? First letter capital. (WARNING: RECOMMENDED TO HAVE A FIVE-STACK)\n")

        mapSelection = input()

        if mapSelection in allMaps:
            os.system("title ValoTools - Viewing Strats for " + mapSelection)
            if str.lower(mapSelection) == str.lower(allMaps[0]): # Ascent
                for x in basicStrats:
                    os.system("cls")
                    print("\n" + choice(ascentStrats))
                    redoStrat(mapSelection)
            elif str.lower(mapSelection) == str.lower(allMaps[1]): # Haven
                for x in basicStrats:
                    os.system("cls")
                    print("\n" + choice(havenStrats))
                    redoStrat(mapSelection)
            elif str.lower(mapSelection) == str.lower(allMaps[2]): # Split
                for x in basicStrats:
                    os.system("cls")
                    print("\n" + choice(splitStrats))
                    redoStrat(mapSelection)
            elif str.lower(mapSelection) == str.lower(allMaps[3]): # Pearl
                for x in basicStrats:
                    os.system("cls")
                    print("\n" + choice(pearlStrats))
                    redoStrat(mapSelection)
            elif str.lower(mapSelection) == str.lower(allMaps[4]): # Icebox
                for x in basicStrats:
                    os.system("cls")
                    print("\n" + choice(iceboxStrats))
                    redoStrat(mapSelection)
            elif str.lower(mapSelection) == str.lower(allMaps[5]): # Fracture
                for x in basicStrats:
                    os.system("cls")
                    print("\n" + choice(fractureStrats))
                    redoStrat(mapSelection)
            elif str.lower(mapSelection) == str.lower(allMaps[6]): # Bind
                for x in basicStrats:
                    os.system("cls")
                    print("\n" + choice(bindStrats))
                    redoStrat(mapSelection)
            elif str.lower(mapSelection) == str.lower(allMaps[7]): # Breeze
                for x in basicStrats:
                    os.system("cls")
                    print("\n" + choice(breezeStrats))
                    redoStrat(mapSelection)
        else:
            actualRandStrat()
    
    def actualRandStratMapDetermined(mapSelected):
        os.system("title ValoTools - Viewing Strats for " + mapSelected)
        if str.lower(mapSelected) == str.lower(allMaps[0]): # Ascent
            for x in basicStrats:
                os.system("cls")
                print("\n" + choice(ascentStrats))
                redoStrat(mapSelected)
        elif str.lower(mapSelected) == str.lower(allMaps[1]): # Haven
            for x in basicStrats:
                os.system("cls")
                print("\n" + choice(havenStrats))
                redoStrat(mapSelected)
        elif str.lower(mapSelected) == str.lower(allMaps[2]): # Split
            for x in basicStrats:
                os.system("cls")
                print("\n" + choice(splitStrats))
                redoStrat(mapSelected)
        elif str.lower(mapSelected) == str.lower(allMaps[3]): # Pearl
            for x in basicStrats:
                os.system("cls")
                print("\n" + choice(pearlStrats))
                redoStrat(mapSelected)
        elif str.lower(mapSelected) == str.lower(allMaps[4]): # Icebox
            for x in basicStrats:
                os.system("cls")
                print("\n" + choice(iceboxStrats))
                redoStrat(mapSelected)
        elif str.lower(mapSelected) == str.lower(allMaps[5]): # Fracture
            for x in basicStrats:
                os.system("cls")
                print("\n" + choice(fractureStrats))
                redoStrat(mapSelected)
        elif str.lower(mapSelected) == str.lower(allMaps[6]): # Bind
            for x in basicStrats:
                os.system("cls")
                print("\n" + choice(bindStrats))
                redoStrat(mapSelected)
        elif str.lower(mapSelected) == str.lower(allMaps[7]): # Breeze
            for x in basicStrats:
                os.system("cls")
                print("\n" + choice(breezeStrats))
                redoStrat(mapSelected)
    
    def redoStrat(mapSelected):
        print("\nWould you like another strat? (y/n)")
        extraStrat = input()

        if extraStrat == "y":
            actualRandStratMapDetermined(mapSelected)
        elif extraStrat == "n":
            textUI()
        else:
            redoStrat(mapSelected)

    actualRandStrat()
            
def loadingAnim(): # Loading Animation when booting the text UI
    os.system("cls && color 0a && title ValoTools - Loading Text UI")
    print("Loading text-based ui...")
    wait(1)
    os.system("cls")
    print("Running text-based ui...")
    wait(0.5)
    os.system("cls")
    wait(0.1)
    os.system("title ValoTools")
    

def textUI(): # Start text UI
    def getSelectedFunc():
        selectedFunc = selectFunc()

        if selectedFunc == "1": # Random Loadout
            os.system("title ValoTools - Random Loadout")
            print("\n" + choice(weapons) + " with " + choice(armorTypes) + " armor.\n")
            input()
            os.system("cls")
            getSelectedFunc()
        elif selectedFunc == "2": # Random Agent
            os.system("title ValoTools - Random Agent")
            print("\n" + choice(agents) + "\n")
            input()
            os.system("cls")
            getSelectedFunc()
        elif selectedFunc == "3": # Random Map for Custom Games
            os.system("title ValoTools - Random Map")
            print("\n" + choice(allMaps) + "\n") # do maps thing
            input()
            os.system("cls")
            getSelectedFunc()
        elif selectedFunc == "4": # Random Strat
            randStrat()
        elif selectedFunc == "5": # Weapon Stats
            weaponStatsFunc()
        else:
            os.system("cls")
            getSelectedFunc()
    
    getSelectedFunc()


# Start File
loadingAnim()
textUI()