from engine import GameManager
from games.brain_even2 import EvenNumGame
from games.brain_calc2 import MathExpresGame

if __name__ == '__main__':
    manager = GameManager()
    manager.register_game("EvenNumGame", EvenNumGame)
    manager.register_game("MathExpresGame", MathExpresGame)
    manager.start_game("EvenNumGame")
    manager.start_game("MathExpresGame")