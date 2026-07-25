import random
from datetime import datetime

from .models import Player, Computer
from .settings import GAME_LEVELS, GAME_LEVELS_CONVERT
from .score import save_result
# from .exceptions import InvalidInputError, InvalidRollError

def choose_level():

    while True:

        level = input("Выберите уровень игры: " \
                    "1 - 5 игр, " \
                    "2 - 8 игр, " \
                    "3 - 10 игр ")

        if level in GAME_LEVELS:
            print(f"игра будет длиной в {GAME_LEVELS[level]} раундов (режим {GAME_LEVELS_CONVERT[GAME_LEVELS[level]]})")
            return GAME_LEVELS[level]
     
        else:
            print("Неверный выбор!")


def choose():
    while True:

        # try:
        value = input("Кинуть кубик (нажмите Enter): ")

        if value != "":
            print("Бросок не сделан!!! Нажмите 'Enter' для повторного броска.")
            continue

        break
        # except InvalidRollError as error:
        #     print(error)


def start_game():

    name = input("vvedite imja igroka: ")
    rounds = choose_level()

    player = Player(name)
    computer = Computer()

    start_time = datetime.now().strftime("%Y.%m.%d %H:%M:%S")

    temp_round = 1

    while temp_round <= rounds:
        print(f"Раунд {temp_round}")
        choose()
        player_value = player.cube()
        print(f"Вы бросили кубик: 🎲 {player_value}")
        computer_value = computer.cube()
        print(f"Компьютер бросил кубик: 🎲 {computer_value}")
        temp_score = player_value - computer_value
        print(temp_score)
        if temp_score != 0:
            player.check(temp_score)
            temp_round +=1
        else:
            continue


    print("\nИгра окончена")
    print(f"Дата начала игры: {start_time}")
    print(f"Игрок: {player.name}")
    print(f"Уровень: {GAME_LEVELS_CONVERT[rounds]}")
    print(f"Финальный счет: {player.score}")  

    save_result(name, rounds, player.score)










