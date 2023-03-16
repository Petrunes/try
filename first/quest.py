import random as rd


HP = 0
GOLD = 0
POWER = 0
# LUCK = 0


def menu_stats():
    print(f"У Вас {HP} здоровья, {POWER} силы и {GOLD} монет.")


def print_hp():
    print("У Вас", HP, "здоровья.")


def print_power():
    print("У Вас", POWER, "силы.")


def print_gold():
    print("У Вас", GOLD, "монет.")


# встреча с торговцем
def meet_shop():
    global HP
    global POWER
    global GOLD

    def buy(cost):
        global GOLD
        if GOLD >= cost:
            GOLD -= cost
            print_gold()
            return True
        print("У вас не хватает монет!")
        return False

    weaponLvl = rd.randint(1, 3)
    weaponDmg = rd.randint(1, 5) * weaponLvl
    weapons = ["Жезл", "Меч", "Кинжал", "Лук", "Арбалет", "Трезубец"]
    weaponRarities = ["Обычный", "Редкий", "Легендарный"]
    weaponRarity = weaponRarities[weaponLvl - 1]
    weaponCost = rd.randint(3, 10) * weaponLvl
    weapon = rd.choice(weapons)

    oneHpCost = 5
    threeHpCost = 12

    print("Вы встретили странствующих торговцев!")
    menu_stats()

    while input("Хотите поторговать (1-да/2-нет): ") == "1":
        print("1 - Малое зелье лечения(добавит одну еденицу здоровья) -", oneHpCost, "монет;")
        print("2 - Большое зелье лечения(добавит три еденицы здоровья) -", threeHpCost, "монет;")
        print(f"3 - {weaponRarity} {weapon} - {weaponCost} монет;")

        choice = input("Что вы хотите приобрести: ")
        if choice == "1":
            if buy(oneHpCost):
                HP += 1
                print_hp()
        elif choice == "2":
            if buy(threeHpCost):
                HP += 3
                print_hp()
        elif choice == "3":
            if buy(weaponCost):
                POWER = weaponDmg
                print_power()
        else:
            print("Я такое не продаю")


# встреча с врагами
def meet_enemy():
    global HP
    global GOLD

    monsterLvl = rd.randint(1, 3)
    monsterHp = monsterLvl
    monsterDmg = monsterLvl * 2 - 1
    monsters = ["Гоблин", "Скелет-воин", "Разбойник", "Волк", "Орк", "Некромант"]

    monster = rd.choice(monsters)

    print(
        f"Вы встретили врага - {monster}, у него {monsterLvl} уровень, {monsterHp} жизней и {monsterDmg} силы. Готовьтесь к бою")
    menu_stats()

    while monsterHp > 0:
        choice = input("Что будете делать (1-в бой/2-бежать/3-подкуп): ")

        if choice == "1":
            monsterHp -= POWER
            print("Вы атаковали врага и у него осталось", monsterHp, "здоровья.")
        elif choice == "2":
            chance = rd.randint(0, monsterLvl)
            if chance == 0:
                print("Вам удалось сбежать с поля боя!")
                break
            else:
                print("Монстр оказался чересчур сильным и догнал Вас...")
        elif choice == "3":
            GOLD -= 3
            print("Вы подкупили монстра заплатив 3 монеты и он оставил вас в покое")
            print_gold()
            break
        else:
            continue

        if monsterHp > 0:
            HP -= monsterDmg
            print("Монстр атаковал и у вас осталось", HP, "здоровья.")

        if HP <= 0:
            break
    else:
        loot = rd.randint(0, 2) + monsterLvl
        GOLD += loot
        print("Вам удалось одолеть врага, за что вы получили", loot, "монет.")
        print_gold()


def meet_container():
    global HP
    global GOLD
    situation = rd.randint(1, 5)
    container_description = ['кучу мусора', 'нору барсука', 'бочку', 'дупло', 'разбитую телегу']
    if situation == 1:
        print(f"В пути вы видите {rd.choices(container_description, [0.2, 0.2, 0.2, 0.2, 0.2, ])},"
              f" исследовав это, вы нашли малое зелье здоровья, здоровье повышено на 1 еденицу")
        HP += 1
        print_hp()
    elif situation == 2:
        print(f"В пути вы видите {rd.choices(container_description, [0.2, 0.2, 0.2, 0.2, 0.2,])},"
              f" исследовав это, вы нашли кошель монет, у вас на 3 монеты больше")
        GOLD += 3
        print_gold()
    else:
        print(f"Вы видите {rd.choices(container_description, [0.2, 0.2, 0.2, 0.2, 0.2,])}, исследовав это, вы ничего не находите...")


# создание начальных характеристик персонажа и инициализация игры
def init_game(hp, gold, power):
    global HP
    global GOLD
    global POWER

    HP = hp
    GOLD = gold
    POWER = power

    print("Вы отправляетесь в путь, навстречу приключениям и опасностям. Удачного путешествия!")
    menu_stats()


# создание одного игрового цикла-хода
def game_loop():
    situation = rd.randint(0, 10)
    local_description = ['вы не видите ничего особенного', 'вы видите чьи-то кости', 'вы видите жирную крысу',
                       'вы видите дерьмо гоблина', 'вы видите кактус', 'вы видите перекати-поле',
                       'вы видите ворону', 'вы видите какие-то развалины']
    if situation == 0:
        meet_shop()
    elif situation == 1:
        meet_enemy()
    elif situation == 2:
        meet_container()
    else:
        input(f"В пути {rd.choices(local_description, [0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,])}, можно идти дальше...")


# инициализация новой игры и создание бесконечного цикла
init_game(5, 10, 3)

while True:
    game_loop()
    if HP <= 0:
        if input("Хотите начать сначала? (да:нажать-1/нет:нажать-2)") == '1':
            init_game(5, 10, 3)
        else:
            print("game over")
            break
