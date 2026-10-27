
from datetime import date

class GameScore:
    def __init__(self, game_name, guesses, completion_date, playtime):
        self.game_name = game_name
        self.guesses = guesses
        self.completion_date = completion_date
        self.playtime = playtime

    def __str__(self):
        return f"{self.game_name}: {self.guesses} prób, ukończono {self.completion_date}, czas gry: {self.playtime}"

    @staticmethod
    def format_duration(seconds):
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes}m {seconds}s"

    def to_dict(self):
        return {
            "game_name": self.game_name,
            "guesses": self.guesses,
            "completion_date": self.completion_date.isoformat(),
            "playtime": self.playtime
        }

    @staticmethod
    def from_dict(data):
        return GameScore(
            game_name=data["game_name"],
            guesses=data["guesses"],
            completion_date=date.fromisoformat(data["completion_date"]),
            playtime=data["playtime"]
        )