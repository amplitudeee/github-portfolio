# ---------------------------------------
# Title:    Marvel Rivals Tryout Form Creator
# Author:   Matt Salvadori
# Date:     July 26, 2025
# Purpose:  To create a neat form that randomly generates characters
# for applicant while giving potential for collecting information
# ---------------------------------------

#region IMPORTS
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from idlelib.tooltip import Hovertip
import random
#endregion

#region GLOBAL VARIABLES AND CONSTANTS
    #region CONSTATNTS and GLOBAL VARS
CUSTOM_TRYOUT_LABEL = "Marvel Rivals Tryout Submission Form"
VERSION = "0.1"

VANGUARDS = [
    "Bruce Banner",
    "Captain America",
    "Emma Frost",
    "Magneto",
    "Doctor Strange",
    "Peni Parker",
    "The Thing",
    "Groot",
    "Venom",
    "Thor"
]
DUELISTS = [
    "Wolverine",
    "Psylocke",
    "Black Panther",
    "Iron Man",
    "Squirrel Girl",
    "The Punisher",
    "Storm",
    "Phoenix",
    "Mr. Fantastic",
    "Winter Soldier",
    "Moon Knight",
    "Scarlet Witch",
    "Hela",
    "Hawkeye",
    "Namor",
    "Star-Lord",
    "Human Torch",
    "Magik",
    "Black Widow",
    "Spider-Man",
    "Iron Fist"
]
STRATEGISTS = [
    "Invisible Woman",
    "Loki",
    "Luna Snow",
    "Rocket Raccoon",
    "Mantis",
    "Ultron",
    "Adam Warlock",
    "Cloak & Dagger",
    "Jeff The Good Boy"
]
CHARACTER_CLASSES = ["Vanguard", "Duelist", "Strategist"]
RANKS = [
    "Bronze III", "Bronze II", "Bronze I",
    "Silver III", "Silver II", "Silver I",
    "Gold III", "Gold II", "Gold I",
    "Platinum III", "Platinum II", "Platinum I",
    "Diamond III", "Diamond II", "Diamond I",
    "Grandmaster III", "Grandmaster II", "Grandmaster I",
    "Celestial III", "Celestial II", "Celestial I",
    "Eternity",
    "One Above All"
]
    #endregion

    #region UI CONTROLS
window = tk.Tk()
lblName = tk.Label(window)
lblHandle = tk.Label(window)
lblRank = tk.Label(window)
lblClass = tk.Label(window)
lblRandomize = tk.Label(window)
lblChar1 = tk.Label(window)
lblChar2 = tk.Label(window)
lblChar3 = tk.Label(window)
txtName = tk.Entry(window)
txtHandle = tk.Entry(window)
cboRank = ttk.Combobox(window)
cboClass = ttk.Combobox(window)
btnGo = tk.Button(window)
lblChar1Out = tk.Label(window)
lblChar2Out = tk.Label(window)
lblChar3Out = tk.Label(window)
btnSubmit = tk.Button(window)
btnReset = tk.Button(window)

    #endregion

#endregion

#region FUNCTIONS
    #region EVENT HANDLERS
def btnGo_click():
    '''Go button characteristics'''
    chars = []
    #if class has been selected
    if isClassSelected():
        #generate 3 characters and put them in lbl slots
        while len(chars) < 3:
            charcheck = getRandChar()
            if charcheck not in chars:
                chars.append(charcheck)
        lblChar1Out.config(text=chars[0])
        lblChar2Out.config(text=chars[1])
        lblChar3Out.config(text=chars[2])

def btnSubmit_click():
    '''Submit Button characteristics'''
    #check if all input areas are filled out
    if isFilledOut():
        messagebox.showinfo("Success", "Your information has been successfully submitted!")
        lblChar1Out.config(text="")
        lblChar2Out.config(text="")
        lblChar3Out.config(text="")
        txtHandle.delete(0, 'end')
        txtName.delete(0, 'end')
        cboRank.set('')
        cboClass.set('')

def btnReset_click():
    '''Reset button characteristics'''
    lblChar1Out.config(text="")
    lblChar2Out.config(text="")
    lblChar3Out.config(text="")
    txtHandle.delete(0, 'end')
    txtName.delete(0, 'end')
    cboRank.set('')
    cboClass.set('')

def isFilledOut():
    '''Check if all entries have been made if not return error message'''
    checkName = txtName.get()
    if checkName == "":
        messagebox.showerror("Error", "You must input name")
        return False
    checkHandle = txtHandle.get()
    if checkHandle == "":
        messagebox.showerror("Error", "You must input handle")
        return False
    checkRank = cboRank.get()
    if checkRank == "":
        messagebox.showerror("Error", "You must select a rank")
        return False
    checkClass = cboClass.get()
    if checkClass == "":
        messagebox.showerror("Error", "You must select a class")
        return False
    if lblChar1Out.cget("text") =="":
        messagebox.showerror("Error", "You must get random scrim characters first")
        return False
    
    return True

