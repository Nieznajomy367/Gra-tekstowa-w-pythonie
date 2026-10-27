from datetime import datetime
from command_parser import CommandParser
from game_score import GameScore
import json
import os

class Game:
    def __init__(self, game_scenarios, chosen_scenario=None):
        self.game_scenarios = game_scenarios
        self.chosen_scenario = chosen_scenario
        self.parser = CommandParser(self)
        self.start_time = None
        self.running_choice = True
        self.running_game = True
        self.guesses= 0
        self.scores_file = "scores.json"
        self.game_scores = self.load_scores()


    def choose_scenario(self):
        while self.running_choice:
            if not self.game_scenarios:
                print("Brak dostępnych scenariuszy.")
                return

            print("\nWpisz 'pomoc' po listę komend.")
            print("Wybierz scenariusz wpisując jego numer (np. '1'):")
            for idx, scenario in enumerate(self.game_scenarios):
                print(f"{idx + 1}. {scenario.name}")

            choice = self.parser.parse_command1(input('<< '))

            if choice == 'exit':
                self.running_choice = False

    def choose(self, choice):
        index = int(choice) - 1
        if 0 <= index < len(self.game_scenarios):
            self.chosen_scenario = self.game_scenarios[index]
            self.game_loop()
        else:
            print("Nieprawidłowy wybór scenariusza.")

    def game_loop(self):
        if not self.chosen_scenario:
            print("Nie wybrano scenariusza.")
            return

        print(self.chosen_scenario.start_description)
        print("Wpisz 'pomoc' po listę komend.")
        self.running_game = True
        self.start_time = datetime.now()

        while self.running_game:
            command = input("\n>> ")
            result = self.parser.parse_command2(command)
            if result == "exit":
                self.running_game= False
                self.chosen_scenario.inv.clear()


    def show_suspects(self):
        self.chosen_scenario.show_suspects()

    def show_rooms(self):
        self.chosen_scenario.show_rooms()

    def interact_room(self):
        self.chosen_scenario.interact_room()

    def interact_suspect(self):
        self.chosen_scenario.interact_suspect()

    def interact_inventory(self):
        self.chosen_scenario.interact_inventory()

    def show_evidence_to_suspect(self, item_name, suspect_name):
        self.chosen_scenario.show_evidence_to_suspect(item_name, suspect_name)

    def end_scenario(self):
        name = input("Kogo wskazujesz jako sprawcę?: ")
        suspect = next((s for s in self.chosen_scenario.suspects if s.name.lower() == name.lower()), None)

        if not suspect:
            print("❗ Nie znaleziono podejrzanego o takiej nazwie.")
            return

        proof = input('Jaki dowód na to wskazuje?: ')
        item = next((i for i in self.chosen_scenario.inv.items if i.name.lower() == proof.lower()), None)

        if not item:
            print("❗ Nie znaleziono dowodu o takiej nazwie.")
            return

        is_correct = suspect.is_criminal and item.is_proof
        result = f"{self.chosen_scenario.end_description}" if is_correct else "Niepoprawnie! Spróbuj ponownie"
        print(result)

        self.guesses += 1

        if is_correct:
            duration = GameScore.format_duration((datetime.now() - self.start_time).total_seconds())
            score = GameScore(
                game_name=self.chosen_scenario.name,
                guesses=self.guesses,
                completion_date=datetime.now().date(),
                playtime=duration
            )
            self.game_scores.append(score)
            self.save_scores()
            self.chosen_scenario.inv.clear()
            self.running_game = False


    def show_game_scores(self):
        print("Wyniki zakończonych gier:")
        for game in self.game_scores:
            print(game)

    def save_scores(self):
        data = json.dumps([score.to_dict() for score in self.game_scores], indent=2)
        with open(self.scores_file, "w", encoding="utf-8") as f:
            f.write(data)

    def load_scores(self):
        if not os.path.exists(self.scores_file):
            return []
        with open(self.scores_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [GameScore.from_dict(entry) for entry in data]

    def clear_scores(self):
        self.game_scores = []
        with open(self.scores_file, "w", encoding="utf-8") as f:
            json.dump([], f)
        print("Historia gier została wyczyszczona.")

