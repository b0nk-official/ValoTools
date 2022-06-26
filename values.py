# Tables file for ValoTools

# Variables
versionNum = "1.2.1" # Master version number, changes values across every file

# Tables
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
allWeapons = [
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
    "Knife",
    "GoldenGun",
    "Headhunter",
    "TourDeForce",
    "OverdriveBeam"
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
weaponStats = {
    "Classic": {
        "fireMode": "Semi-Auto",
        "fireRate": "6.75 rounds per second",
        "runSpeed": "5.73 meters per second",
        "equipSpeed": "0.75 seconds",
        "firstShotAcc": "0.4 degrees",
        "reloadSpeed": "1.75 seconds",
        "magSize": "12 rounds per mag, 3 mags in reserve"
    },
    "GoldenGun": {
        "fireMode": "Semi-Auto",
        "fireRate": "3 rounds per second",
        "runSpeed": "7.4 meters per second",
        "equipSpeed": "0.67 seconds",
        "firstShotAcc": "0 degrees",
        "reloadSpeed": "No reload on gun",
        "magSize": "2 rounds per mag, 1 mag"
    },
    "OverdriveBeam": {
        "fireMode": "Full-Auto",
        "fireRate": "20 rounds per second",
        "runSpeed": "Linked to relative ultimate",
        "equipSpeed": "1 second initially, 0.333 seconds for re-equip",
        "firstShotAcc": "0 degrees",
        "reloadSpeed": "0.5 seconds after shooting you receive 1 ammo per 0.05 seconds",
        "magSize": "Linked to relative ultimate"
    },
    "TourDeForce": {
        "fireMode": "Semi-Auto",
        "fireRate": "1.2 rounds per second",
        "runSpeed": "5.13/5.4 meters per second",
        "equipSpeed": "0.67 seconds",
        "firstShotAcc": "0 degrees while aiming(?)",
        "reloadSpeed": "No reload on gun",
        "magSize": "5 rounds per mag, 1 mag"
    },
    "Headhunter": {
        "fireMode": "Semi-Auto",
        "fireRate": "6.75 rounds per second",
        "runSpeed": "5.73 meters per second",
        "equipSpeed": "0.75 seconds",
        "firstShotAcc": "No information found",
        "reloadSpeed": "No reload on gun",
        "magSize": "0-8 rounds per mag, 1 mag"
    },
    "Sheriff": {
        "fireMode": "Semi-Auto",
        "fireRate": "4 rounds per second",
        "runSpeed": "5.4 meters per second",
        "equipSpeed": "1 seconds",
        "firstShotAcc": "0.25 degrees",
        "reloadSpeed": "2.25 seconds",
        "magSize": "6 rounds per mag, 3 mags in reserve"
    },
    "Ghost": {
        "fireMode": "Semi-Auto",
        "fireRate": "6.75 rounds per second",
        "runSpeed": "5.73 meters per second",
        "equipSpeed": "0.75 seconds",
        "firstShotAcc": "0.4 degrees",
        "reloadSpeed": "1.5 seconds",
        "magSize": "15 rounds per mag, 3 mags in reserve"
    },
    "Shorty": {
        "fireMode": "Semi-Auto",
        "fireRate": "3.33 rounds per second",
        "runSpeed": "5.4 meters per second",
        "equipSpeed": "0.75 seconds",
        "firstShotAcc": "4 degrees",
        "reloadSpeed": "1.75 seconds",
        "magSize": "2 rounds per mag, 5 mags in reserve"
    },
    "Frenzy": {
        "fireMode": "Full-Auto",
        "fireRate": "10 rounds per second",
        "runSpeed": "5.73 meters per second",
        "equipSpeed": "1 second",
        "firstShotAcc": "0.45 degrees",
        "reloadSpeed": "1.5 seconds",
        "magSize": "13 rounds per mag, 3 mags in reserve"
    },
    "Stinger": {
        "fireMode": "Full-Auto",
        "fireRate": "16 rounds per second",
        "runSpeed": "5.73 meters per second",
        "equipSpeed": "0.75 seconds",
        "firstShotAcc": "0.65 degrees",
        "reloadSpeed": "2.25 seconds",
        "magSize": "20 rounds per mag, 3 mags in reserve"
    },
    "Spectre": {
        "fireMode": "Full-Auto",
        "fireRate": "13.33 rounds per second",
        "runSpeed": "5.73 meters per second",
        "equipSpeed": "0.75 seconds",
        "firstShotAcc": "0.4 degrees",
        "reloadSpeed": "2.25 seconds",
        "magSize": "30 rounds per mag, 3 mags in reserve"
    },
    "Bucky": {
        "fireMode": "Semi-Auto",
        "fireRate": "1.1 rounds per second",
        "runSpeed": "5.06 meters per second",
        "equipSpeed": "1 seconds",
        "firstShotAcc": "2.6 degrees",
        "reloadSpeed": "2.5 seconds",
        "magSize": "5 rounds per mag, 2 mags in reserve"
    },
    "Judge": {
        "fireMode": "Full-Auto",
        "fireRate": "3.5 rounds per second",
        "runSpeed": "5.06 meters per second",
        "equipSpeed": "1 seconds",
        "firstShotAcc": "2.25 degrees",
        "reloadSpeed": "2.2 seconds",
        "magSize": "7 rounds per mag, 3 mags in reserve"
    },
    "Bulldog": {
        "fireMode": "Full-Auto",
        "fireRate": "5.4 rounds per second",
        "runSpeed": "5.4 meters per second",
        "equipSpeed": "1 seconds",
        "firstShotAcc": "0.3 degrees",
        "reloadSpeed": "2.5 seconds",
        "magSize": "24 rounds per mag, 3 mags in reserve"
    },
    "Guardian": {
        "fireMode": "Semi-Auto",
        "fireRate": "5.25 rounds per second",
        "runSpeed": "5.4 meters per second",
        "equipSpeed": "1 seconds",
        "firstShotAcc": "0.1 degrees",
        "reloadSpeed": "2.5 seconds",
        "magSize": "12 rounds per mag, 3 mags in reserve"
    },
    "Phantom": {
        "fireMode": "Full-Auto",
        "fireRate": "11 rounds per second",
        "runSpeed": "5.4 meters per second",
        "equipSpeed": "1 seconds",
        "firstShotAcc": "0.2 degrees",
        "reloadSpeed": "2.5 seconds",
        "magSize": "30 rounds per mag, 3 mags in reserve"
    },
    "Vandal": {
        "fireMode": "Full-Auto",
        "fireRate": "9.75 rounds per second",
        "runSpeed": "5.4 meters per second",
        "equipSpeed": "1 seconds",
        "firstShotAcc": "0.25 degrees",
        "reloadSpeed": "2.5 seconds",
        "magSize": "25 rounds per mag, 3 mags in reserve"
    },
    "Marshal": {
        "fireMode": "Semi-Auto",
        "fireRate": "1.5 rounds per second",
        "runSpeed": "5.4 meters per second",
        "equipSpeed": "1.25 seconds",
        "firstShotAcc": "1 degree",
        "reloadSpeed": "2.5 seconds",
        "magSize": "5 rounds per mag, 3 mags in reserve"
    },
    "Operator": {
        "fireMode": "Semi-Auto",
        "fireRate": "0.6 rounds per second",
        "runSpeed": "5.13 meters per second",
        "equipSpeed": "1.5 seconds",
        "firstShotAcc": "5 degrees",
        "reloadSpeed": "3.7 seconds",
        "magSize": "5 rounds per mag, 2 mags in reserve"
    },
    "Ares": {
        "fireMode": "Full-Auto",
        "fireRate": "13 rounds per second",
        "runSpeed": "5.13 meters per second",
        "equipSpeed": "1.25 seconds",
        "firstShotAcc": "1 degree",
        "reloadSpeed": "3.25 seconds",
        "magSize": "50 rounds per mag, 2 mags in reserve"
    },
    "Odin": {
        "fireMode": "Full-Auto",
        "fireRate": "12-15.6 rounds per second",
        "runSpeed": "5.13 meters per second",
        "equipSpeed": "1.25 seconds",
        "firstShotAcc": "0.6 degrees",
        "reloadSpeed": "5 seconds",
        "magSize": "100 rounds per mag, 2 mags in reserve"
    },
    "Knife": {
        "fireMode": "Semi-Auto",
        "fireRate": "No information found",
        "runSpeed": "No information found",
        "equipSpeed": "No information found",
        "firstShotAcc": "Not applicable",
        "reloadSpeed": "Not applicable",
        "magSize": "Not applicable"
    }
}

# Functions
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

def getWeapons():
    return weapons, allWeapons
def getWeaponStats():
    return weaponStats
def getAgents():
    return agents
def getMaps ():
    return allMaps
def getArmorTypes():
    return armorTypes
def getBasicStrats():
    return basicStrats
def getAscentStrats():
    return ascentStrats
def getHavenStrats():
    return havenStrats
def getSplitStrats():
    return splitStrats
def getPearlStrats():
    return pearlStrats
def getIceboxStrats():
    return iceboxStrats
def getFractureStrats():
    return fractureStrats
def getBindStrats():
    return bindStrats
def getBreezeStrats():
    return breezeStrats

def getVersionNum():
    return versionNum