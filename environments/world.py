class Environment:
    def __init__(self, name, description, is_magical=False):
        self.name = name
        self.description = description
        self.is_magical = is_magical
        self.weather = None
        self.time_of_day = 'Day'

    def set_weather(self, weather):
        self.weather = weather
        print(f"The weather in {self.name} has changed to {self.weather}.")

    def toggle_day_night(self):
        self.time_of_day = 'Night' if self.time_of_day == 'Day' else 'Day'
        print(f"It is now {self.time_of_day} in {self.name}.")

    def display_environment(self):
        super().display_environment()
        if self.is_magical:
            print("This place is imbued with magic, altering reality in unseen ways.")
        if self.weather:
            print(f"Weather: {self.weather}")
        print(f"Time of Day: {self.time_of_day}")

    # Additional methods to interact with the environment
