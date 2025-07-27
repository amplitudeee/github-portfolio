# ------------------------------------
# Title:    Projectile Motion Calculations
# Author:   Matt Salvadori
# Date:     July 10, 2025
# Purpose:  To calculate the time it takes for a projectile
#           to hit the ground mapping it's location each time interval.
# ------------------------------------

# IDFIIP0
#region IMPORTS
import math
import random
#region DECLARATIONS
GRAVITY = -9.81
MIN_START_DISTANCE = 250
MAX_START_DISTANCE = 3128
INITIAL_VELOCITY = 175.0
TIME_INTERVAL = 2.0
PI = 3.14159
HIT_DISTANCE = 5.0
SELF_DESTRUCT_DISTANCE = 1.00
USER_GREETING = '''
--------------------------------------------------
HELLO MOTHERFUCKER WELCOME TO MY PEW PEW TANK GAME
--------------------------------------------------'''
MENU = '''
--------------------------------------------------
1. Easy
2. Hard
3. Extreme
Q. Quit
--------------------------------------------------'''
#region FUNCTIONS

def randomDistance(min, max):
    '''randomize target distance given range'''
    ranNum = float(random.randint(min, max))
    return ranNum

def getUserFloatInRange(prompt):
    '''get user angle and validate'''
    is_valid = False
    while not is_valid:
        try:
            choice = float(input(prompt))

            if choice < 0 or choice > 90:
                print("Please enter a value between 0 and 90")
            else:
                is_valid = True
        except ValueError:
            print("Please enter a float value")
    return choice

def getRadians(float):
    '''use float to calc radians'''
    initial_angle = float * (PI / 180.0)
    return initial_angle

def findInitialVelocityXY(initial_angle_rads):
    '''Find initial velocity of x and y'''
    initial_velocity_x = INITIAL_VELOCITY * math.cos(initial_angle_rads)
    initial_velocity_y = INITIAL_VELOCITY * math.sin(initial_angle_rads)
    return [initial_velocity_x, initial_velocity_y]

def printInterval(initial_velocity_x, initial_velocity_y):
    '''Print X/Y coordinates at intervals of 2.0 seconds'''
    time = 0
    position_x = 0
    position_y = 0
    while position_y >= 0:
        time = time + TIME_INTERVAL

        position_x = initial_velocity_x * time
        position_y = initial_velocity_y * time + 0.5 * GRAVITY * time ** 2

        print("Time %.2f seconds, x = %.2fm, y = %.2fm." % (time, position_x, position_y))

def calcTimeToHitGround(initial_velocity_y):
    '''Calculate time to hit ground'''
    time_to_hit_ground = - 2 * initial_velocity_y / GRAVITY
    return time_to_hit_ground

def calcHorizontalDistance(initial_velocity_x, time_to_hit_ground):
    '''Calculate total horizontal distance'''
    horizontal_distance = initial_velocity_x * time_to_hit_ground
    return horizontal_distance

def match(horizontal_distance, targetDistance, num_shots):
    '''Checks results of shot'''
    if abs(horizontal_distance - targetDistance) < HIT_DISTANCE:
        print("You hit the target at %.2f meters!" % (targetDistance))
        print("Congradulations! You hit the target in %i shots!" % num_shots)
        return False
    elif horizontal_distance < SELF_DESTRUCT_DISTANCE:
        print("You self-destructed, oh no!  Game Over!")
        return False
    elif horizontal_distance < targetDistance:
        print("You missed, short by %.2f meters. \n Try again" % (targetDistance-horizontal_distance))
        return True
    else:
        print("You overshot by %.2f meters." % (horizontal_distance-targetDistance))
        print("Try again.")
        return True

def printResults(horizontal_distance, time_to_hit_ground):
    '''Print shot results'''
    print("\nTime to hit the ground: %.2f seconds" % (time_to_hit_ground))
    print("\nThe horizontal distance the projectile traveled is: %.2f meters" % (horizontal_distance))

def doPartition():
    print('-' * 40)

def applyMovement(gameMode, target_distance):
    if gameMode == 2 or gameMode == 3:
        move_distance = randomDistance(20, 30)
        print("Your tank moved %.1f meters towards the target." % (move_distance))
        target_distance -= move_distance

    if gameMode == 3:
        move_distance = randomDistance(-100, 100)
        print("The target moved %.1f meters." % (move_distance))
        target_distance += move_distance

    return target_distance


#region INFO
print(USER_GREETING)

#region MAIN
gameMode = 1
quit = False
while not quit:
    print(MENU)
    choice = input("Enter your choice: ")

    if choice == "1":
        gameMode = 1
    elif choice == "2":
        gameMode = 2
    elif choice == "3":
        gameMode = 3
    elif choice.lower() == "q":
        quit = True
        continue
    else:
        print("Invalid choice. Please try again.")
        continue

    gameon = True
    while gameon:
        target_distance = randomDistance(MIN_START_DISTANCE, MAX_START_DISTANCE)
        num_shots = 0
        game_win = False
        shootAgain = True

        while shootAgain:
            num_shots += 1
            doPartition()
            print("Target distance is %.1f meters." % target_distance)
            doPartition()
            initial_angle = getUserFloatInRange("Please enter an angle to fire at between 0-90: ")
            doPartition()
            initial_angle_rads = getRadians(initial_angle)
            ivxy = findInitialVelocityXY(initial_angle_rads)
            printInterval(ivxy[0], ivxy[1])
            time_to_hit_ground = calcTimeToHitGround(ivxy[1])
            horizontal_distance = calcHorizontalDistance((ivxy[0]), time_to_hit_ground)
            printResults(horizontal_distance, time_to_hit_ground)
            shootAgain = match(horizontal_distance, target_distance, num_shots)
            target_distance = applyMovement(gameMode, target_distance)



        gameon = input("Would you like to play again(y/n)?: ")[0].strip().lower() == 'y'

print("Goodbye!")
exit()
