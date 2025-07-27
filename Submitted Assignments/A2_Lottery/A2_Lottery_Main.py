#-----------------------------------------------
# Title:            Lottery Project
# Author:           Matt Salvadori
# Date:             July 18, 2025
# Purpose:          To check lottery tickets for 
#                   winning sets and print prize money if won
# ----------------------------------------------

# IDFIIPO IMPORTS, DECLARATIONS, FUNCTIONS, I, INPUT, PROCESS, OUTPUT
#region IMPORTS
import A2_tools

#endregion

#region DECLARATIONS
USER_GREETING = '''
--------------------------------------------------

HELLO, WELCOME TO BIG 7's GAMBLING ADDICTION PROGRAM
'''
MENU = '''--------------------------------------------------
1. 2x Random Set, 1 Manual Set
2. 3x Random Set
--------------------------------------------------'''
WINNERMENU = '''--------------------------------------------------
1. Manual Winning Set
2. Random Winning Set
--------------------------------------------------'''
PRIZECHART = '''
-------------------------------------------------------------------------------------
|   # of Matches  | # of Winners in Category |           Prize Amount           '''


#region CONSTANTS
MIN_ROLL_NUM = 1
MAX_ROLL_NUM = 50
TICKET_PRICE = 5
JACKPOT_PERCENTAGE = 0.85
SIX_MATCH_PERCENTAGE = 0.05
FIVE_MATCH_PERCENTAGE = 0.05
FOUR_MATCH_PRIZE = 20
MIN_TICKET_COUNT = 1000000
MAX_TICKET_COUNT = 40000000
ticketCarry = 0

#endregion

#region FUNCTIONS
def getManualLine(prompt: str, minLen: int, maxLen: int):
    '''Get 7 numbers from user without duplicates'''
    line3 = [0]
    while len(line3) < 8:
        try:
            rollcheck = A2_tools.getIntRange(prompt, minLen, maxLen)
            if rollcheck in line3:
                raise ValueError
            else:    
                line3.append(rollcheck)
            
        except ValueError as v:
            print(line3)
            print("Number already exists in set, please enter a different number.")

    return line3

def genRandLine():
    '''Generate 7 random numbers and return an array with a zero at the beginning'''
    line = [0]
    while len(line) < 8:
        rollcheck = A2_tools.getRandIntRange(MIN_ROLL_NUM, MAX_ROLL_NUM)
        if rollcheck not in line:
            line.append(rollcheck)
    return line

def printTicket():
    '''Consolidate and print ticket'''
    lines.append(line1)
    lines.append(line2)
    lines.append(line3)
    print("-"*50)
    print("Added: ")
    print(line1)
    print(line2)
    print(line3)
    print("-"*50)

def printEntries():
    '''Print all tickets entered'''
    print("-"*50)
    print("All entries: ")
    for i in lines:
        print(i)
    print("-"*50)

def getWinningSet(selection):
    '''Generate winning numbers'''
    if selection == 1:
        winner = getManualLine("Please enter a number between 1-50: ", MIN_ROLL_NUM, MAX_ROLL_NUM)
    elif selection == 2:
        winner = genRandLine()
    return winner

def compareSets(lines,winning_set):
    '''Compare each number at like index numbers, then add 1 to the sets counter'''
    # iterate through each line
    for i in range(len(lines)):
        for num in winning_set[1:]:
            if num in lines[i]:
                lines[i][0] += 1
        if lines[i][0] > 2:
            print("Winning Ticket !")
        else:
            print("Losing Ticket :(")

def countWinners(lines):
    '''Calculate Winners in each category'''
    seven_check = 0
    six_check = 0
    five_check = 0
    four_check = 0
    three_check = 0
    for i in range(len(lines)):
        if lines[i][0] == 7:
            seven_check += 1
            continue
        
        elif lines[i][0] == 6:
            six_check += 1
            continue

        elif lines[i][0] == 5:
            five_check += 1
            continue

        elif lines[i][0] == 4:
            four_check += 1
            continue

        elif lines[i][0] == 3:
            three_check += 1
            continue
    # return array with winners from each pize pool
    winners = [seven_check, six_check, five_check, four_check, three_check]
    return winners

def countPrizeMoney(ticketsSold):
    '''Calculate prize money'''
    totalPot = ticketsSold * TICKET_PRICE
    sevenPrize = totalPot * JACKPOT_PERCENTAGE
    sixPrize = totalPot * SIX_MATCH_PERCENTAGE
    fivePrize = totalPot * FIVE_MATCH_PERCENTAGE
    fourPrize = FOUR_MATCH_PRIZE
    threePrize = TICKET_PRICE

    return [sevenPrize, sixPrize, fivePrize, fourPrize, threePrize]

