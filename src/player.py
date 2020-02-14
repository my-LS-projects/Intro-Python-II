# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=[]):
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
        item = getattr(self.current_room.items, f"{item}")

    def drop(self, item):
        item = getattr(self.inventory, f"{item}")
