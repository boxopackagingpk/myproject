import requests
import xml.etree.ElementTree as ET
import csv

from requests_ntlm import HttpNtlmAuth

schema XML microsoft 
ns0 = "http://www.w3.org/2005/Atom"
ns1 = "http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"
ns2 = "http://schemas.microsoft.com/ado/2007/08/dataservices"

Create csv file 
csv_file = open('file_name_csv.csv', 'w', newline = '', encoding='ansi')
csvwriter = csv.writer(csv_file)

col_names = ['Col_1', 'Col_2', 'Col_3', 'Col_n']
csvwriter.writerow(col_names)

field_tag = ['dado_1', 'dado_2', 'dado_3', 'dado_n']


response = requests.get("your_url", auth=HttpNtlmAuth('xxxx\\username','password'))
tree =  ET.ElementTree(ET.fromstring(response.content))
tree.write('file_name_xml.xml')
root = tree.getroot()

schema XML microsoft 
ns0 = "http://www.w3.org/2005/Atom"
ns1 = "http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"
ns2 = "http://schemas.microsoft.com/ado/2007/08/dataservices"
schema XML microsoft 
ns0 = "http://www.w3.org/2005/Atom"
ns1 = "http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"
ns2 = "http://schemas.microsoft.com/ado/2007/08/dataservices"

Create csv file 
csv_file = open('file_name_csv.csv', 'w', newline = '', encoding='ansi')
csvwriter = csv.writer(csv_file)

col_names = ['Col_1', 'Col_2', 'Col_3', 'Col_n']
csvwriter.writerow(col_names)

field_tag = ['dado_1', 'dado_2', 'dado_3', 'dado_n']

Create csv file 
csv_file = open('file_name_csv.csv', 'w', newline = '', encoding='ansi')
csvwriter = csv.writer(csv_file)

col_names = ['Col_1', 'Col_2', 'Col_3', 'Col_n']
csvwriter.writerow(col_names)

field_tag = ['dado_1', 'dado_2', 'dado_3', 'dado_n']
from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=('calibri', 50, 'bold'), background='black', foreground='cyan')
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
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")
    print()

def mark_done():
    tasks = load_tasks()
    view_tasks()
    num = int(input("Enter task number to mark done: ")) - 1
    if 0 <= num < len(tasks):
        tasks[num]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!\n")

def main():
    while True:
        print("1. Add Task\n2. View Tasks\n3. Mark Done\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()

csv_file.close()

import random

def roll_dice(num_dice=3):
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    return rolls, sum(rolls)

results, total = roll_dice()
print("🎲 Rolls:", results, "| Total:", total)



