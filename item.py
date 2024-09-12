# item.py

class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def use(self, player, target=None):
        print(f"You can't use {self.name} here.")
