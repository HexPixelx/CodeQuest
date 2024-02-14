import random

class Player:
    def __init__(self, name, race, character_class, level=1, inventory=None, equipped=None):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = level
        self.health = 100
        self.attack_power = 10
        self.inventory = inventory if inventory is not None else []
        self.equipped = equipped if equipped is not None else {}
        self.abilities = self.set_abilities()
        self.traits = self.set_traits()
        self.fate = self.set_fate()
        self.stats = {
            "HP": 100,
            "MP": 20,
            "strength": 12,
            "dexterity": 10,
            "intelligence": 8,
            "luck": 5
        }
        self.skills = {
            "combat": ["swordsmanship", "archery"],
            "non-combat": ["lockpicking", "persuasion"],
        }

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
        """Display detailed information about the character."""
        print(f"Name: {self.name}, Race: {self.race}, Class: {self.character_class}, Level: {self.level}")
        print(f"Health: {self.stats['HP']}, MP: {self.stats['MP']}")
        print(f"Abilities: {', '.join(self.abilities)}")
        print(f"Trait: {self.traits}")
        print(f"Fate: {self.fate}")
        # Display inventory and equipped items if desired

    # Example method to add items to the inventory
    def add_item_to_inventory(self, item):
        """Add an item to the player's inventory."""
        self.inventory.append(item)
        print(f"Added {item.name} to inventory.")

    # Example method to equip an item from the inventory
    def equip_item(self, item_name):
        """Equip an item from the inventory."""
        for item in self.inventory:
            if item.name == item_name:
                self.equipped[item.type] = item
                print(f"Equipped {item.name}.")
                break
