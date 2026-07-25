
from game.models import Player, Computer
from game.settings import GAME_LEVELS, GAME_LEVELS_CONVERT

from game.game import start_game
from game.score import get_results

def main():

    while True:

        igra = input("Vvedite svoi vibor:" \
        "       1.Играть." \
        "       2.Посмотреть результаты." \
        "       3.Выйти. ")

        if igra == "1":
            start_game()
        elif igra == "2":
            get_results()
        elif igra == "3":
            print("dosvidanija")
            break
        else:
            print("Nevernii vibor")

        continue


if __name__ == "__main__":
    main()