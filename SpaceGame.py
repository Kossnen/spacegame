# Import os to use os.system('cls') later on.
# Clear doesn't work in PyCharm. However, works as intended once compiled.
import os


# Create a function to print instructions and intro.
# Clear screen after each Enter press.
# Retype instructions after each press to give the instructions an interactive, staggered feel.
# Note: This will look repetitive in PyCharm. Works as intended once compiled.
# Note 2: This would be better pulled from a .txt file. Due to submission of a single file, it must be done this way.
def instructions():
    print()
    print()
    print()
    border()
    print('Welcome to "Security Breach"!')
    border()
    input('Press Enter to continue.\n')
    os.system('cls')
    print()
    print()
    print()
    border()
    print('Welcome to "Security Breach"!')
    border()
    print('Use your map navigate from room to room.\n')
    border()
    input('Press Enter to continue.\n')
    os.system('cls')
    print()
    print()
    print()
    border()
    print('Welcome to "Security Breach"!')
    border()
    print('Use your map navigate from room to room.\nYou can move by typing directional commands:\n\nNorth, N, '
          'Up, U, South, S, Down, D, \nEast, E, Right, R, West, W, Left, L\n\nAdditionally, you may type Quit or Exit '
          'to end the game.\n')
    border()
    input('Press Enter to continue.\n')
    os.system('cls')
    print()
    print()
    print()
    border()
    print('Welcome to "Security Breach"!')
    border()
    print('Use your map navigate from room to room.\nYou can move by typing directional commands:\n\nNorth, N, Up, U, '
          'South, S, Down, D, \nEast, E, Right, R, West, W, Left, L\n\nAdditionally, you may type Quit or Exit to '
          'end the game.\nYour objective is to make it to Pod B2 to confront the life form after gathering all of '
          'the items.')
    border()
    input('Memorize the instructions. Press Enter one last time to review your mission objectives.\n')
    os.system('cls')
    print()
    print()
    print()
    border()
    print('Mission Details:')
    border()
    print('              -Command Center-')
    border()
    print('*BBZZZZzzzttt* A haul breach has been detected on your ship.\nContamination detected. It seems to be '
          'emanating from Pod B2.')
    border()
    print('Additional Information... *bbbBBzzzttt* ')
    print('                 -UPDATING-')
    print('               ~`~Attention!~`~\nLife Form detected. Handle with extreme caution!')
    border()
    print('As you are the only one on the ship, you need to eliminate this life form.\nHelp will not arrive. You need'
          ' to prepare. Do it fast.')
    border()
    print('Leave your Crew Quarters and gather all necessary equipment and activate containment measures.')
    print('Do this before entering Pod B2. You will surely fail without your equipment.')
    border()
    input('*BzZZzt* Do you have all that soldier? A list of equipment needed is to follow....Press Enter to continue\n')
    os.system('cls')
    border()
    print('Inventory needed before entering B2 is as follows:')
    border()
    print('  -Protective Helmet: Located in Pod A1 by your desk.\n  -Shock Gun: Located in Pod A2 weapon locker.\n  '
          '-Contamination Control Measures Remote: Located in Pod A3.\n  -Your Lucky Boots: Located outside of your '
          'Crew Quarters in Pod B2.\n  -Standard Issue Protective Vest: Located in your clothing locker. Pod B3.\n '
          ' -Spare Oxygen Tank: Located in auxiliary closet. Pod C1.\n  -Environmental Control Remote: Located in Pod'
          ' C2.\n  -Explosives: Located in Pod C3.... In case the problem can not be dealt with by other means.')
    border()
    input('Press Enter to continue.\n')
    os.system('cls')
    border()
    print('There is one issue. The doors open based on biometrics.\nThey will not open for the life form in Pod B2. '
          'He is trapped there for now.\nHowever, they will automatically open for you if you walk to them.\nIf '
          'you''re not careful, you may inadvertently walk into Pod B2 with no gear.\nCompletely unprepared and sure '
          'to fail. Letting the creature out....')
    border()
    input('Press Enter to continue.\n')
    os.system('cls')
    border()
    print('If this thing isn''t stopped, autopilot will direct the ship back to Earth.\nWho knows what will happen if '
          'it reaches your home.....')
    border()
    input('Press Enter to embark on your mission.\n')
    os.system('cls')