def printChart(winner):
    '''Print Winning Chart'''
    for i in range(len(winner)):
        chart_pos = 7 - i
        if winner[i] > 0:
            print("|        %i        |            %i             |        Portion of $%i       " % (chart_pos, winner[i], prize_money[i]))
    print("-"*85)

def ticketCarryOver(ticketCarry):
    '''Carry tickets over if lost'''
    if ticketCarry > 0:
        return ticketCarry
    else:
        return 0

#endregion


#endregion

#region MAIN PROGRAM
print(USER_GREETING)
gambling = True
while gambling:
    lines = []
    tickets_sold = ticketCarryOver(ticketCarry)
    enter_ticket = True
    while enter_ticket:
        # Get User Menu Input
        print(MENU)
        selection = A2_tools.getIntRange("Please select from the above card options: ", 1, 2)
        if selection == 1:
            # Generate 2 randomized sets of additional sets of 7 integers
            line1 = genRandLine()
            line2 = genRandLine()
            # Ask for user input of 7 intergers between 1-50 (no repeats)
            line3 = getManualLine("Please enter a number between 1-50: ", MIN_ROLL_NUM, MAX_ROLL_NUM)
            # Consolidate and print ticket
            printTicket()

        # 2. Quick Pick
        # Output 3 randomized sets of 7 integers
        if selection == 2:
            line1 = genRandLine()
            line2 = genRandLine()
            line3 = genRandLine()
            # Consolidate and print ticket
            printTicket()
        
        #   Are you done inputting?
        enter_ticket = input("Would you like to enter another ticket(y/n)? ")[0].lower().strip() == "y"  
    # How many tickets were sold not including user ticekts
    printEntries()
    # Get tickets sold
    tickets_sold += A2_tools.getIntRange("Please enter quantity of tickets sold: ", MIN_TICKET_COUNT, MAX_TICKET_COUNT)
    # Calculate prize money and display possible grand prize
    prize_money = countPrizeMoney(tickets_sold)
    print("Total Possible Grand Prize: $%i" % (prize_money[0]))
    # Draw random number 
    print(WINNERMENU)
    selection = A2_tools.getIntRange("Please select a menu option: ", 1, 2)
    # Draw pre-selected number
    winning_set = getWinningSet(selection)
    print("PRIZE WINNING NUMBERS: ", end="")
    print(winning_set)
    # Compare sets and add number matches to first element in each set array
    compareSets(lines, winning_set)
    #get winner count for each prize pool
    winners = countWinners(lines)
    hasWinner = False

    for i in winners:
        if i > 0:
            hasWinner = True

    if hasWinner:
        print(PRIZECHART)
        printChart(winners)
    else:
        print("Better luck next time!")
        ticketCarry = tickets_sold


    gambling = input("Would you like to go another round(y/n)? ")[0].lower().strip() == "y"  
#endregion

#region DESK CHECK

# 7 Matching Numbers
# Select:                   1  
# Input Selection:          0, 1, 22, 33, 44, 49, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 33, 44, 49, 16, 27
# Output:                   $4,250,000.00

# 6 Matching Numbers
# Select:                   1  
# Input Selection:          0, 1, 22, 33, 44, 49, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 33, 44, 49, 16, 0
# Output:                   You win a share of $250,000.00

# 5 Matching Numbers
# Select:                   1  
# Input Selection:          0, 1, 22, 33, 44, 49, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 33, 44, 49, 0, 0
# Output:                   You win a share of $250,000.00 

# 4 Matching Numbers
# Select:                   1  
# Input Selection:          0, 1, 22, 33, 44, 49, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 33, 44, 0, 0, 0
# Output:                   $20

# 3 Matching Numbers
# Select:                   1  
# Input Selection:          0, 1, 22, 33, 44, 49, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 33, 0, 0, 0, 0
# Output:                   $5 (free ticket)

# 2 or Less Matching Numbers
# Select:                   1  
# Input Selection:          0, 1, 22, 33, 44, 49, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 0, 0, 0, 0, 0
# Output:                   Loss

# 2 or Less Matching Numbers, try again and win with 7 matching numbers
# Select:                   1  
# Input Selection:          0, 1, 22, 33, 44, 49, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 0, 0, 0, 0, 0
# Output:                   Loss
# Playagain:                Y
# Select:                   1
# Input Selection:          0, 1, 22, 33, 44, 49, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 33, 44, 49, 16, 27
# Output:                   $8,500,000.00

# Anything but an integer
# Select:                   1  
# Input Selection:          a, ' ', '/'
# Output:                   Invalid Entry, Enter nth Number again

# Check Random Ticket output
# Select:                   2
# Input Selection:          1, 22, 33, 44, 49, 16, 27  
# Select:                   3
# Output:                   % of prize pool, Lose, $5, $20, $0.25, $0.85

#endregion


