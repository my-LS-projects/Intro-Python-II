# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory={}):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f"{self.name}, {self.current_room}"

    def move(self, command):
        next_room = getattr(self.current_room, f"{command}_to")
        if next_room is not None:
            self.current_room = next_room
            print(f"You walk towards the {next_room.name}...")

    def yoink(self, item):
        # check if item exists
        try:
            room_item = self.current_room.items[item]
            del self.current_room.items[item]

        except KeyError:
            print("Sorry, that item is not in the room.")
            return

        self.inventory[item] = room_item
        print(f"INVENTORY: ")
        for item in self.inventory:
            print(item)

    def drop(self, item):
        try:
            player_item = self.inventory[item]
            del self.inventory[item]

        except KeyError:
            print("You don't have that in your inventory.")
            return

        self.current_room.items[item] = player_item
