class Environment:
    def __init__(self, name, description, interactables=None, npcs=None, effects=None, connections=None):
        self.name = name
        self.description = description
        self.interactables = interactables if interactables is not None else {}
        self.npcs = npcs if npcs is not None else {}
        self.effects = effects if effects is not None else []
        self.connections = connections if connections is not None else {}

    def add_interactable(self, name, interactable):
        """Add an interactable object to the environment."""
        self.interactables[name] = interactable

    def add_npc(self, name, npc):
        """Add an NPC to the environment."""
        self.npcs[name] = npc

    def add_effect(self, effect):
        """Add an environmental effect."""
        self.effects.append(effect)

    def connect_environment(self, direction, environment):
        """Connect this environment to another, facilitating player movement."""
        self.connections[direction] = environment

    def display_info(self):
        """Display detailed information about the environment."""
        print(f"Location: {self.name}")
        print(f"Description: {self.description}")
        if self.effects:
            print("Effects: " + ", ".join(self.effects))
        if self.interactables:
            print("Interactables: " + ", ".join(self.interactables.keys()))
        if self.npcs:
            print("NPCs: " + ", ".join(self.npcs.keys()))
        if self.connections:
            print("Connections: " + ", ".join(f"{direction} to {environment.name}" for direction, environment in self.connections.items()))
