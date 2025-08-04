# ------------------------------
# COSC1100 - Assignment 3 Dnd Chars
# Matt Salvadori
# July 24, 2025
# Calculator Applications
#-------------------------------

'''Everything looks cool, and efficient and looks coolio.'''
#region IMPORTS
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from idlelib.tooltip import Hovertip
#endregion

#region CONSTANTS AND CONTROLS
    #region CONSTANTS AND GLOBAL VARS
TITLE = "DND Character Customization"
VERSION = "0.1"
SPECIES = ["Aasimar","Dragonborn","Dwarf","Elf","Gnome",
    "Goliath","Halfling","Human","Orc","Tiefling"]

CLASSES = ["Barbarian","Bard","Cleric","Druid","Fighter","Monk",
    "Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"]
MINUS = "-"
PLUS = "+"
MIN_STAT = "8"
MIN_COST = "1"
MAXPOINTS = 27
CHARACTERNAMEINDEX = 0
PLAYERNAMEINDEX = 1
CLASSINDEX = 2
SPECIESINDEX = 3
STRENGTHINDEX = 4
DEXTERITYINDEX = 5
CONSTITUTIONINDEX = 6
INTELLECTINDEX = 7
WISDOMINDEX = 8
CHARISMAINDEX = 9
STRENGTHCOSTINDEX = 10
DEXTERITYCOSTINDEX = 11
CONSTITUTIONCOSTINDEX = 12
INTELLECTCOSTINDEX = 13
WISDOMCOSTINDEX = 14
CHARISMACOSTINDEX = 15
UNUSEDSKILLPOINTS = 16
FRESHPROFILE = ["","","","",MIN_STAT,MIN_STAT,MIN_STAT,MIN_STAT,MIN_STAT,MIN_STAT,MIN_COST,MIN_COST,MIN_COST,MIN_COST,MIN_COST,MIN_COST,MAXPOINTS]

characters = []
limbo_profile = FRESHPROFILE
loaded_profile = ["","","","",MIN_STAT,MIN_STAT,MIN_STAT,MIN_STAT,MIN_STAT,MIN_STAT,MIN_COST,MIN_COST,MIN_COST,MIN_COST,MIN_COST,MIN_COST,MAXPOINTS]

    #endregion
    #region UI CONTROLS
window = tk.Tk()
txtCharName = tk.Entry(window)
txtName = tk.Entry(window)
cboClass = ttk.Combobox(window)
cboSpecies = ttk.Combobox(window)
btnStrM = tk.Button(window)
btnStrA = tk.Button(window)
btnDexM = tk.Button(window)
btnDexA = tk.Button(window)
btnConstM = tk.Button(window)
btnConstA = tk.Button(window)
btnIntM = tk.Button(window)
btnIntA = tk.Button(window)
btnWisdomM = tk.Button(window)
btnWisdomA = tk.Button(window)
btnRizzM = tk.Button(window)
btnRizzA = tk.Button(window)
btnResetAttr = tk.Button(window)
btnSave = tk.Button(window)
btnCancel = tk.Button(window)
btnNew = tk.Button(window)
lbxCharacters = tk.Listbox(window, width=15, height=13)
btnEdit = tk.Button(window)
btnDelete = tk.Button(window)
lblName = tk.Label(window)
lblCharName = tk.Label(window)
lblClass = tk.Label(window)
lblSpecies = tk.Label(window)
lblStr = tk.Label(window)
lblDex = tk.Label(window)
lblConst = tk.Label(window)
lblInt = tk.Label(window)
lblWisdom = tk.Label(window)
lblRizz = tk.Label(window)
lblClvl = tk.Label(window)
lblptStr = tk.Label(window)
lblptDex = tk.Label(window)
lblptConst = tk.Label(window)
lblptInt = tk.Label(window)
lblptWisdom = tk.Label(window)
lblptRizz = tk.Label(window)
lblptReq = tk.Label(window)
lblreqStr = tk.Label(window)
lblreqDex = tk.Label(window)
lblreqConst = tk.Label(window)
lblreqInt = tk.Label(window)
lblreqWisdom = tk.Label(window)
lblreqRizz = tk.Label(window)
lblSPAvail = tk.Label(window)
lblBaseSP = tk.Label(window)

    #endregion

