# Text UI portion of ValoTools

# Imports
import random
from os import system as runCmd
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
    "Bulldog",
    "Knife"
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
    "FLABBERMOUTH GHOSTS - Only dead players are allowed to comm or speak.",
    "BRIMSTONE IRL - If you die, you have to do ten pushups before you are allowed to play again.",
    "ALPHA//OMEGA - If there is an agent that is the same as yours on the enemy team, you have to kill them before you can kill anybody else.",
    "LET ME SOLO HER - Only one player is allowed out of spawn at a time. If they die, another player can come out. Lowest k/d to highest.",
    "THE RATS DEN - When the round starts, you are not allowed to move. You can only move when spike is planted. If on defenders, you can\'t move ",
    "THE PHILANTHROPIST - The player with the most cash must sell and drop everything they have and buy for any teammates that need it.",
    "AROUND THE WORLD - You must set foot on every site before you can plant/defuse. If spike is transferred to another player, they must complete the challenge before planting.",
    "PRECISE GUNPLAY - Kills are only allowed while moving.",
    "OVER COMMUNICATION - Announce to your team every single action that you make until you are dead. (Reloading, walking, peaking, shooting, etc.)",
    "WILD WEST - Sheriffs only. Western accent. Armor allowed.",
    "IN THE SHADOWS - Ghosts only.",
    "RESPECT THE FALLEN - Buy the same loadout that the bottom frag has.",
    "WE ARE VALORANT - Buy all odins this round and rush into site as fast as possible. If not enough money, buy frenzys.",
    "FAKE PUSH - Buy all abilities. When pushing into site, waste all abilities and rotate to the other site.",
    "UNEXPECTED PEAKS - Jump before you peak any angle.",
    "MOTIVATE THE MANY - The bottom frag must give an inspirational speech. Every player must stay in spawn while the speech is going on.",
    "SHUT THE FUCK UP GUYS IM TRYNA CLUTCH - Everybody must stay silent for the whole round.",
    "THIS SHIT EXPENSIVE - Every player must spend as much as they can.",
    "ENEMY AMMUNITION - If somebody gets a kill, they have to drop their weapon they got a kill with and grab the enemy\'s weapon. Knife kills still allowed.",
    "DEAF AF - Turn your volume down to zero.",
    "FULL SEND IT - Either push a site as fast as possible as attackers or five-stack a site on defenders.",
    "RUSH B DO NOT STOP - Rush B site as fast as possible.",
    "COUNTER STRIKE: GLOBAL OFFENSIVE - Everybody is not allowed to use abilities this round.",
    "STEALTH MODE - Never stop crouching. Did you ever need to stand, anyway?",
    "FOLLOW THE LEADER - The top frag is the leader, and every player has to follow them in a line that follows their movements.",
    "DIRECTIONAL CALLOUTS - The only callouts allowed are Forward, Back, Left, and Right."
]
ascentStrats = [
    "FUCK THEM DOORS - On attackers, destroy all doors before you can plant. On defenders, destroy all doors before you can defuse."
]
havenStrats = [
    "AROUND THE WORLD 2 - You must set foot on every site before you can plant/defuse. If spike is transferred to another player, they must complete the challenge before planting."
]
splitStrats = [
    "BOOTS ON THE GROUND - Ziplines are not usable this round."
]
pearlStrats = [
    "PLAZA CRUSADE - Attackers: Push through mid plaza to any of the sites as fast as you can. Defenders: Push through mid plaza to flank on any of the sites as fast as you can."
]
iceboxStrats = [
    "BOOTS ON THE GROUND - Ziplines are not usable this round."
]
fractureStrats = [
    "BOOTS ON THE GROUND - Ziplines are not usable this round."
]
bindStrats = [
    
]
breezeStrats = [
    
]

def appendBasic(): # Put basic strats inside the map-specific ones
    for x in basicStrats:
        ascentStrats.append(x)
        havenStrats.append(x)
        splitStrats.append(x)
        pearlStrats.append(x)
        iceboxStrats.append(x)
        fractureStrats.append(x)
        bindStrats.append(x)
        breezeStrats.append(x)

# Functions
def selectFunc():
    runCmd("cls")
    print("ValoTools\n---------------------------\nSelect what you want to use.\n1. Random Loadout\n2. Random Agent\n3. Random Map (Custom Game)\n4. Random Strat\n")

    selectedFunc = input()

    return selectedFunc

