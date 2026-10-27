
class CommandParser:
    def __init__(self, game_in):
        self.help_info = [('Dostępne komendy:\n'
                        "- 'liczba'— wybierz numer scenariusza\n"
                        "- historia gier\n"
                        "- usuń historię\n"
                        "- wyjście"

                        ), (
            "Dostępne komendy:\n"
            "- pokoje\n"
            "- przeszukaj\n"
            "- podejrzani\n"
            '- przesłuchaj\n'
            "- ekwipunek: pokaż zebrane dowody\n"
            "- pokaż przedmiot [nazwa przedmiotu] [nazwa podejrzanego]\n"
            "- wskaż sprawcę\n"
            "- pomoc\n"
            "- wyjście\n"
            "- historia gier"
        )]
        self.game_in = game_in
        self.command_handlers1 = {
            "pomoc": self.help_info1,
            "historia gier": self.game_in.show_game_scores,
            'wyjście': self.exit,
            'usuń historię': self.game_in.clear_scores

        }
        self.command_handlers2 = {
            "pomoc": self.help_info2,
            "pokoje": self.game_in.show_rooms,
            "podejrzani": self.game_in.show_suspects,
            "ekwipunek": self.game_in.interact_inventory,
            "wskaż sprawcę": self.game_in.end_scenario,
            "wyjście": self.exit,
            "przeszukaj": self.game_in.interact_room,
            "przesłuchaj": self.game_in.interact_suspect,
            "historia gier": self.game_in.show_game_scores,
        }
    def parse_command1(self, command: str):
        try:
            command = int(command)
            self.game_in.choose(command)
        except(IndexError, ValueError):
            command = command.strip().lower()
            for keyword, handler in self.command_handlers1.items():
                result = handler() if command.startswith(keyword) else None
                if result == "exit":
                    return "exit"

            if command not in self.command_handlers1:
                print("Nieznana komenda. Wpisz 'pomoc' aby zobaczyć dostępne polecenia.")

    def help_info1(self):
        print(self.help_info[0])

    def help_info2(self):
        print(self.help_info[1])

    def parse_command2(self, command: str):
        command = command.strip().lower()

        if command.startswith("pokaż przedmiot"):
            parts = command.split()
            if len(parts) >= 4:
                item_name = parts[2]
                suspect_name = parts[3]
                self.game_in.show_evidence_to_suspect(item_name, suspect_name)
                return
            else:
                print("Użycie: pokaż przedmiot [nazwa przedmiotu] [nazwa podejrzanego]")
                return

        for keyword, handler in self.command_handlers2.items():
            if command.startswith(keyword):
                return handler()

        if command not in self.command_handlers1:
            print("Nieznana komenda. Wpisz 'pomoc' aby zobaczyć dostępne polecenia.")


    def exit(self):
        print("Zakończono grę.")
        return 'exit'

