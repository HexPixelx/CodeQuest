from characters.player import Player
from environments.world import Environment

def main():
    print("Welcome to RPG Adventure!")
    name = input("Enter your character's name: ")
    character_class = input("Choose your class (Warrior, Mage, Archer): ")
    player = Player(name, character_class)

    starting_environment = Environment("Starting Village", "A peaceful village with friendly folk.")
    player.display_character()
    starting_environment.display_environment()

    # Game loop for actions
    while True:
        action = input("What would you like to do? (explore, rest, quit): ")
        if action == "quit":
            print("Thanks for playing!")
            break
        elif action == "explore":
            print("You explore the surrounding area.")
        elif action == "rest":
            print("You rest and recover your strength.")
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()
