# Import necessary modules and classes
from Characters.player import Player
from NPCs.quest_giver import QuestGiver
from NPCs.vendor import Vendor
from NPCs.storyteller import Storyteller
from Items.items import Item
from Quests.quest import Quest
from Environments.world import World
from Environments.environment_manager import EnvironmentManager
from Environments.environment import Environment

# Initialize game world
world = World()
starting_environment = Environment("Starting Village", "A peaceful village.")
world.add_environment(starting_environment)

# Initialize player
player = Player("Hero", "Human", "Warrior", inventory=[], equipped={})

# Initialize NPCs
# Note: Implement the loading of dialogue and quests from files as per previous discussion
gandalf = QuestGiver("Gandalf", "A wise wizard.", "gandalf_dialogue.json", quests=[])
balin = Vendor("Balin", "A friendly merchant.", inventory=[Item("Sword", "A sharp blade.", 10)])
aragorn = Storyteller("Aragorn", "A brave ranger.", "aragorn_stories.json")

# Example quest setup
fetch_quest = Quest("Fetch Quest", "Find the hidden treasure in the forest.", "Gandalf", "Treasure Chest", 100)
gandalf.quests.append(fetch_quest)

# Create items
sword = Item("Sword", "A sharp blade.", "Weapon", 10)

# Create vendors
balin = Vendor("Balin", "A friendly merchant.", inventory=[Item("Sword", "A sharp blade.", "Weapon", 10)])
balin.display_items()

# Game loop
while True:
    print("\nWhat would you like to do?")
    action = input("Talk to Gandalf (1), Balin (2), Aragorn (3), Go on a quest (4), Quit (5): ")
    
    if action == "1":
        gandalf.interact(player)
    elif action == "2":
        balin.display_items()
        # Additional logic for buying items
    elif action == "3":
        aragorn.tell_story("legend_of_the_ancient")
    elif action == "4":
        if not fetch_quest.is_completed:
            print("You embark on the quest to find the hidden treasure.")
            # Simulate quest completion
            fetch_quest.complete_quest()
            player.inventory.append(fetch_quest.reward)
            print(f"Quest completed! You found {fetch_quest.reward}.")
        else:
            print("You have already completed this quest.")
    elif action == "5":
        print("Thank you for playing!")
        break
    else:
        print("Invalid action. Please choose again.")

