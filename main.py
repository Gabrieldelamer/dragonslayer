import random

hp: int = 20
monster_counter: int = 0
attack: int = 3


def figth():
    monster_health: int = random.randint(1, 7)
    monster_health_damage: int = monster_health
    monster_attack: int = random.randint(1, 3)
    round_counter: int = 0
    while monster_health_damage >= 0:
        round_counter = round_counter + 1
        monster_health_damage = monster_health_damage - attack
    global hp, monster_counter
    hp = hp - round_counter * monster_attack
    monster_counter = monster_counter + 1
    if hp <= 0:
        print("Вы не справились с натиском даракона и погибли")
    else:
        print("Вы сразились со свирепым драконом и потеряли", round_counter * monster_attack, "здоровья. Крепитесь.")


def input_controller() -> int:
    while True:
        try:
            input_key = int(input())
            assert 0 < input_key <= 2
        except ValueError:
            print("Нужно ввести число 1 или 2")
        except AssertionError:
            print("Нужно ввести число 1 или 2")
        else:
            return abs(input_key)


def get_sword():
    global attack
    sword_attack_expander: int = random.randint(1, 7)
    print("Вы нашли меч с атакой", sword_attack_expander, "!")
    print("Если хотите взять его и выкинуть текущий меч с атакой,", attack, "нажмите 1.")
    print("Если хотите оставить текущий меч, с атакой", attack, ",нажмите 2.")
    action = input_controller()
    if action == 1:
        attack = sword_attack_expander
        print("Вы подобрали новый меч! Теперь сила вашей атаки равняется.", attack)
    else:
        print("Вы оставили свой меч у себя.")


def get_hp():
    hp_upper: int = random.randint(2, 6)

    def food_selector(upper):
        if upper == 2:
            print("По дороге вы нашли поле земляники!")
        if upper == 3:
            print("По дороге вы нашли яблоко!")
        if upper == 4:
            print("По дороге вы нашли яица перепелки!")
        if upper == 5:
            print("По дороге вы поймали молодого кабана!")
        if upper == 6:
            print("По дороге вам встретился лекарь, который дал вам волшебное снадобье!")

    global hp
    hp = hp + hp_upper
    food_selector(hp_upper)
    print("Теперь ваше здоровье", hp)


def event_selector(event: int):
    event_on_the_road: int = random.randint(0, 1)
    if event == 1:
        figth()
        player_status()
    if event == 2:
        if event_on_the_road == 0:
            get_sword()
            player_status()
        if event_on_the_road == 1:
            get_hp()
            player_status()


def player_status():
    global hp, attack, monster_counter
    print('Здоровье', hp, 'Атака', attack, 'Убито драконов', monster_counter)


def game():
    global monster_counter, attack, hp
    print('Приветствую вас в игре "Герои и Драконы!"')
    player_status()
    while monster_counter < 10 and hp > 0:
        print("Выберите действие. Для того, чтобы сразиться с драконом, введите 1. Чтобы пойти дальше, введите 2.")
        event_selector(input_controller())
    if monster_counter == 10 and hp > 0:
        print('Поздравляем! Вы победили всех драконов!')
    elif hp <= 0:
        print('Вы проиграли!')


game()
