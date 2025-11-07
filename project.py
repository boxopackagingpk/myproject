from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "cisco"
}

connection = ConnectHandler(**device)
ping_result = connection.send_command("ping 8.8.8.8 repeat 5")
print(ping_result)
connection.disconnect()

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





