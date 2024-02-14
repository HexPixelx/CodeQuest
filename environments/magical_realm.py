from .environment import Environment

class MagicalRealm(Environment):
    def __init__(self, name, description, magic_effect):
        super().__init__(name, description)
        self.magic_effect = magic_effect

    def display_info(self):
        super().display_info()
        print(f"Magic Effect: {self.magic_effect}")

    # You can add methods specific to magical realms here, such as applying effects
