class Quest:
    def __init__(self, title, description, giver, objective, reward):
        self.title = title
        self.description = description
        self.giver = giver
        self.objective = objective
        self.reward = reward
        self.is_completed = False

    def complete_quest(self):
        self.is_completed = True
        print(f"Quest '{self.title}' completed! Reward: {self.reward}")
