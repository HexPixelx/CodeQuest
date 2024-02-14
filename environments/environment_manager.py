class EnvironmentManager:
    def __init__(self):
        self.environments = {}  # Key: environment name, Value: Environment object

    def add_environment(self, environment):
        self.environments[environment.name] = environment

    def display_environment_info(self, name):
        if name in self.environments:
            self.environments[name].display_info()
        else:
            print("Environment does not exist.")

    # Add methods to manage dynamic changes, such as time of day or special events
