from inventory import Inventory


class Plot:
    def __init__(self, name,  start_description, end_description, suspects, rooms):
        self.name = name
        self.start_description = start_description
        self.suspects = suspects
        self.rooms = rooms
        self.inv = Inventory()
        self.end_description = end_description

    def interact_room(self):
        room_name = input("Podaj nazwę pokoju: ")
        for room in self.rooms:
            if room.name.lower() == room_name.lower():
                item = room.search()
                if item:
                    self.inv.add(item)
                return
        print("Nie znaleziono pokoju.")

    def interact_suspect(self):
        name = input("Podaj nazwę podejrzanego: ")
        for suspect in self.suspects:
            if suspect.name.lower() == name.lower():
                suspect.interrogate()
                return
        print("Nie znaleziono podejrzanego.")

    def interact_inventory(self):
        self.inv.print_items()
        item_name = input("Podaj nazwę przedmiotu do opisu lub Enter by wrócić: ")
        if item_name:
            self.inv.describe_item(item_name)

    def show_suspects(self):
        for suspect in self.suspects:
            suspect.describe()

    def show_rooms(self):
        for room in self.rooms:
            room.describe()

    def show_evidence_to_suspect(self, item_name: str, suspect_name: str):
        if not self.inv.has_item(item_name):
            print('Nie masz takiego przedmiotu.')
            return

        for suspect in self.suspects:
            if suspect.name.lower() == suspect_name.lower():
                print(suspect.show(item_name))
                return
        print("Nie znaleziono podejrzanego.")