#endregion

#region FUNCTIONS
    #region EVENT HANDLERS
def guiUpdateAll(colour: str = "black"):
    '''Update entire GUI interface'''
    for i in range(len(limbo_profile)):
        guiUpdate(i)
        changeColor(i, colour)

def changeColor(index, bgColour):
    '''Change colour of guide text'''
    if index == 4:
        lblptStr.config(fg=bgColour)
        lblreqStr.config(fg=bgColour)
        lblSPAvail.config(fg=bgColour)
    if index == 5:
        lblptDex.config(fg=bgColour)
        lblreqDex.config(fg=bgColour)
        lblSPAvail.config(fg=bgColour)
    if index == 6:
        lblptConst.config(fg=bgColour)
        lblreqConst.config(fg=bgColour)
        lblSPAvail.config(fg=bgColour)
    if index == 7:
        lblptInt.config(fg=bgColour)
        lblreqInt.config(fg=bgColour)
        lblSPAvail.config(fg=bgColour)
    if index == 8:
        lblptWisdom.config(fg=bgColour)
        lblreqWisdom.config(fg=bgColour)
        lblSPAvail.config(fg=bgColour)
    if index == 9:
        lblptRizz.config(fg=bgColour)
        lblreqRizz.config(fg=bgColour)
        lblSPAvail.config(fg=bgColour)
    if index == 16:
        lblSPAvail.config(fg=bgColour)

def guiUpdate(index):
    '''Update GUI profile by index number'''
    global limbo_profile
    if index == 0:
        txtCharName.delete(0, tk.END)
        txtCharName.insert(0, limbo_profile[CHARACTERNAMEINDEX])
    if index == 1:
        txtName.delete(0, tk.END)
        txtName.insert(0, limbo_profile[PLAYERNAMEINDEX]) 
    if index == 2:
        cboClass.set(limbo_profile[CLASSINDEX])
    if index == 3:
        cboSpecies.set(limbo_profile[SPECIESINDEX])
    if index == 4:
        lblptStr.config(text=limbo_profile[STRENGTHINDEX])
    if index == 5:
        lblptDex.config(text=limbo_profile[DEXTERITYINDEX])
    if index == 6:
        lblptConst.config(text=limbo_profile[CONSTITUTIONINDEX])
    if index == 7:
        lblptInt.config(text=limbo_profile[INTELLECTINDEX])
    if index == 8:
        lblptWisdom.config(text=limbo_profile[WISDOMINDEX])
    if index == 9:
        lblptRizz.config(text=limbo_profile[CHARISMAINDEX])
    if index == 10:
        lblreqStr.config(text=limbo_profile[STRENGTHCOSTINDEX])
    if index == 11:
        lblreqDex.config(text=limbo_profile[DEXTERITYCOSTINDEX])
    if index == 12:
        lblreqConst.config(text=limbo_profile[CONSTITUTIONCOSTINDEX])
    if index == 13:
        lblreqInt.config(text=limbo_profile[INTELLECTCOSTINDEX])
    if index == 14:
        lblreqWisdom.config(text=limbo_profile[WISDOMCOSTINDEX])
    if index == 15:
        lblreqRizz.config(text=limbo_profile[CHARISMACOSTINDEX])
    if index == 16:
        lblSPAvail.config(text=limbo_profile[UNUSEDSKILLPOINTS])

def sort_listbox():
    '''Sort Listbox'''
    items = lbxCharacters.get(0, tk.END)
    items = sorted(items)                    
    lbxCharacters.delete(0, tk.END)    
    for item in items:                    
        lbxCharacters.insert(tk.END, item)
    characters.sort()

