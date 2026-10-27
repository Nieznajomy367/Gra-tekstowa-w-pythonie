class Suspect:
    def __init__(self, name, description, dialogue, reactions=None, is_criminal=False):
        self.name = name
        self.description = description
        self.dialogue = dialogue
        self.reactions = reactions if reactions else {}
        self.is_criminal = is_criminal

    def describe(self):
        print(f"Podejrzany: {self.name}")
        print(self.description)

    def interrogate(self):
        print(f"Przesłuchujesz {self.name}...")
        print(self.dialogue)

    def show(self, item_name):
        item_name = item_name.lower()
        if item_name in self.reactions:
            return f"{self.name} reaguje na {item_name}: {self.reactions[item_name]}"
        else:
            return f"{self.name} nie ma nic do powiedzenia na temat {item_name}."
