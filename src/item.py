# Items


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def on_yoink(self, current_room):
        print(f"You yoink {self.name} and put it in your bag.\n")

    def on_drop(self, current_room):
        print(f"You toss out {self.name}.")

