class User:
    def __init__(self, username):
        self.username = username
        self.score = 0

    def update_score(self, points):
        self.score += points
        print(f"{self.username}'s new score: {self.score}")
