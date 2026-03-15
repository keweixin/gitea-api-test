import yaml

def load_yaml_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def load_yaml_cases(file_path, case_group):
    data = load_yaml_file(file_path)
    return data.get(case_group, [])
