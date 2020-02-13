from room import Room
from roomlist import room
from player import Player
from item import Item
import sys

# Declare all the rooms

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

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

commands = ["n", "s", "e", "w", "take", "drop", "q", "quit"]

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
        command = input("\nWhat's the move? [n/s/e/w/take/drop]  ").lower()

        # check if valid command
        if command in commands:
            if command == "q" or command == "quit":
                print("See you next time.")
                sys.exit()
            elif command == "n":
                if player.current_room.n_to == None:
                    print("\nThere isn't anything in that direction.\n")
                else:
                    player.current_room = player.current_room.n_to
                    print(f"You walk towards the {player.current_room.name}...")
            elif command == "s":
                if player.current_room.s_to == None:
                    print("\nThere isn't anything in that direction.\n")
                else:
                    player.current_room = player.current_room.s_to
            elif command == "e":
                if player.current_room.e_to == None:
                    print("\nThere isn't anything in that direction.\n")
                else:
                    player.current_room = player.current_room.e_to
            elif command == "w":
                if player.current_room.w_to == None:
                    print("\nThere isn't anything in that direction.\n")
                else:
                    player.current_room = player.current_room.w_to
        else:
            print("Sorry, that's not a valid command. Try: [n/s/e/w/q/quit]")


main()