# Define a border function to separate elements when needed.
def border():
    print('__________________________________________________________')


# Defines each room's map and what segments to use. B2 not included as this is the end.
# Additional if statement to evaluate if player character should have helmet on.
def crew_quarters():
    if 'Helmet' in inventory:
        print(map_title, '\n', map_divide_start, '\n', north_no_exit, '\n', top_E_exit, '\n', mid_E_exit, '\n',
              lower_E_exit, '\n', south_no_exit, '\n', map_divide_end)
    else:
        print(map_title, '\n', map_divide_start, '\n', north_no_exit, '\n', top_E_exit, '\n', nHelm_mid_E_exit, '\n',
              lower_E_exit, '\n', south_no_exit, '\n', map_divide_end)


def pod_a1():
    if 'Helmet' in inventory:
        print(map_title, '\n', map_divide_start, '\n', north_no_exit, '\n', top_E_exit, '\n', mid_E_exit, '\n',
              lower_E_exit, '\n', south_exit, '\n', map_divide_end)
    else:
        print(map_title, '\n', map_divide_start, '\n', north_no_exit, '\n', top_E_exit, '\n', nHelm_mid_E_exit, '\n',
              lower_E_exit, '\n', south_exit, '\n', map_divide_end)


def pod_a2():
    if 'Helmet' in inventory:
        print(map_title, '\n', map_divide_start, '\n', north_no_exit, '\n', top_WandE_exit, '\n', mid_WandE_exit, '\n',
              lower_WandE_exit, '\n', south_exit, '\n', map_divide_end)
    else:
        print(map_title, '\n', map_divide_start, '\n', north_no_exit, '\n', top_WandE_exit, '\n', nHelm_mid_WandE_exit,
              '\n', lower_WandE_exit, '\n', south_exit, '\n', map_divide_end)


def pod_a3():
    if 'Helmet' in inventory:
        print(map_title, '\n', map_divide_start, '\n', north_no_exit, '\n', top_W_exit, '\n', mid_W_exit, '\n',
              lower_W_exit, '\n', south_exit, '\n', map_divide_end)
    else:
        print(map_title, '\n', map_divide_start, '\n', north_no_exit, '\n', top_W_exit, '\n', nHelm_mid_W_exit, '\n',
              lower_W_exit, '\n', south_exit, '\n', map_divide_end)


def pod_b1():
    if 'Helmet' in inventory:
        print(map_title, '\n', map_divide_start, '\n', north_exit, '\n', top_WandE_exit, '\n', mid_WandE_exit, '\n',
              lower_WandE_exit, '\n', south_exit, '\n', map_divide_end)
    else:
        print(map_title, '\n', map_divide_start, '\n', north_exit, '\n', top_WandE_exit, '\n', nHelm_mid_WandE_exit,
              '\n', lower_WandE_exit, '\n', south_exit, '\n', map_divide_end)


def pod_b3():
    if 'Helmet' in inventory:
        print(map_title, '\n', map_divide_start, '\n', north_exit, '\n', top_W_exit, '\n', mid_W_exit, '\n',
              lower_W_exit, '\n', south_exit, '\n', map_divide_end)
    else:
        print(map_title, '\n', map_divide_start, '\n', north_exit, '\n', top_W_exit, '\n', nHelm_mid_W_exit, '\n',
              lower_W_exit, '\n', south_exit, '\n', map_divide_end)


def pod_c1():
    if 'Helmet' in inventory:
        print(map_title, '\n', map_divide_start, '\n', north_exit, '\n', top_E_exit, '\n', mid_E_exit, '\n',
              lower_E_exit, '\n', south_no_exit, '\n', map_divide_end)
    else:
        print(map_title, '\n', map_divide_start, '\n', north_exit, '\n', top_E_exit, '\n', nHelm_mid_E_exit, '\n',
              lower_E_exit, '\n', south_no_exit, '\n', map_divide_end)


