import random
import time



class Player:
    def __init__(self, name):
        self.name = name
        self.health = 30

    def alive(self):
        return self.health > 0


class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        return random.randint(3, 8)


def battle(player, enemy):
    print(f"\n⚔️ {enemy.name} appears!")

    while enemy.hp > 0 and player.alive():
        print(f"Your HP: {player.health} | {enemy.name} HP: {enemy.hp}")
        choice = input("1.Attack  2.Heal: ")

        if choice == "1":
            dmg = random.randint(4, 8)
            enemy.hp -= dmg
            print("You hit for", dmg)
        elif choice == "2":
            heal = random.randint(5, 10)
            player.health += heal
            print("You healed", heal)

        if enemy.hp > 0:
            edmg = enemy.attack()
            player.health -= edmg
            print("Enemy hits for", edmg)

    return player.alive()


def game():
    name = input("Enter your hero name: ")
    player = Player(name)

    enemies = [
        Enemy("Goblin", 15),
        Enemy("Wolf", 18),
        Enemy("Spirit", 20)
    ]

    for enemy in enemies:
        if not battle(player, enemy):
            print("💀 You died!")
            return

    print("🏆 You won the game!")


# ---------------- MAIN ----------------

while True:
    print("\n1.Register\n2.Login\n3.Exit")
    ch = input("Choose: ")

    if ch == "1":
        register()

    elif ch == "2":
        if login():
            print("🎉 Login successful! Starting game...")
            game()
        else:
            print("❌ Wrong credentials")

    elif ch == "3":
        break