def skillPointUpdate(index, skillPoints):
    '''Update skillpoint labels based on + or - function'''
    if index == STRENGTHINDEX:
        lblptStr.config(text=limbo_profile[index])
        limbo_profile[STRENGTHCOSTINDEX] = skillPoints
        lblreqStr.config(text=skillPoints)
        lblSPAvail.config(text=limbo_profile[UNUSEDSKILLPOINTS])
    if index == DEXTERITYINDEX:
        lblptDex.config(text=limbo_profile[index])
        limbo_profile[DEXTERITYCOSTINDEX] = skillPoints
        lblreqDex.config(text=skillPoints)
        lblSPAvail.config(text=limbo_profile[UNUSEDSKILLPOINTS])
    if index == CONSTITUTIONINDEX:
        lblptConst.config(text=limbo_profile[index])
        limbo_profile[CONSTITUTIONCOSTINDEX] = skillPoints
        lblreqConst.config(text=skillPoints)
        lblSPAvail.config(text=limbo_profile[UNUSEDSKILLPOINTS])
    if index == INTELLECTINDEX:
        lblptInt.config(text=limbo_profile[index])
        limbo_profile[INTELLECTCOSTINDEX] = skillPoints
        lblreqInt.config(text=skillPoints)
        lblSPAvail.config(text=limbo_profile[UNUSEDSKILLPOINTS])
    if index == WISDOMINDEX:
        lblptWisdom.config(text=limbo_profile[index])
        limbo_profile[WISDOMCOSTINDEX] = skillPoints
        lblreqWisdom.config(text=skillPoints)
        lblSPAvail.config(text=limbo_profile[UNUSEDSKILLPOINTS])
    if index == CHARISMAINDEX:
        lblptRizz.config(text=limbo_profile[index])
        limbo_profile[CHARISMACOSTINDEX] = skillPoints
        lblreqRizz.config(text=skillPoints)
        lblSPAvail.config(text=limbo_profile[UNUSEDSKILLPOINTS])

def skillPointsRequired(nextLevel):
    '''Determine skill points required to get to next attribute level'''
    if nextLevel >= 8 and nextLevel <= 13:
        return 1
    elif nextLevel >= 14 and nextLevel <=15:
        return 2
    elif nextLevel == 16:
        return 9999999

def btnPlus_click(index):
    '''Plus button event handler, update limbo profile array and listbox'''
    current_level = int(limbo_profile[index])    # make current level at atrribute index an int
    next_level = current_level + 1                  # determine the next level
    next_next_level = current_level + 2
    skill_points_upgrade_cost = skillPointsRequired(next_level)   # use the next level to determine the cost of the upgrade
    skill_points_next_upgrade_cost = skillPointsRequired(next_next_level)
    skill_points_available = int(limbo_profile[UNUSEDSKILLPOINTS])      # retrieve skill points available
    if skill_points_available >= skill_points_upgrade_cost:        # upgrade skill points if skill points available
        limbo_profile[index] = str(int(limbo_profile[index]) + 1) # upgrade level
        limbo_profile[UNUSEDSKILLPOINTS] = str(int(limbo_profile[UNUSEDSKILLPOINTS]) - skill_points_upgrade_cost) # take from unused skill points
        skillPointUpdate(index, skill_points_next_upgrade_cost)        # update GUI
        changeColor(index, "darkblue")

def btnMinus_click(index):
    '''Minus button event handler, update limbo profile array and listbox'''
    current_level = int(limbo_profile[index])       # make current level at atrribute index an int
    previous_level = current_level - 1                    # determine the previous level
    skill_points = skillPointsRequired(previous_level)   # use the previous level to determine the cost of the downgrade
    if current_level > 8:                            # upgrade skill points if skill points available
        limbo_profile[index] = str(int(limbo_profile[index]) - 1) # downgrade level
        limbo_profile[UNUSEDSKILLPOINTS] = str(int(limbo_profile[UNUSEDSKILLPOINTS]) + skillPointsRequired(current_level)) # take from unused skill points
        skillPointUpdate(index, skill_points)
        changeColor(index, "darkblue")

def btnResetAttr_click():
    '''Reset attribute points to default for limbo profile'''
    limbo_profile[UNUSEDSKILLPOINTS] = MAXPOINTS
    for i in range(4, 10):
        limbo_profile[i] = MIN_STAT
        skillPointUpdate(i, MIN_COST)

