import json
from time import sleep
user_list = "list_items.json"

tasks = {
    "to_do": [],
    "completed" : []
}

global get_task

def greeting():
    print(f"Welcome! You don't have anything on your list.")

def menu():

    useraction = input("What would you like to do? \n"
                       "1. Add another task\n"
                       "2. Complete a task\n"
                       "3. Quit\n"
                       "4. Clear the entire list\n"
                       "5. Clear the completed list\n"
                       "6. Display the list\n"
                       "Answer: ")

    if useraction == "1":
        add_to_todo()
    elif useraction == "2":
        complete_task()
        save_list()
    elif useraction == "3":
        print("slay those dragons!")
        return
    elif useraction == "4":
        clear_all()
        save_list()
    elif useraction == "5":
        clear_completed()
        save_list()
    elif useraction == "6":
        display_list()
    else:
        return

def add_to_todo():
    print("press 'q' to quit")
    while True:
        get_task = input("What would you like to accomplish?\n"
                         "Goal:")
        answer = get_task
        tasks["to_do"] += [answer]
        if get_task == "q":
            tasks["to_do"].pop()
            print("Here is your list!\n")
            save_list()
            n = 0
            for i in tasks["to_do"]:
                n += 1
                print(f"{n}. {i}")
            print("\n")
            break


#move task from to do to completed

def complete_task():
    get_task = input("Which task did you complete?\n"
                     "Answer:")
    answer = get_task
    for i in tasks["to_do"]:
        if i == answer:
            tasks["to_do"].remove(i)
            tasks["completed"] += [answer]
    with open(user_list, 'w') as list:
        save_list()
    print(f"successfully completed {answer}\n")
    sleep(2)
    menu()

#clear items in completed list

def clear_completed():
    tasks["completed"].clear()

def clear_all():
    tasks["completed"].clear()
    tasks["to_do"].clear()
    menu()

#save list to 'list_items.json

def save_list():
    with open(user_list, 'w') as list:
        json.dump(tasks, list)
        list.close()

#display contents of list_items.json

def load_list():
    #this assigns the list from 'list_items.json' a vriable
    with open(user_list, 'r') as list:
        tasks = json.load(list)
    return tasks

def display_list():
    with open(user_list, 'r') as list:
        tasks = json.load(list)
    list_counter()
    menu()

def list_counter():
    n = 0
    for i in tasks["to_do"]:
        n += 1
        print(f"{n}. {i} \n")
    print("\n")


#this assigns a variable to the results of the list loaded from list_items.json
tasks = load_list()
#if tasks is blank, initiate adding to the list
if tasks == {
    "to_do": [],
    "completed" : []
}:
    add_to_todo()
    save_list()
else:
    menu()

#print the tasks left to do. Iterate and count them.
    # print("Here are your current incomplete tasks:\n")
    # n = 0
    # for i in tasks["to_do"]:
    #     n += 1
    #     print(f"{n}. {i}")
    # print("\n")

