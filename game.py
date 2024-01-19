# Import necessary libraries
import random
import time

# Game Configuration Data
password_hint = "a popular coding language"
password = "python"
themes = ["Copy Rory’s game", "Dungeons & Dragons", "Murder Mystery", "Who wants to be a Spondoolionaire?"]
procrastinate_options = ["Read a book", "Internet rabbit hole", "Ouija board", "Rubik’s cube"]
energy_loss_per_action = 10

# Login Function: Handles user login with a password hint
def login():
    print("\nWelcome to the game! Please log in to your computer.\n")
    username = input("Enter your username: ")
    while True:
        pwd = input("Enter your password: ")
        if pwd == password:
            print(f"\nWelcome to the Matrix, {username}\n")
            return username
        else:
            print("Incorrect password. Hint:", password_hint)

# Function to Handle Reading Emails
def read_emails():
    print("\nYou have 2 emails in your inbox.\n")
    while True:
        choice = input("Do you want to read the emails? (yes/no): ").lower()
        if choice == "yes":
            print("\nReading emails...\n")
            return handle_emails()
        else:
            print("\nIt might be important. Let's check the emails.\n")

# Function to Handle the Email Logic
def handle_emails():
    # Email 1: Nigerian Prince Scam
    print("Email 1: \nA spam email from a Nigerian Prince claiming you have an inheritance right of 1 million spondooleys.\n")
    choice = input("Do you give bank details or report as spam? (give/report): ").lower()
    if choice == "give":
        print("\nYour bank account is drained of money, you have no will to continue. Game Over.\n")
        return False
    else:
        print("\nEmail reported as spam. Moving to email 2.\n")
        # Email 2: Assignment Email
        print("Email 2: \nAn email from Rory at Digital Hub Jersey giving you an assignment to create a 'choose your own adventure' game.\n")
        while True:
            accept = input("Do you accept the assignment? (yes/no): ").lower()
            if accept == "yes":
                print("\nAssignment accepted. Let's begin.\n")
                print("You have 5 minutes to complete the assignment. Your energy will deplete over time.")
                print("\nHint: You may want to seek inspiration first. However, sometimes procrastination brings forth inspiration in unusual places.\n")
                return True
            else:
                print("\nThen why are you here?\n")

# Function for Seeking Inspiration
def seek_inspiration():
    options = ["Meditate", "Chat to an AI bot", "Take a mysterious pill found in Snow Hill toilets", "Ask a friend"]
    print("\nChoose how to seek inspiration:\n")
    for i, option in enumerate(options, start=1):
        print(f"{i}) {option}")
    choice = input("Choose an option: ")
    if choice in ["1", "2", "3", "4"]:
        theme = random.choice(themes)
        print(f"\nYou {options[int(choice)-1]} and found inspiration to create a game based on '{theme}'\n")
    else:
        print("\nInvalid choice. Please choose again.\n")
        seek_inspiration()

# Function for Procrastination Choices
def procrastinate(inventory, enlightened):
    print("\nChoose how to procrastinate:\n")
    for i, option in enumerate(procrastinate_options, start=1):
        print(f"{i}) {option}")
    choice = input("Choose an option: ")
    if choice == "1":
        print("\nYou are now spiritually enlightened after reading the Bhagavad Gita.\n")
        enlightened = True
        return True, enlightened
    elif choice == "2":
        print("\nYou fall down a rabbit hole of Wiki Leaks information and learn how to break the Matrix. You must create an infinite loop. *Hint* Type 'break the matrix' when doing your assignment.\n")
        return True, enlightened
    elif choice == "3":
        if "talisman" in inventory:
            print("\nThe talisman in your inventory protects you from the Demon from Guernsey. It is sent back to the Underworld.\n")
            return True, enlightened
        else:
            print("\nYou summon a Demon from Guernsey and are haunted for eternity. Game Over.\n")
            return False, enlightened
    elif choice == "4":
        if enlightened:
            print("\nYour spiritual enlightenment helps you solve the Rubik’s cube in record time!\n")
            return True, enlightened
        else:
            print("\nThe Rubik’s cube made you lose track of time! Game Over.\n")
            return False, enlightened
    else:
        print("\nInvalid choice. Please choose again.\n")
        return procrastinate(inventory, enlightened)

