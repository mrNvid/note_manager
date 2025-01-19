import yaml
def load_notes_from_file(filename):
    with open("config.yaml", "r") as file:
        data = yaml.safe_load(file)