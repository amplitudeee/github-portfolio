#-----------------------------------------------
# Title:            My Tools Library for Python Console
# Author:           Matt Salvadori
# Date:             July 18, 2025
# Purpose:          A set of tools to be reused in our console apps
# ----------------------------------------------

#INPUT
# Welcome to the Big 7
# 1. Selection pick input
# 2. Quick Pick input

# 1. Selection Pick
# Ask for user input of 7 intergers between 1-50 (no repeats)
# Generate 2 randomized sets of additional sets of 7 integers
# Print all 3 sets of numbers
# 
# 2. Quick Pick
# Output 3 randomized sets of 7 integers
# Print all 3 sets of numbers
#
#   Are you done inputting?
#       How many tickets were sold not including user ticekts
#           Draw random number 
#           Draw pre-selected number
#           Did you win?
#           If loss then add old amount to new amount

#PROCESS
# WRAPPER Compare ticket array to winning array and decide how much the ticket array is worth based on table
#   Take ticket array, Winner Array

#OUTPUT
# Print Ticket line results

#DESK CHECK

# 7 Matching Numbers
# Select:                   1  
# Input Selection:          1, 22, 33, 44, 55, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 33, 44, 55, 16, 27
# Output:                   $4,250,000.00

# 6 Matching Numbers
# Select:                   1  
# Input Selection:          1, 22, 33, 44, 55, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 33, 44, 55, 16, 0
# Output:                   You win a share of $250,000.00

# 5 Matching Numbers
# Select:                   1  
# Input Selection:          1, 22, 33, 44, 55, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 33, 44, 55, 0, 0
# Output:                   You win a share of $250,000.00 

# 4 Matching Numbers
# Select:                   1  
# Input Selection:          1, 22, 33, 44, 55, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 33, 44, 0, 0, 0
# Output:                   $20

# 3 Matching Numbers
# Select:                   1  
# Input Selection:          1, 22, 33, 44, 55, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 33, 0, 0, 0, 0
# Output:                   $5 (free ticket)

# 2 or Less Matching Numbers
# Select:                   1  
# Input Selection:          1, 22, 33, 44, 55, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 0, 0, 0, 0, 0
# Output:                   Loss

# 2 or Less Matching Numbers, try again and win with 7 matching numbers
# Select:                   1  
# Input Selection:          1, 22, 33, 44, 55, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 0, 0, 0, 0, 0
# Output:                   Loss
# Select:                   1
# Input Selection:          1, 22, 33, 44, 55, 16, 27
# Tickets Sold:             1000000
# Draw pre-selected number: 1, 22, 33, 44, 55, 16, 27
# Output:                   $8,500,000.00

# Anything but an integer
# Select:                   1  
# Input Selection:          a, ' ', '/'
# Output:                   Invalid Entry, Enter nth Number again

# Check Random Ticket output
# Select:                   2
# Input Selection:          1, 22, 33, 44, 55, 16, 27  
# Select:                   3
# Output:                   % of prize pool, Lose, $5, $20, $0.25, $0.85



