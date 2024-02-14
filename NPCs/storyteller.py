import json
import os

class Storyteller:
    def __init__(self, name, description, stories_file):
        self.name = name
        self.description = description
        self.stories = self.load_stories(stories_file)

    def load_stories(self, stories_file):
        file_path = os.path.join(os.path.dirname(__file__), "..", "Dialogue", stories_file)
        with open(file_path, 'r') as file:
            return json.load(file)

    def tell_story(self, story_name):
        if story_name in self.stories:
            print(self.stories[story_name])
        else:
            print(f"Sorry, the story '{story_name}' is not available.")

# Example usage:
# aragorn = Storyteller("Aragorn", "A brave ranger.", "aragorn_stories.json")
# aragorn.tell_story("legend_of_the_ancient")

