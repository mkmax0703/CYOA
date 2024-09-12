# room.py

class Room:
    def __init__(self, description):
        self.description = description
        self.connections = {}
        self.characters = {}
        self.items = {}

    def connect(self, direction, room):
        self.connections[direction] = room

    def add_character(self, character):
        self.characters[character.name] = character

    def add_item(self, item):
        self.items[item.name] = item

    def describe(self):
        print(self.description)
        if self.characters:
            print("You see:")
            for character in self.characters.values():
                print(f"- {character.name}")
        if self.items:
            print("You see the following items:")
            for item in self.items.values():
                print(f"- {item.name}")

    def list_options(self):
        options = []
        option_map = {}

        option_num = 1

        if self.connections:
            for direction in self.connections:
                options.append(f"Move {direction}")
                option_map[str(option_num)] = ("move", direction)
                option_num += 1

        if self.characters:
            for character in self.characters:
                options.append(f"Talk to {character}")
                option_map[str(option_num)] = ("talk", character)
                option_num += 1

        if self.items:
            for item in self.items:
                options.append(f"Take {item}")
                option_map[str(option_num)] = ("take", item)
                option_num += 1

        options.append("Show inventory")
        option_map[str(option_num)] = ("show_inventory", None)
        option_num += 1

        options.append("Quit game")
        option_map[str(option_num)] = ("quit", None)

        print("\nYou can:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        return option_map