def isClassSelected():
    '''Check if class is selected, if not return error messagebox'''
    #get text from cboClass
    check = cboClass.get()
    #if empty popout window error
    if check == "":
        messagebox.showerror("Error", "You must select a class first")
        return False
    return True

def getRandChar():
    '''Generate random character  based on cboClass box'''
    #get class string from cboClass
    selected_class = cboClass.get()
    if selected_class == "Vanguard":
        randChar = random.choice(VANGUARDS)
        return randChar
    elif selected_class == "Duelist":
        randChar = random.choice(DUELISTS)
        return randChar
    elif selected_class == "Strategist":
        randChar = random.choice(STRATEGISTS)
        return randChar

def escape_key():
    '''Display confirmation box if escape key pressed'''
    result = messagebox.askyesno("Quit Confirmation", "Are you sure you want to quit?")
    #quit if yes
    if result:
        window.quit()

def enter_key(event):
    '''bind enter key to invoke, or whatever it means ot click an object when highlighted with tab'''
    #store highlighted in variable
    focused = event.widget.focus_get()
    #if variable is button then invoke
    if isinstance(focused, tk.Button):
        focused.invoke()

    #endregion

    #region CUSTOM FUNCTIONS
def initializeUI():
    '''start your engines'''
    window.title(CUSTOM_TRYOUT_LABEL + " (" + VERSION + " )")
    window.geometry("356x144")

    #row 0
    lblName.config(text="Name:")
    lblName.grid(row=0, column=0, sticky="WE")
    txtName.config(width = 10)
    txtName.grid(row=0, column=1, sticky="WE")
    lblRandomize.config(text="Get Random Scrim Characters")
    lblRandomize.grid(row=0, column=2, columnspan=2, sticky="WE")
    btnGo.config(text="Go!", command=btnGo_click)
    btnGo.grid(row=0, column=4, sticky="E")

    #row 1
    lblHandle.config(text="Handle:")
    lblHandle.grid(row=1, column=0, sticky="WE")
    txtHandle.config(width = 10)
    txtHandle.grid(row=1, column=1, sticky="WE")
    lblChar1.config(text="Scrim Character 1:")
    lblChar1.grid(row=1, column=2, sticky="WE")
    lblChar1Out.config(bg="lightgrey", text="")
    lblChar1Out.grid(row=1, column=3, columnspan=2,sticky="WE")

    #row 2
    lblRank.config(text="Rank:")
    lblRank.grid(row=2, column=0, sticky="WE")
    cboRank.config(width=15)
    cboRank['values'] = (RANKS)
    cboRank.grid(row=2, column=1, sticky="WE")
    lblChar2.config(text="Scrim Character 2:")
    lblChar2.grid(row=2, column=2, sticky="WE")
    lblChar2Out.config(bg="lightgrey", text="")
    lblChar2Out.grid(row=2, column=3, columnspan=2, sticky="WE")
    
    #row 3
    lblClass.config(text="Class:")
    lblClass.grid(row=3, column=0, sticky="WE")
    cboClass.config(width=15)
    cboClass['values'] = (CHARACTER_CLASSES)
    cboClass.grid(row=3, column=1, sticky="WE")
    lblChar3.config(text="Scrim Character 3:")
    lblChar3.grid(row=3, column=2, sticky="WE")
    lblChar3Out.config(bg="lightgrey", text="")
    lblChar3Out.grid(row=3, column=3, columnspan=2, sticky="WE")

    #row 4
    btnSubmit.config(text="Submit", command=btnSubmit_click)
    btnSubmit.grid(row=4, column=0, columnspan=5, sticky="WE")

    #row 5
    btnReset.config(text="Reset", command=btnReset_click)
    btnReset.grid(row=5, column=0, columnspan=5, sticky="WE")

    #AODA
    Hovertip(txtName, "Enter your full name")
    Hovertip(txtHandle, "Enter your in game name")
    Hovertip(cboRank, "Select your rank")
    Hovertip(cboClass, "Select your class")
    Hovertip(btnGo, "Get random scrim characters")
    Hovertip(btnReset, "Reset form")
    Hovertip(btnSubmit, "Submit your information")

    #Key Binds
    window.bind("<Escape>", lambda event: escape_key())
    window.bind("<Return>", enter_key)

    #endregion
#endregion

#region MAIN PROGRAM
initializeUI()
window.mainloop()

#endregion