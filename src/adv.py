from room import Room
from roomlist import room
from player import Player
from item import Item
import sys

# Declare all the rooms

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

commands = ["n", "s", "e", "w", "q", "quit"]
actions = ["take", "drop"]
#
# Main
#


def main():
    # create player to initialize game
    player = Player(input("Player name: "), room["outside"])
    print(f"Welcome, {player.name}")

    while True:
        print("\nCurrent location: ", player.current_room.name)
        print(player.current_room.description)
        
        for item in player.current_room.items:
            print(f"{item}")
        command = input("\nWhat's the move? [n/s/e/w/take/drop]  ").lower().split(" ")

        if len(command) == 1:
            # check if valid command
            if command[0] in commands:
                # quit
                if command[0] == "q" or command[0] == "quit":
                    verify = input("Are you sure you want to quit? ")
                    if verify == "y":
                        print("See you next time.")
                        sys.exit()
                    else:
                        pass

                # movement
                elif command[0] in commands:
                    player.move(command[0])
            else:
                print("Sorry, that's not a valid command.")

        # interact with items
        elif len(command) == 2:
            item = command[1]
            if command[0] == "take":
                player.yoink(item)
            elif command[0] == "drop":
                player.drop(item)
            else:
                print("Sorry, that's not a valid command.")

        else:
            print("Sorry, that's not a valid command. Try: [n/s/e/w/take/drop/q/quit]")


main()
