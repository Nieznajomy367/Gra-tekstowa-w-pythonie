class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"Dodano do ekwipunku: {item.name}")

    def clear(self):
        self.items = []

    def has_item(self, name):
        return any(item.name.lower() == name.lower() for item in self.items)

    def print_items(self):
        if not self.items:
            print("Ekwipunek jest pusty.")
        else:
            print("Ekwipunek:")
            for item in self.items:
                print(f"- {item.name}")

    def describe_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                item.describe()
                return
        print("Nie znaleziono takiego przedmiotu w ekwipunku.")

