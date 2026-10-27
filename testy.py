from item import Item
from inventory import Inventory
from suspect import Suspect
from game_score import GameScore
from datetime import date


def test_item_creation():
    item = Item(name="List", description="List z pogróżkami", is_proof=True)
    assert item.name == "List"
    assert item.is_proof is True

def test_add_and_get_item():
    inv = Inventory()
    item = Item("List", "Dowód", True)
    inv.add(item)
    assert inv.has_item("List")
    assert inv.items[0] == item

def test_suspect_reacts_to_item():
    suspect = Suspect("Jan", False, reactions={"list": "To nie mój list!"}, dialogue='nic')
    output = suspect.show("list")
    assert "reaguje" in output.lower()

def test_game_score_serialization():
    score = GameScore("Zbrodnia", 2, date.today(), "5m")
    d = score.to_dict()
    restored = GameScore.from_dict(d)
    assert restored.game_name == score.game_name
    assert restored.playtime == "5m"

if __name__ == "__main__":
    test_item_creation()
    test_add_and_get_item()
    test_suspect_reacts_to_item()
    test_game_score_serialization()