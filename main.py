import json
from colorama import Fore

#opens the json file
print(Fore.LIGHTBLACK_EX + "initializing data...")

with open("data.json" , "r") as f:
    data = json.load(f)

    print(Fore.GREEN + "data successfully initialized")


def console():

    image = input(Fore.WHITE)

    for image in data["json"]:
        
        print(Fore.LIGHTBLACK_EX + "keyword found!\nprinting..")
        input()

    else:
        print(Fore.RED + "not found")
        input()


console()