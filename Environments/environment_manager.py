import json
from .environment import Environment

class EnvironmentManager:
    def __init__(self):
        self.environments = {}  # Key: environment name, Value: Environment object
        self.current_time = "Day"  # Example for handling time of day

    def load_environments_from_file(self, filepath):
        """Load environment data from an external file and create environment instances."""
        with open(filepath, 'r') as file:
            environments_data = json.load(file)
            for env_data in environments_data:
                self.add_environment(Environment(**env_data))

    def add_environment(self, environment):
        """Add a new environment."""
        self.environments[environment.name] = environment

    def remove_environment(self, name):
        """Remove an environment by name."""
        if name in self.environments:
            del self.environments[name]
        else:
            print(f"Environment '{name}' does not exist.")

    def update_environment(self, name, **updates):
        """Update properties of an existing environment."""
        if name in self.environments:
            environment = self.environments[name]
            for key, value in updates.items():
                setattr(environment, key, value)
        else:
            print(f"Environment '{name}' does not exist.")

    def display_environment_info(self, name):
        """Display information about a specific environment."""
        if name in self.environments:
            self.environments[name].display_info()
        else:
            print("Environment does not exist.")

    def change_time_of_day(self, time):
        """Simulate time of day changes across all environments."""
        self.current_time = time
        # Optionally update environments based on the new time of day
        print(f"Time of day changed to {time}.")

    def trigger_event(self, event_name, environment_name):
        """Trigger a specific event in a given environment."""
        if environment_name in self.environments:
            # This assumes an environment can handle a 'trigger_event' method
            self.environments[environment_name].trigger_event(event_name)
        else:
            print(f"Environment '{environment_name}' does not exist.")

    def find_environments_by_feature(self, feature):
        """Find and list environments that contain a specific feature."""
        matching_envs = [name for name, env in self.environments.items() if feature in getattr(env, 'features', [])]
        if matching_envs:
            print("Matching environments:", ", ".join(matching_envs))
        else:
            print("No matching environments found.")

    def connect_environments(self, env_name1, direction, env_name2):
        """Connect two environments, allowing navigation between them."""
        if env_name1 in self.environments and env_name2 in self.environments:
            self.environments[env_name1].connect_environment(direction, self.environments[env_name2])
        else:
            print("One or both specified environments do not exist.")

# Example of extending the combat system to consider environmental factors
def adjust_combat_for_environment(player, enemy, current_environment):
    # Modify combat dynamics based on the current environment
    if current_environment.effects.include("swamp"):
        # Adjust combat stats for swamp environment
        pass
    # Additional environment-specific adjustments can be added here