def pod_c2():
    if 'Helmet' in inventory:
        print(map_title, '\n', map_divide_start, '\n', north_exit, '\n', top_WandE_exit, '\n', mid_WandE_exit, '\n',
              lower_WandE_exit, '\n', south_no_exit, '\n', map_divide_end)
    else:
        print(map_title, '\n', map_divide_start, '\n', north_exit, '\n', top_WandE_exit, '\n', nHelm_mid_WandE_exit,
              '\n', lower_WandE_exit, '\n', south_no_exit, '\n', map_divide_end)


def pod_c3():
    if 'Helmet' in inventory:
        print(map_title, '\n', map_divide_start, '\n', north_exit, '\n', top_W_exit, '\n', mid_W_exit, '\n',
              lower_W_exit, '\n', south_no_exit, '\n', map_divide_end)
    else:
        print(map_title, '\n', map_divide_start, '\n', north_exit, '\n', top_W_exit, '\n', nHelm_mid_W_exit, '\n',
              lower_W_exit, '\n', south_no_exit, '\n', map_divide_end)


# Define player function for location and inventory.
def player():
    border()
    # Calls function to display current room's map
    current_room_map()
    # Display Location
    print('You are in {}'.format(current_room))
    # Evaluates if there is an item in the room.
    # If so, then evaluates if you already have that item.
    # Prints appropriate response.
    if 'Item' in roomList[current_room]:
        if roomList[current_room]['oItem'] in inventory:
            print('You already picked up your {}.'.format(roomList[current_room]['oItem']))
        else:
            print('You can see {}.'.format(roomList[current_room]['Item']))
            # Asks if you would like to pick up the item if there is one in the room.
            pick_up = input('Would you like to pick up? \'Yes\', \'Y\', \'No\' or \'N\'?\n').capitalize()
            while pick_up != 'Yes' or pick_up != 'No' or pick_up != 'Y' or pick_up != 'N':
                if pick_up == 'Yes' or pick_up == 'Y':
                    print('You pick up {}.'.format(roomList[current_room]['oItem']))
                    # Starts by appending the inventory to get rid of the 'Nothing!' entry.
                    if 'Lucky Boots' not in inventory:
                        inventory[0] = 'Lucky Boots'
                        break
                    else:
                        # Adds item collected to the inventory after Lucky Boots.
                        inventory.append(roomList[current_room]['oItem'])
                        break
                elif pick_up == 'No' or pick_up == 'N':
                    print('You decide to leave the {} behind.'.format(roomList[current_room]['oItem']))
                    break
                else:
                    pick_up = input('Invalid response. Would you like to pick up?'
                                    ' \'Yes\', \'Y\', \'No\' or \'N\'?\n').capitalize()
    else:
        print('There are no items here. Stop wasting time. You need to hurry!')
    border()
    print('------Inventory------')
    # Prints Nothing! if there is nothing in inventory. Prints the list separated by comma if it is populated.
    print(*inventory, sep=", ")
    # Display how many items the user has based on length of inventory.
    if 'Lucky Boots' in inventory:
        if len(inventory) != 8:
            print('You have', len(inventory), 'out of 8 items needed')
        else:
            print('You have all of the items! It\'s time to rock.')
    else:
        print('You aren\'t carrying anything!')
    border()
    print()


# Function decides which map to use based on current_room.
def current_room_map():
    if current_room == 'the Crew Quarters':
        return crew_quarters()
    if current_room == 'Pod A1':
        return pod_a1()
    if current_room == 'Pod A2':
        return pod_a2()
    if current_room == 'Pod A3':
        return pod_a3()
    if current_room == 'Pod B1':
        return pod_b1()
    if current_room == 'Pod B3':
        return pod_b3()
    if current_room == 'Pod C1':
        return pod_c1()
    if current_room == 'Pod C2':
        return pod_c2()
    if current_room == 'Pod C3':
        return pod_c3()


# Function for retrieving new rooms from dictionary based on direction moved.
def new_room():
    currentRoom = room
    for i in roomList:
        if i == room:
            if p_movement in roomList[room]:
                currentRoom = roomList[room][p_movement]
    # Return new room
    return currentRoom


