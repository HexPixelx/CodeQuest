import os
import json


class QuestGiver:
    def __init__(self, name, description, dialogue_file, quests):
        self.name = name
        self.description = description
        self.dialogue_file = os.path.join(os.path.dirname(
            __file__), "..", "Dialogue", dialogue_file)
        self.quests = quests
        self.load_dialogue()

    def load_dialogue(self):
        try:
            with open(self.dialogue_file, 'r') as file:
                self.dialogue = json.load(file)  # Assign loaded dialogue to self.dialogue
        except FileNotFoundError:
            print(f"Error: Dialogue file '{self.dialogue_file}' not found.")
            self.dialogue = {}

    def interact(self, player):
        current_state = "initial_greeting"  # Start at the beginning
        while True:
            if current_state in self.dialogue:
                print(self.dialogue[current_state])
                if isinstance(self.dialogue[current_state], dict):  # Choice offered
                    options = self.dialogue[current_state]["options"]
                    for key, text in options.items():
                        print(f"({key}): {text}")
                    choice = input("> ").lower() 
                    current_state = options.get(choice, "invalid_choice")  # Handle invalid choice
                else: 
                    input("Press Enter to continue...")  # Non-choice dialogue  
                    break  # Exit once all dialogue is shown
            else:
                print(f"Error: State '{current_state}' not found in dialogue.")
                break  # Exit if state not found

# Example usage:
# gandalf = QuestGiver("Gandalf", "A wise wizard.", "gandalf_dialogue.json", quests=[])
# gandalf.interact(player)
