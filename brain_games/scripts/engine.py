class Game:
    def start(self):
        pass

class GameManager:
    def __init__(self):
        self.games = {}
    
    def register_game(self, game_name, game_class):
        self.games[game_name] = game_class()

    def start_game(self, game_name):
        if game_name in self.games:
            self.games[game_name].start()
        else:
            print(f"Game {game_name} is not registered.")
