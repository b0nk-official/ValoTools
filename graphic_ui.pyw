# Graphical User Interface for ValoTools

# Imports
import tkinter as tk
import values
from random import choice
from time import sleep as wait

# Variables
versionNum = values.getVersionNum()
armorTypes = values.getArmorTypes()
weapons, allWeapons = values.getWeapons()
agents = values.getAgents()
allMaps = values.getMaps()

# Window
window = tk.Tk()
window.geometry("800x400")
window.title("ValoTools - Main Menu")
window.configure(bg="#1a1a1a")
window.iconbitmap("valotoolsicon.ico")
window.resizable(False, False)

# Widgets
versionLabelText = "Version: " + versionNum
versionLabel = tk.Label(text=versionLabelText, fg="#ff6161", bg="#1a1a1a", anchor=tk.CENTER, width=20, font="Helvetica 10")
versionLabel.place(x=297, y=380)

randomLoadoutLabelText = tk.StringVar()
randomLoadoutLabelText.set("")
randomLoadoutLabel = tk.Label(textvariable=randomLoadoutLabelText, bg="#1a1a1a", fg="#ff6161", anchor=tk.CENTER, width=27, height=1)

def randomLoadoutFunc():
    randomLoadoutLabelText.set(choice(weapons) + " with " + choice(armorTypes) + " armor.")

randomLoadout = tk.Button(text="Random Loadout", width=25, height=3, bg="#ff6161", fg="#1a1a1a", borderwidth=0, font="Helvetica 10 bold", command=randomLoadoutFunc)

randomAgentLabelText = tk.StringVar()
randomAgentLabelText.set("")
randomAgentLabel = tk.Label(textvariable=randomAgentLabelText, bg="#1a1a1a", fg="#ff6161", anchor=tk.CENTER, width=27, height=1)

def randomAgentFunc():
    randomAgentLabelText.set(choice(agents))

randomAgent = tk.Button(text="Random Agent", width=25, height=3, bg="#ff6161", fg="#1a1a1a", borderwidth=0, font="Helvetica 10 bold", command=randomAgentFunc)

randomMapLabelText = tk.StringVar()
randomMapLabelText.set("")
randomMapLabel = tk.Label(textvariable=randomMapLabelText, bg="#1a1a1a", fg="#ff6161", anchor=tk.CENTER, width=27, height=1)

def randomMapFunc():
    randomMapLabelText.set(choice(allMaps))

randomMap = tk.Button(text="Random Map", width=25, height=3, bg="#ff6161", fg="#1a1a1a", borderwidth=0, font="Helvetica 10 bold", command=randomMapFunc)

stratGen = tk.Button(text="Random Strat", width=30, height=18, bg="#ff6161", fg="#1a1a1a", borderwidth=0, font="Helvetica 10 bold")

wepStats = tk.Button(text="Weapon Stats", width=30, height=18, bg="#ff6161", fg="#1a1a1a", borderwidth=0, font="Helvetica 10 bold")

def mainMenuPageShow(): # Show everything in the main menu page
    wepStats.place(x=530, y=30)
    stratGen.place(x=260, y=30)
    randomMapLabel.place(x=38, y=325)
    randomMap.place(x=30, y=270)
    randomAgentLabel.place(x=38, y=205)
    randomAgent.place(x=30, y=150)
    randomLoadout.place(x=30, y=30)
    randomLoadoutLabel.place(x=38, y=85)
def mainMenuPageHide(): # Hide everything in the main menu page
    wepStats.place_forget()
    stratGen.place_forget()
    randomMapLabel.place_forget()
    randomMap.place_forget()
    randomAgentLabel.place_forget()
    randomAgent.place_forget()
    randomLoadout.place_forget()
    randomLoadoutLabel.place_forget()

backButton = tk.Button(text="<", width=5, height=2, bg="#ff6161", fg="#1a1a1a", borderwidth=0, font="Helvetica 10 bold")

def weaponStatsPageShow(): # Show everything in the weapon stats page
    backButton.place(x=10, y=350)
def weaponStatsPageHide():
    backButton.place_forget()

def wepStatsFunc():
    mainMenuPageHide()
    weaponStatsPageShow()

def backToMenu():
    weaponStatsPageHide()
    mainMenuPageShow()

# End
backButton.configure(command=backToMenu)
wepStats.configure(command=wepStatsFunc)

mainMenuPageShow()

window.mainloop()