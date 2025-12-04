import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 30
        self.inventory = []

    def is_alive(self):
        return self.health > 0


class Enemy:
    def __init__(self, name, health, dmg_range):
        self.name = name
        self.health = health
        self.dmg_range = dmg_range

    def attack(self):
        return random.randint(*self.dmg_range)


def slow_print(text, delay=0.03):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()


def battle(player, enemy):
    slow_print(f"\n⚔️ A wild {enemy.name} appears!")
    while enemy.health > 0 and player.is_alive():
        slow_print(f"\nYour HP: {player.health} | {enemy.name} HP: {enemy.health}")
        slow_print("Choose an action:\n1. Attack\n2. Heal\n> ", 0.01)
        choice = input()

        if choice == "1":
            dmg = random.randint(4, 8)
            enemy.health -= dmg
            slow_print(f"You strike the {enemy.name} for {dmg} damage!")
        elif choice == "2":
            heal = random.randint(5, 10)
            player.health += heal
            slow_print(f"You heal yourself for {heal} HP.")
        else:
            slow_print("Invalid choice, turn wasted...")

        if enemy.health > 0:
            edmg = enemy.attack()
            player.health -= edmg
            slow_print(f"The {enemy.name} hits you for {edmg} damage!")

    return player.is_alive()


def game():
    slow_print("🗺️ Welcome, traveler. What is your name?")
    name = input("> ")
    player = Player(name)
    slow_print(f"Greetings, {name}. Your journey begins...\n")

    time.sleep(1)

    slow_print("You enter a dark forest. The wind whispers your name.")
    time.sleep(1)

    enemies = [
        Enemy("Goblin", 15, (3, 6)),
        Enemy("Wolf", 18, (2, 8)),
        Enemy("Forest Spirit", 22, (4, 9))
    ]

    for enemy in enemies:
        alive = battle(player, enemy)
        if not alive:
            slow_print("\n💀 You have fallen... The forest claims another soul.")
            return
        else:
            slow_print(f"\n🏆 You defeated the {enemy.name}!")
            item = random.choice(["Healing Potion", "Magic Leaf", "Iron Dagger"])
            player.inventory.append(item)
            slow_print(f"You found a {item}!")

    slow_print("\n🌟 After defeating all foes, you find a glowing portal.")
    slow_print("You step through it and vanish into legend...")
    slow_print("\n🎉 THE END 🎉")


if __name__ == "__main__":
    game()

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "password"
}

conn = ConnectHandler(**device)
conn.enable()

config = conn.send_command("show running-config")

with open("backup_config.txt", "w") as f:
    f.write(config)

conn.disconnect()
ckground='black', foreground='cyan')
label.pack(anchor='center')

time()
root.mainloop()




for member in root:
    if member.tag == '{' + ns0 + '}entry':
        for element in member:
            if element.tag == '{' + ns0 + '}content':
                data_line = []

                for field in element[0]:            
                    for count in range(0, len(field_tag)):
                        if field.tag == '{' + ns2 + '}' + field_tag[count]:
                            data_line.append(field.text)

import json

FILE = "todo_list.json"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    task = input("Enter a new task: ")
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"✅ '{task}' added.\n")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.\n")
        return
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

while True:
    print("\n--- CALCULATOR ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = input("Enter choice: ")

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
    elif choice == "5":
        break
    else:
        print("Invalid choice!")








