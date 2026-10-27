
class Item:
    def __init__(self, name, description, is_proof=False):
        self.name = name
        self.description = description
        self.is_proof = is_proof

    def describe(self):
        print(f"Dowód: {self.name}")
        print(self.description)