# Defines inputs to give user more options as to what can be entered.
north = ['North', 'N', 'Up', 'U']
south = ['South', 'S', 'Down', 'D']
east = ['East', 'E', 'Right', 'R']
west = ['West', 'W', 'Left', 'L']
p_exit = ['Exit', 'Quit']

# Set default room, current_room, inventory list, and sets some variables to blank.
room = 'the Crew Quarters'
current_room = room
old_room = ''
inventory = ['       Nothing!']
roomList = ''
p_movement = ''

# Defines the segments for map room layout art
map_title = '      ~`~MAP~`~'
map_divide_start = '+----------------+'
north_exit = '  ____|   |____'
north_no_exit = '  _____________'
south_exit = '  ````|   |```` '
south_no_exit = '  `````````````'
mid_no_exit = '  |      ' '\U0001f916' '      |'  # unused
top_WandE_exit = '  \u2534           \u2534'
top_W_exit = '  \u2534           |'
top_E_exit = '  |           \u2534'
mid_WandE_exit = '       ' '\U0001f916' '       '
nHelm_mid_WandE_exit = '       ' '\U0001f468' '       '
mid_W_exit = '       ' '\U0001f916' '     |'
nHelm_mid_W_exit = '       ' '\U0001f468' '     |'
mid_E_exit = '  |    ' '\U0001f916' '        '
nHelm_mid_E_exit = '  |    ' '\U0001f468' '        '
lower_W_exit = '  T           |'
lower_WandE_exit = '  T           T'
lower_E_exit = '  |           T'
map_divide_end = '+----------------+'

# Provides an option to skip the intro and instructions before main loop starts.
skip = input('Type \'Skip\' to skip the rules and introductions.\n\nPress Enter to continue.\n').capitalize()
while skip != 'Skip':
    os.system('cls')
    instructions()
    skip = 'Skip'


