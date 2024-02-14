class User:
    def __init__(self, username):
        self.username = username
        self.score = 0
        self.inventory = []
        self.equipped = {}  # Could be structured as {'weapon': None, 'armor': None}

    def update_score(self, points):
        self.score += points
        print(f"{self.username}'s new score: {self.score}")

    def add_item_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item.name} added to {self.username}'s inventory.")

    def use_item(self, item_name):
        # Find and use the item from the inventory
        for item in self.inventory:
            if item.name == item_name and isinstance(item, Potion):
                item.use(self)
                self.inventory.remove(item)
                break
