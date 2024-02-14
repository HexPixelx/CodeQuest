class Item:
    def __init__(self, name, description, item_type, price):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.price = price

    def display_info(self):
        print(f"Item: {self.name}")
        print(f"Description: {self.description}")
        print(f"Type: {self.item_type}")
        print(f"Price: {self.price} gold")

# Example subclass for a specific type of item, like a potion
class Potion(Item):
    def __init__(self, name, description, potency, price):
        super().__init__(name, description, "Potion", price)
        self.potency = potency

    def use(self, player):
        # Implement the effect of using the potion, e.g., restore health
        print(f"{player.username} uses {self.name}, restoring {self.potency} health.")

# Example subclass for weapons
class Weapon(Item):
    def __init__(self, name, description, damage, price):
        super().__init__(name, description, "Weapon", price)
        self.damage = damage

    def display_info(self):
        super().display_info()
        print(f"Damage: {self.damage}")