# Define main function
def main():
    # set all the variables to reference their global counterparts
    global room
    global old_room
    global inventory
    global roomList
    global p_movement
    global current_room

    # Dictionary to link rooms with paths and items. oItems for obtained items.
    roomList = {
        'the Crew Quarters': {'East': 'Pod B1'},
        'Pod A1': {'Item': 'your Protective Helmet hanging on a hook by your desk', 'oItem': 'Helmet',
                   'South': 'Pod B1',
                   'East': 'Pod A2'},
        'Pod A2': {'Item': 'a Shock Gun just inside the weapon\'s locker', 'oItem': 'Shock Gun', 'South': 'Pod B2',
                   'East': 'Pod A3', 'West': 'Pod A1'},
        'Pod A3': {'Item': 'the Contamination Control Remote laying on a desk, covered by loose papers and dust',
                   'oItem': 'C.C.Remote', 'South': 'Pod B3', 'West': 'Pod A2'},
        'Pod B1': {'Item': 'your Lucky Boots which you remember throwing off last night right outside of your '
                           'quarter\'s door', 'oItem': 'Lucky Boots', 'North': 'Pod A1', 'East': 'Pod B2',
                   'West': 'the Crew Quarters', 'South': 'Pod C1'},
        'Pod B3': {'Item': 'your Standard Issue Protective Vest sticking out from behind the improperly closed clothing'
                           'locker door', 'oItem': 'Vest', 'North': 'Pod A3', 'West': 'Pod B2', 'South': 'Pod C3'},
        'Pod C1': {'Item': 'a Spare Oxygen Tank in an auxiliary cabinet', 'oItem': 'O2 Tank', 'North': 'Pod B1',
                   'East': 'Pod C2'},
        'Pod C2': {'Item': 'the Environmental Control Remote placed on a console beside a couple of flashing screens',
                   'oItem': 'E.C. Remote', 'North': 'Pod B2', 'East': 'Pod C3', 'West': 'Pod C1'},
        'Pod C3': {'Item': 'a pack of Explosives in a locker. Just looking at them causes you to nervously sweat..',
                   'oItem': 'Explosives', 'North': 'Pod B3', 'West': 'Pod C2'}

    }

    # Main loop start. Dictates that the game continues till the word Exit or Quit is typed.
    while current_room != 'Exit':
        while current_room != 'Pod B2':
            # Call the function to create a map and list the current player position/inventory
            player()
            # Gather user input and store to p_movement. Capitalize the input to fix sloppy user input.
            p_movement = input('Which direction do you want to go?\n').capitalize()
            os.system('cls')
            # Converts user input to "North, South, East, or West" using above lists depending on what is entered.
            if p_movement in north:
                p_movement = north[0]
            elif p_movement in south:
                p_movement = south[0]
            elif p_movement in east:
                p_movement = east[0]
            elif p_movement in west:
                p_movement = west[0]
            # Checks to see if p_movement is in one of the lists.
            # Checking for "North, South, East, or West" would also work.
            if p_movement in north or p_movement in south or p_movement in east or p_movement in west:
                # Saves the current room to "old_room" and uses function new_room to create new current_room.
                # Compare old and new rooms to see if we changed rooms.
                room = current_room
                old_room = current_room
                current_room = new_room()
                # If current_room did not change, tell player they cant go that way.
                if current_room == old_room:
                    border()
                    print('There is no path there.')
                # If different, let player know they moved to the next room.
                else:
                    border()
                    print('The door automatically opens and you slowly enter {}.'.format(current_room))
            # Changes current_room to Exit to break the while loop if typed
            elif p_movement in p_exit:
                current_room = 'Exit'
            # If the input was not in any of the lists, it is invalid.
            else:
                border()
                print('!!!-----Invalid entry. Try again!------!!!')
                border()
        else:
            # If all 8 items are in the inventory when entering B2, win condition.
            if len(inventory) == 8:
                print('There in front of you stands not just any life form. But a creature.\n')
                border()
                input('Press Enter to continue.\n')
                os.system('cls')
                border()
                print('There in front of you stands not just any life form. But a creature.\n')
                print()
                print()
                print('A big one.\n')
                border()
                input('Press Enter to continue.\n')
                os.system('cls')
                border()
                print('The creature '
                      'lunges a tentacle appendage at you.\nIt wraps around one of your Lucky Boots.\nThe boot slides '
                      'off and you are able to leap backwards.\nYou fire the Stun Gun which bounces off of the '
                      'creature. Having done no damage.\nYou survive repeated hits to the chest and head thanks to '
                      'your gear. You know that this fight is unwinnable.\nAching and on the verge of blacking out, '
                      'you arm the Explosives.\n')
                border()
                input('Press Enter to continue.\n')
                os.system('cls')
                border()
                print('The last thing you hear is a calming beeping noise.\n')
                border()
                input('Press Enter to continue.\n')
                os.system('cls')
                border()
                print('A count down.\n\nBeep. Beep. Beeeeeeeep...\n')
                print('You\'re home is safe\n\n-----MISSION SUCCESS-----\n...at a cost.\n')
                # changes current room to 'Exit' Which causes the loop to end.
                current_room = 'Exit'
            # If all 8 items are not in the inventory when entering B2, lose condition.
            else:
                print('Panic sets in. Due to a hasty mistake, you accidentally walk into Pod B2 without all of your '
                      'gear!\nThe creature is much bigger than you thought it would be...\nA tentacle shoots out and'
                      ' wraps around your leg, tripping you. Pulling you in towards it.\nWith a loud thud. The creature'
                      ' slams you against the wall.\nEverything is going black... Is this it...? What have '
                      'you done...?')
                border()
                input('Press Enter to continue.\n')
                os.system('cls')
                print('Autopilot directs the ship back to Earth.\nMilitary personnel swarm the shuttle as soon as it '
                      'touches ground.\nThey cautiously open the door. To their surprise, they find nothing.\nThey all'
                      ' know this can only mean one thing...\nIt escaped. It\'s somewhere on Earth...\n'
                      '\n-----MISSION FAILURE-----\n')
                border()
                current_room = 'Exit'
    # Once While loop is broke by Exit current_room, prompts player to end the game with the Enter button.
    else:
        border()
        input('Game over! Press Enter to leave the game.')
        border()
        quit()


if __name__ == "__main__":
    main()
