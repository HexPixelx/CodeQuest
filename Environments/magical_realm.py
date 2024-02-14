from environment import Environment

class MagicalRealm(Environment):
    def __init__(self, name, description, interactables=None, npcs=None, effects=None, connections=None, magic_effect=None):
        super().__init__(name, description, interactables, npcs, effects, connections)
        self.magic_effect = magic_effect

    def add_magic_effect(self, effect):
        """Add a magic effect specific to the magical realm."""
        self.magic_effect = effect

    def display_info(self):
        """Display detailed information about the magical realm, including magic effects."""
        super().display_info()
        print(f"Magic Effect: {self.magic_effect}")

    # Additional methods specific to magical realms can be implemented here

