import random

class Player:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = 100
        self.attack_power = 10
        self.inventory = []
        self.abilities = self.set_abilities()
        self.traits = self.set_traits()
        self.fate = self.set_fate()

    def set_abilities(self):
        """Assign special abilities based on character class."""
        abilities = {
            'Warrior': ['Power Strike', 'Shield Wall'],
            'Mage': ['Fireball', 'Teleport'],
            'Archer': ['Piercing Arrow', 'Eagle Eye']
        }
        return abilities.get(self.character_class, [])

    def set_traits(self):
        """Assign passive traits based on character class."""
        traits = {
            'Warrior': 'Stalwart - Less damage from attacks',
            'Mage': 'Arcane Insight - Chance to double spell power',
            'Archer': 'Quickfoot - Dodge enemy attacks more easily'
        }
        return traits.get(self.character_class, '')

    def set_fate(self):
        """Assign a random fate attribute that affects game dynamics."""
        fates = [
            'Lucky - Finds more gold',
            'Cursed - Encounters tougher enemies',
            'Blessed - Health regenerates over time',
            'Doomed - Randomly suffers minor damage'
        ]
        return random.choice(fates)

    def display_character(self):
        super().display_character()
        print(f"Abilities: {', '.join(self.abilities)}")
        print(f"Trait: {self.traits}")
        print(f"Fate: {self.fate}")

    # Add methods for using abilities and traits here

