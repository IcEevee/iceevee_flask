import json
from colorama import Fore
from os import system as sys

def get_data():
    with open("data.json", "r") as f:
        datas = json.load(f)
    return datas

sys("cls")

while 1:
    name = input(f"{Fore.GREEN}Name: ")
    pulish_time = input("Publish time: ")
    pulisher = input("Publisher: ")
    author = input("Author: ")

    datas = get_data()

    datas[name] = {}
    datas[name]["publish_time"] = pulish_time
    datas[name]["publisher"] = pulisher
    datas[name]["author"] = author

    with open("data.json", "w") as f:
        json.dump(datas, f)

    print("-----------------------")