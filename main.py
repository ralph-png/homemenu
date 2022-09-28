from random import choice

# Add item or choose item

using = True

while using:

    prompt = input("Would you like a meal idea or add to the menu? (Idea/Change)\n").lower()

    menu = {"easy": ["waffle", "taco", "2", "e"],
            "medium": [],
            "hard": []
            }
    # ToDo 1) Create dictionary of menu choices
    if prompt == "change":
        menuChange = input("Would you like to add or remove a menu item? (Add/Remove)\n").lower()

        if menuChange == "add":

            food = input("What would you like to add to the menu?\n")
            difficulty = input("How difficult is it to make? Easy/Medium/Hard\n").lower()

            menu[difficulty] += [food]

        elif menuChange == "remove":
            #list options or blind

        anotherChange = input("Would you like to make another change? (Yes/No)\n").lower()

        if anotherChange == "yes":
            #return to menuChange prompt

    # ToDo 2) Prompt user for Menu difficulty
    elif prompt == "idea":
        # print(menu.items())
        diffchoice = input("What difficulty food would you like? (Easy/Medium/Hard)\n").lower()
        # print(diffchoice)
        if diffchoice != "easy" and diffchoice != "medium" and diffchoice != "hard":
            print('Please enter "Easy", "Medium", or "Hard"\n')

        # ToDO 3) Randomly choose Menu item with selected difficulty

        print(choice(menu[diffchoice]))

    # ToDO 4) Option to add or remove Menu items
    quitprompt = input("Would you like to quit the app? (Yes/No)\n").lower()
    if quitprompt == "yes":
        using = False
