#!/usr/bin/python3

import sys
import json
import os

def main():
    
    my_dict = get_todos()
    store_todos(my_dict)
   # display_todos()


def get_todos():
    my_dict = {}
    if os.path.isfile("todo.json"):
        with open("todo.json", "r") as file:
            my_dict = json.load(file)

    my_dict["TODO"] = "STATUS"

    if len(sys.argv) == 1:
        display_todos()
    elif len(sys.argv) > 1 and not len(sys.argv) == 3:
        print("Todo and status required")
    else:
        todo = sys.argv[1]
        status = sys.argv[2]
        my_dict[todo] = status

    return my_dict


def store_todos(my_dict):

    with open("todo.json", "w") as file:
        json.dump(my_dict, file, indent=3)


def display_todos():

    with open("todo.json", "r") as file:
        data = json.load(file)

    for key, value in data.items():
        print(f"{key}:\t{value}")
    


if __name__ == "__main__":
    main()
