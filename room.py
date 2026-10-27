
class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items if items else None
        self.searched = False

    def describe(self):
        print(f"Pokój: {self.name}")

    def search(self):
        if self.searched:
            print("Ten pokój już został przeszukany.")
            return []
        print(f"Przeszukujesz pokój: {self.name}...")
        self.searched = True
        print(self.description)
        if self.items:
            print("Znalazłeś następujące przedmioty:")
            print(self.items.name)
            return self.items
        else:
            print("Nie znaleziono żadnych przedmiotów.")
            return []