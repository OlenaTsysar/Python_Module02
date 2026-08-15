
import os
import json

from datetime import datetime

FILE_NAME = os.path.join(os.path.dirname(__file__), "game_results.json")

def save_result(name, rounds: int, score: int):
    result = {
        "Дата": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Игрок": name,
        "Количество раундов": rounds,
        "Итоговый счет": score
    }

    results = []

    with open(FILE_NAME, "r", encoding="UTF-8") as file:
        results = json.load(file)

    results.append(result)

    with open(FILE_NAME, "w", encoding="UTF-8") as file:
        json.dump(results, file, indent = 4, ensure_ascii=False)

def get_results():

    with open(FILE_NAME, "r", encoding="UTF-8") as file:
        results = json.load(file)

    for item in results:
        print("-" * 40)
        print(f"Дата: {item['Дата']}")
        print(f"Игрок: {item['Игрок']}")
        print(f"Количество раундов: {item['Количество раундов']}")
        print(f"Итоговый счет: {item['Итоговый счет']}")
