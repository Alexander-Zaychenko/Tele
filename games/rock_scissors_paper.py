from random import randint

# 1 - камень
# 2 - ножницы
# 3 - бумага
rsp = {0: "бумага", 1: "камень", 2: "ножницы", 3: "бумага", 4:"камень"}


def engine(computer_choice, player_choice):
    if player_choice < 4 and player_choice > 0:
        if computer_choice == player_choice:
            return f"Ничья! Выбор компьютера: {rsp[computer_choice]}"
        elif computer_choice == 1 and player_choice == 2 or computer_choice == 2 and player_choice == 3 or computer_choice == 3 and player_choice == 1:
            return f"Поражение! Выбор компьютера: {rsp[computer_choice]}"
        elif computer_choice == 2 and player_choice == 1 or computer_choice == 3 and player_choice == 2 or computer_choice == 1 and player_choice == 3:
            return f"Победа! Выбор компьютера: {rsp[computer_choice]}"
    else:
        return "Ошибка! "


def engine_hard(computer_choice, player_choice):
    if player_choice < 4 and player_choice > 0:
        if computer_choice == 9:
            return f"Ничья! Выбор компьютера: {rsp[player_choice]}"
        elif computer_choice < 9:
            return f"Поражение! Выбор компьютера: {rsp[player_choice + 1]}"
        elif computer_choice == 10:
            return f"Победа! Выбор компьютера: {rsp[player_choice - 1]}"

def in_game(player_choice):
    computer_choice = randint(1, 3)
    return engine(computer_choice, int(player_choice))