def btnEdit_click():
    '''Open highlighted character'''
    global limbo_profile
    global loaded_profile
    selected_index = lbxCharacters.curselection()
    limbo_profile = characters[selected_index[0]]
    loaded_profile = characters[selected_index[0]]
    lbxCharacters.delete(selected_index)
    characters.pop(selected_index[0])
    sort_listbox()
    guiUpdateAll()

def btnDelete_click():
    '''Delete highlighted character'''
    global limbo_profile
    selected_index = lbxCharacters.curselection()
    if messagebox.askquestion("Delete Character", "Are you sure you wish to delete this character?") == 'yes':
        lbxCharacters.delete(selected_index)
        characters.pop(selected_index[0])
        sort_listbox()

def btnCancelChanges_click():
    '''Cancel recent changes to loaded profile'''
    global limbo_profile
    global loaded_profile
    if loaded_profile != limbo_profile:
        if messagebox.askquestion("Cancel Changes", "Are you sure you wish to cancel changes?") == 'yes':
            limbo_profile = loaded_profile.copy()
            guiUpdateAll()

def btnNewProfile_click():
    '''Erase current loaded profile and start from default settings'''
    for i in range(0, 3):
        limbo_profile[i] = ""
    btnResetAttr_click()

def btnSave_click():
    '''Save current limbo profile to listbox'''
    if isSavePossible():
        limbo_profile=[txtCharName.get(), txtName.get(), cboClass.get(), cboSpecies.get(), lblptStr.cget("text"), lblptDex.cget("text"), lblptConst.cget("text"), lblptInt.cget("text"), lblptWisdom.cget("text"), lblptRizz.cget("text"),lblreqStr.cget("text"), lblreqDex.cget("text"), lblreqConst.cget("text"), lblreqInt.cget("text"), lblreqWisdom.cget("text"), lblreqRizz.cget("text"), lblSPAvail.cget("text")]
        # add save query to main array
        characters.append(limbo_profile)
        lbxCharacters.insert(tk.END, limbo_profile[0])
        sort_listbox()
        btnNewProfile_click()
        guiUpdateAll()