def randStrat(): # Random Strat
    def actualRandStrat():
        runCmd("cls")
        print("\nWhat map are you on? First letter capital. (WARNING: RECOMMENDED TO HAVE A FIVE-STACK)\n")

        mapSelection = input()

        if mapSelection in allMaps:
            if str.lower(mapSelection) == str.lower(allMaps[0]): # Ascent
                for x in basicStrats:
                    runCmd("cls")
                    print("\n" + choice(ascentStrats))
                    anotherStrat(mapSelection)
            elif str.lower(mapSelection) == str.lower(allMaps[1]): # Haven
                for x in basicStrats:
                    runCmd("cls")
                    print("\n" + choice(havenStrats))
                    anotherStrat(mapSelection)
            elif str.lower(mapSelection) == str.lower(allMaps[2]): # Split
                for x in basicStrats:
                    runCmd("cls")
                    print("\n" + choice(splitStrats))
                    anotherStrat(mapSelection)
            elif str.lower(mapSelection) == str.lower(allMaps[3]): # Pearl
                for x in basicStrats:
                    runCmd("cls")
                    print("\n" + choice(pearlStrats))
                    anotherStrat(mapSelection)
            elif str.lower(mapSelection) == str.lower(allMaps[4]): # Icebox
                for x in basicStrats:
                    runCmd("cls")
                    print("\n" + choice(iceboxStrats))
                    anotherStrat(mapSelection)
            elif str.lower(mapSelection) == str.lower(allMaps[5]): # Fracture
                for x in basicStrats:
                    runCmd("cls")
                    print("\n" + choice(fractureStrats))
                    anotherStrat(mapSelection)
            elif str.lower(mapSelection) == str.lower(allMaps[6]): # Bind
                for x in basicStrats:
                    runCmd("cls")
                    print("\n" + choice(bindStrats))
                    anotherStrat(mapSelection)
            elif str.lower(mapSelection) == str.lower(allMaps[7]): # Breeze
                for x in basicStrats:
                    runCmd("cls")
                    print("\n" + choice(breezeStrats))
                    anotherStrat(mapSelection)
        else:
            print("Not a valid option.")
            actualRandStrat()
    
    def actualRandStratMapDetermined(mapSelected):
        if mapSelected == allMaps[0]: # Ascent
            for x in basicStrats:
                runCmd("cls")
                print("\n" + choice(ascentStrats))
                anotherStrat(mapSelected)
    
    def anotherStrat(mapSelected):
        print("\nWould you like another strat? (y/n)")
        extraStrat = input()

        if extraStrat == "y":
            actualRandStratMapDetermined(mapSelected)
        elif extraStrat == "n":
            textUInoAnim()
        else:
            print("\nNot a valid option.")
            input()
            anotherStrat(mapSelected)

    actualRandStrat()
            
def loadingAnim(): # Loading Animation when booting the text UI
    runCmd("cls")
    print("Running text-based ui...")
    wait(0.5)
    runCmd("cls")
    wait(0.1)

def textUI(): # Start text UI from UI selection menu
    loadingAnim()
    runCmd("title ValoTools")
    def getSelectedFunc():
        selectedFunc = selectFunc()

        if selectedFunc == "1": # Random Loadout
            print("\n" + choice(weapons) + " with " + choice(armorTypes) + " armor.\n")
            input()
            runCmd("cls")
            getSelectedFunc()
        elif selectedFunc == "2": # Random Agent
            print("\n" + choice(agents) + "\n")
            input()
            runCmd("cls")
            getSelectedFunc()
        elif selectedFunc == "3": # Random Map for Custom Games
            print("\n" + choice(allMaps) + "\n") # do maps thing
            input()
            runCmd("cls")
            getSelectedFunc()
        elif selectedFunc == "4": # Random Strat
            randStrat()
        else:
            print("\nNot a valid option.\n")
            input()
            runCmd("cls")
            getSelectedFunc()
    
    getSelectedFunc()

def textUInoAnim(): # Return to text UI from a different command
    runCmd("title ValoTools")
    def getSelectedFunc():
        selectedFunc = selectFunc()

        if selectedFunc == "1": # Random Loadout
            print("\n" + choice(weapons) + " with " + choice(armorTypes) + " armor.\n")
            input()
            runCmd("cls")
            getSelectedFunc()
        elif selectedFunc == "2": # Random Agent
            print("\n" + choice(agents) + "\n")
            input()
            runCmd("cls")
            getSelectedFunc()
        elif selectedFunc == "3": # Random Map for Custom Games
            print("\n" + choice(allMaps) + "\n") # do maps thing
            input()
            runCmd("cls")
            getSelectedFunc()
        elif selectedFunc == "4": # Random Strat
            randStrat()
        else:
            print("\nNot a valid option.\n")
            input()
            runCmd("cls")
            getSelectedFunc()
    
    getSelectedFunc()