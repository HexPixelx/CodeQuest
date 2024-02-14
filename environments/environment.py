class Environment:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Location: {self.name}")
        print(f"{self.description}")
