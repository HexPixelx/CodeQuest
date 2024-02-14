from .environment_manager import EnvironmentManager

class World:
    def __init__(self):
        self.environment_manager = EnvironmentManager()  # Manages all environments within the world
        self.global_weather = None  # Weather affecting the entire world, can override local weather
        self.time_of_day = 'Day'  # Global time of day

    def set_global_weather(self, weather):
        """Set the weather affecting the entire world."""
        self.global_weather = weather
        print(f"The global weather has changed to {self.global_weather}.")
        # Optionally update all environments with the new global weather
        for environment in self.environment_manager.environments.values():
            environment.set_weather(self.global_weather)

    def toggle_global_day_night(self):
        """Toggle the global time of day between day and night."""
        self.time_of_day = 'Night' if self.time_of_day == 'Day' else 'Day'
        print(f"It is now {self.time_of_day} globally.")
        # Optionally update the time of day in all environments
        for environment in self.environment_manager.environments.values():
            environment.time_of_day = self.time_of_day

    def display_world_info(self):
        """Display information about the world, including global conditions."""
        print(f"Global Weather: {self.global_weather}")
        print(f"Global Time of Day: {self.time_of_day}")
        # Display information about all environments within the world
        for name, environment in self.environment_manager.environments.items():
            print(f"--- Environment: {name} ---")
            environment.display_info()

    def add_environment(self, environment):
        """Add an environment to the world via the environment manager."""
        self.environment_manager.add_environment(environment)
