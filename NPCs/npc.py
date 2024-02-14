class NPC:
    def __init__(self, name, description, dialogue_tree, inventory=None, quests=None):
        self.name = name
        self.description = description
        self.dialogue_tree = dialogue_tree  # A nested structure for complex dialogues
        self.inventory = inventory if inventory is not None else []
        self.quests = quests if quests is not None else []

    def interact(self, player):
        # Implement interaction logic, possibly using the dialogue_tree for conversation
        pass

    def trade(self, player, item_name):
        # Implement trading logic, allowing players to buy/sell items
        pass

    def give_quest(self, player):
        # Select and assign a quest to the player
        pass