# Function for Choosing Assignment Theme
def choose_assignment():
    print("\nChoose the theme for your assignment:\n")
    for i, theme in enumerate(themes, start=1):
        print(f"{i}) {theme}")
    while True:
        choice = input("Type your choice: ")
        if choice in ["1", "2", "3", "4", "break the matrix"]:
            theme = themes[int(choice) - 1] if choice != "break the matrix" else "Break the matrix"
            print(f"\nYou have chosen to create a game based on '{theme}'\n")
            return theme
        else:
            print("\nInvalid choice. Please choose again.\n")

# Function for Handling Assignment Progress
def do_assignment(theme, progress):
    progress += 1/3
    print(f"\nYou worked on your assignment: {theme}. Progress: {progress*100:.0f}%\n")
    if progress >= 1:
        if theme == "Break the matrix":
            print("Well done you discombobulated the Matrix. You have created an infinite existential loop in which the protagonist in your game is yourself coding yourself into existence for all eternity.\n")
        else:
            print("Well done you passed your assignment\n")
        return progress, True
    else:
        print("\nYour energy levels are low, you must take a rest.\n")
        return progress, False

# Function for Taking a Break
def take_break(inventory):
    options = ["Buy more time", "Walk on the beach", "Eat a delicious feast", "Drink an espresso"]
    print("\nChoose how to take a break:\n")
    for i, option in enumerate(options, start=1):
        print(f"{i}) {option}")
    choice = input("Choose an option: ")
    if choice == "1":
        print("\nYou go to the market and mistakenly buy some thyme. Time reset.\n")
        return True
    elif choice == "2":
        if "talisman" not in inventory:
            print("\nYou walk on the beach and ponder about life. You find a talisman and add it to your inventory.\n")
            inventory.append("talisman")
        else:
            print("\nYou walk on the beach and ponder about life.\n")
        return False
    elif choice == "3":
        print("\nYou ate a delicious feast and are feeling rested.\n")
        return False
    elif choice == "4":
        print("\nYou drink an espresso and feel rejuvenated.\n")
        return False
    else:
        print("\nInvalid choice. Please choose again.\n")
        return take_break(inventory)

# Function for Game Over Scenario
def game_over():
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice == "yes":
        main()
    else:
        print("\nThanks for playing!\n")

# Main Game Function
def main():
    username = login()
    if not read_emails():
        game_over()
        return

    # Initialize game variables
    energy = 100
    start_time = time.time()
    assignment_theme = None
    progress = 0
    completed_assignment_section = False
    inventory = []
    enlightened = False

    while True:
        # Check time and energy constraints
        if time.time() - start_time > 300:
            print("\nTime's up! Assignment failed.\n")
            game_over()
            break
        if energy <= 50:
            print("\nEnergy too low. You must take a break.\n")

        # Player action choices
        print("\nChoose an action:\n")
        print("A) Seek Inspiration")
        print("B) Procrastinate")
        print("C) Do the Assignment")
        print("D) Take a Break")
        choice = input("Enter your choice: ").upper()

        if choice == "A":
            if not completed_assignment_section:
                seek_inspiration()
            else:
                print("\nYou should take a break before continuing.\n")
        elif choice == "B":
            if not completed_assignment_section:
                continue_game, enlightened = procrastinate(inventory, enlightened)
                if not continue_game:
                    game_over()
                    break
            else:
                print("\nYou should take a break before continuing.\n")
        elif choice == "C":
            if not assignment_theme:
                assignment_theme = choose_assignment()
            if not completed_assignment_section:
                progress, completed = do_assignment(assignment_theme, progress)
                if completed:
                    game_over()
                    break
                completed_assignment_section = True
            else:
                print("\nYou must take a break before continuing your assignment.\n")
        elif choice == "D":
            if take_break(inventory):
                start_time = time.time()  # Reset timer if they bought thyme
            energy = 100
            completed_assignment_section = False
        else:
            print("\nInvalid choice, try again.\n")

        # Reduce energy after each action
        energy -= energy_loss_per_action

# Start the game when the script is executed
if __name__ == "__main__":
    main()