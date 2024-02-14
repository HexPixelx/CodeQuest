class Vendor:
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        self.inventory = inventory  # Inventory is a list of items the vendor can sell

    def display_items(self):
        """Show the items available for sale."""
        print(f"{self.name} offers the following items for sale:")
        for item in self.inventory:
            print(f"- {item.name} at {item.price} gold each.")

    def sell_item(self, item_name, player):
        """Process the sale of an item to a player."""
        for item in self.inventory:
            if item.name == item_name:
                if player.gold >= item.price:
                    player.gold -= item.price
                    player.inventory.append(item)
                    print(f"{player.name} has purchased {item.name} for {item.price} gold.")
                    break
                else:
                    print("You do not have enough gold.")
                    break
        else:
            print("Item not found.")