def isSavePossible():
    '''Check if listbox has matching character profile'''
    try:
        limbo_profile=[txtCharName.get(), txtName.get(), cboClass.get(), cboSpecies.get(), lblptStr.cget("text"), lblptDex.cget("text"), lblptConst.cget("text"), lblptInt.cget("text"), lblptWisdom.cget("text"), lblptRizz.cget("text"),lblreqStr.cget("text"), lblreqDex.cget("text"), lblreqConst.cget("text"), lblreqInt.cget("text"), lblreqWisdom.cget("text"), lblreqRizz.cget("text"),lblSPAvail.cget("text")]
        if limbo_profile[CHARACTERNAMEINDEX] == '' or limbo_profile[PLAYERNAMEINDEX] == '' or limbo_profile[CLASSINDEX] == '' or limbo_profile[SPECIESINDEX] == '':
            messagebox.showerror("Empty Field", "You must fill out all fields")
            raise ValueError
        
        for char in characters:
            if txtCharName.get() == char[0]:
                messagebox.showerror("Character Exists", "Character Name Already Exists")
                raise ValueError
        return True
    except ValueError as v:
        return False

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
    '''Run da program broda'''

    window.title(TITLE + " (" + VERSION + ") ")
    # window.geometry("490x300")
    window.geometry("520x305")

    #column0
    lbxCharacters.grid(row=0, column=0, rowspan=11, columnspan=2, padx=5, sticky="nsew")
    btnEdit.config(text="EDIT", command=btnEdit_click)
    btnEdit.grid(row=12, column=0, padx=5, sticky="WE")
    btnDelete.config(text="DELETE", command=btnDelete_click)
    btnDelete.grid(row=12, column=1, padx=5, sticky="WE")   

    #column2
    lblCharName.config(text="Character Name")
    lblCharName.grid(row=0, column=2, sticky="E")
    lblName.config(text="Player Name")
    lblName.grid(row=1, column=2, sticky="E")
    lblClass.config(text="Class")
    lblClass.grid(row=2, column=2, sticky="E")
    lblSpecies.config(text="Species")
    lblSpecies.grid(row=3, column=2, sticky="E")
    lblStr.config(text="Strength")
    lblStr.grid(row=5, column=2, sticky="E")
    lblDex.config(text="Dexterity")
    lblDex.grid(row=6, column=2, sticky="E")
    lblConst.config(text="Constitution")
    lblConst.grid(row=7, column=2, sticky="E")
    lblInt.config(text="Intellect")
    lblInt.grid(row=8, column=2, sticky="E")
    lblWisdom.config(text="Wisdom")
    lblWisdom.grid(row=9, column=2, sticky="E")
    lblRizz.config(text="Charisma")
    lblRizz.grid(row=10, column=2, sticky="E")
    btnSave.config(text="SAVE CHANGES", command=btnSave_click)
    btnSave.grid(row=12, column=2, columnspan=4, padx=10, pady=10, sticky="WE")   


    #column3
    lblClvl.config(text="Attribute Level")
    lblClvl.grid(row=4, column=3, columnspan=3, sticky="WE")

    #column4
    txtCharName.config(width=10)
    txtCharName.grid(row=0, column=4, columnspan=7, sticky="WE")
    txtName.config(width=10)
    txtName.grid(row=1, column=4, columnspan=7, sticky="WE")
    cboClass.config(width=10)
    cboClass['values'] = (CLASSES)
    cboClass.grid(row=2, column=4, sticky="WE")
    cboSpecies.config(width = 10)
    cboSpecies['values'] = (SPECIES)
    cboSpecies.grid(row=3, column=4, sticky="WE")
    lblptStr.config(bg='lightgrey', text=limbo_profile[STRENGTHINDEX])
    lblptStr.grid(row=5, column=4)
    lblptDex.config(bg='lightgrey', text=limbo_profile[DEXTERITYINDEX])
    lblptDex.grid(row=6, column=4)
    lblptConst.config(bg='lightgrey', text=limbo_profile[CONSTITUTIONINDEX])
    lblptConst.grid(row=7, column=4)
    lblptInt.config(bg='lightgrey', text=limbo_profile[INTELLECTINDEX])
    lblptInt.grid(row=8, column=4)
    lblptWisdom.config(bg='lightgrey', text=limbo_profile[WISDOMINDEX])
    lblptWisdom.grid(row=9, column=4)
    lblptRizz.config(bg='lightgrey', text=limbo_profile[CHARISMAINDEX])
    lblptRizz.grid(row=10, column=4)

    #column6
    lblptReq.config(text="Upgrade Cost")
    lblptReq.grid(row=4, column=5, columnspan=3, sticky="WE")
    btnCancel.config(text="CANCEL CHANGES", padx=10, command=btnCancelChanges_click)
    btnCancel.grid(row=12, column=6, columnspan=6, padx=10, sticky="WE")

    #column7
    lblreqStr.config(bg='lightgrey', text=MIN_COST)
    lblreqStr.grid(row=5, column=6)
    lblreqDex.config(bg='lightgrey', text=MIN_COST)
    lblreqDex.grid(row=6, column=6)
    lblreqConst.config(bg='lightgrey', text=MIN_COST)
    lblreqConst.grid(row=7, column=6)
    lblreqInt.config(bg='lightgrey', text=MIN_COST)
    lblreqInt.grid(row=8, column=6)
    lblreqWisdom.config(bg='lightgrey', text=MIN_COST)
    lblreqWisdom.grid(row=9, column=6)
    lblreqRizz.config(bg='lightgrey', text=MIN_COST)
    lblreqRizz.grid(row=10, column=6)

    #column9
    btnStrM.config(text=MINUS, command=lambda: btnMinus_click(STRENGTHINDEX))
    btnStrM.grid(row=5, column=9, sticky="E")
    btnDexM.config(text=MINUS, command=lambda: btnMinus_click(DEXTERITYINDEX))
    btnDexM.grid(row=6, column=9, sticky="E")
    btnConstM.config(text=MINUS, command=lambda: btnMinus_click(CONSTITUTIONINDEX))
    btnConstM.grid(row=7, column=9, sticky="E")
    btnIntM.config(text=MINUS, command=lambda: btnMinus_click(INTELLECTINDEX))
    btnIntM.grid(row=8, column=9, sticky="E")
    btnWisdomM.config(text=MINUS, command=lambda: btnMinus_click(WISDOMINDEX))
    btnWisdomM.grid(row=9, column=9, sticky="E")
    btnRizzM.config(text=MINUS, command=lambda: btnMinus_click(CHARISMAINDEX))
    btnRizzM.grid(row=10, column=9, sticky="E")

    #column10
    btnStrA.config(text=PLUS, command=lambda: btnPlus_click(STRENGTHINDEX))
    btnStrA.grid(row=5, column=10, sticky="E")
    btnDexA.config(text=PLUS, command=lambda: btnPlus_click(DEXTERITYINDEX))
    btnDexA.grid(row=6, column=10, sticky="E")
    btnConstA.config(text=PLUS, command=lambda: btnPlus_click(CONSTITUTIONINDEX))
    btnConstA.grid(row=7, column=10, sticky="E")
    btnIntA.config(text=PLUS, command=lambda: btnPlus_click(INTELLECTINDEX))
    btnIntA.grid(row=8, column=10, sticky="E")
    btnWisdomA.config(text=PLUS, command=lambda: btnPlus_click(WISDOMINDEX))
    btnWisdomA.grid(row=9, column=10, sticky="E")
    btnRizzA.config(text=PLUS, command=lambda: btnPlus_click(CHARISMAINDEX))
    btnRizzA.grid(row=10, column=10, sticky="E")
    
    #column11
    btnNew.config(text="NEW", command=btnNewProfile_click)
    btnNew.grid(row=0, column=11, columnspan=1, padx=10, sticky="WE")
    lblSPAvail.config(text=limbo_profile[UNUSEDSKILLPOINTS], bg='lightgrey')
    lblSPAvail.grid(row=4, column=11, columnspan=1, padx=10, sticky="WE")
    lblBaseSP.config(text="Available Skill Points")
    lblBaseSP.grid(row=3, column=11, columnspan=1, padx=10, sticky="WE")
    btnResetAttr.config(text="Reset \nAttributes", command=btnResetAttr_click)
    btnResetAttr.grid(row=5, column=11, rowspan=6, padx=10, sticky="NSWE")    

    #AODA
    Hovertip(txtName, "Please enter your name.")
    Hovertip(txtCharName, "Please enter your character name.")
    Hovertip(cboClass, "Please select your class.")
    Hovertip(cboSpecies, "Please select your species.")
    Hovertip(btnEdit, "Edit existing character file.")
    Hovertip(btnDelete, "Delete selected character file.")
    Hovertip(btnSave, "Save all changes to character file.")
    Hovertip(btnCancel, "Cancel changes to character file.")
    Hovertip(btnResetAttr, "Reset all attributes.")
    Hovertip(btnStrM, "Decrease Strength Point.")
    Hovertip(btnStrA, "Increase Strength Point.")
    Hovertip(btnDexM, "Decrease Dexterity Point.")
    Hovertip(btnDexA, "Increase Dexterity Point.")
    Hovertip(btnConstM, "Decrease Constitution Point.")
    Hovertip(btnConstA, "Increase Constitution Point.")
    Hovertip(btnIntM, "Decrease Intellect Point.")
    Hovertip(btnIntA, "Increase Intellect Point.")
    Hovertip(btnNew, "Create New Character File")
    Hovertip(btnWisdomM, "Decrease Wisdom Point.")
    Hovertip(btnWisdomA, "Increase Wisdom Point.")
    Hovertip(btnRizzM, "Decrease Charisma Point.")
    Hovertip(btnRizzA, "Increase Charisma Point.")

    #KEY BINDS
    window.bind("<Escape>", lambda event: escape_key())
    window.bind("<Return>", enter_key)

def main():
    '''Main it up'''
    initializeUI()
    window.mainloop()
    #endregion
#endregion

#region MAIN PROGRAM
main()
exit()
#endregion



