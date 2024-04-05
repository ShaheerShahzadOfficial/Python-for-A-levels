import inquirer
import random

ARRAY_LENGHT = 3
array = [""] * ARRAY_LENGHT


ADDED_START = 0
ADDED_END = ARRAY_LENGHT - 1

REMOVE_START = 0
REMOVE_END = ARRAY_LENGHT - 1

confirmation = [
    inquirer.List(
        "confirm",
        "Do you want to continue running this program",
        carousel=True,
        choices=["YES", "NO"],
    )
]

choices = [
    inquirer.List(
        "choice",
        "Which Action do you want to perform",
        carousel=True,
        choices=["PUSH", "POP"],
    )
]


sides = [
    inquirer.List(
        "side",
        "Which side do you want your Action to be performed",
        carousel=True,
        choices=["START", "END"],
    )
]


continueFunction = "YES"


# print(continueFunction)


while continueFunction == "YES":
    choice = inquirer.prompt(choices)["choice"]
    if choice == "PUSH":
        side = inquirer.prompt(sides)["side"]
        if side == "START":
            if array[ADDED_START] != "":
                print("Element is Already Present")     
            else:
                array[ADDED_START] = random.randint(1, 100)
                ADDED_START += 1
                if ADDED_START == ARRAY_LENGHT:
                    ADDED_START = 0
                print(array,ADDED_START)
        else:
            if array[ADDED_END] != "":
                print("Element is Already Present")
            else:
                array[ADDED_END] = random.randint(1, 100)
                ADDED_END -= 1
                if ADDED_END == -1:
                    ADDED_END = ARRAY_LENGHT - 1
                print(array)

    else:
        side = inquirer.prompt(sides)["side"]
        if side == "START":
            if array[REMOVE_START] == "":
                print("Element Not Found")
            else:
                array[REMOVE_START] = ""
                REMOVE_START += 1
                if REMOVE_START == ARRAY_LENGHT :
                    REMOVE_START = 0
                print(array)
        else:
            if array[REMOVE_END] == "":
                print("Element Not Found")
            else:
                array[REMOVE_END] = ""
                REMOVE_END -= 1
                if REMOVE_END == -1:
                    REMOVE_END = ARRAY_LENGHT - 1
                print(array)

        continueFunction = inquirer.prompt(confirmation)["confirm"]
        