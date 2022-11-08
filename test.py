import json
from colorama import Fore
from os import system as sys

def get_data():
    with open("data.json", "r") as f:
        datas = json.load(f)
    return datas

sys("cls")

a = None
b = None
c = None

while 1:
    name = input(f"{Fore.LIGHTGREEN_EX}Name: ")
    pulish_time = input("Publish time: ")
    if pulish_time == "":
        pulish_time=a
    pulisher = input("Publisher: ")
    if pulisher == "":
        pulisher=b
    author = input("Author: ")
    if author == "":
        author=c

    a = pulish_time
    b = pulisher
    c = author

    datas = get_data()

    datas[name] = {}
    datas[name]["publish_time"] = pulish_time
    datas[name]["publisher"] = pulisher
    datas[name]["author"] = author

    with open("data.json", "w") as f:
        json.dump(datas, f)

    print("-----------------------")