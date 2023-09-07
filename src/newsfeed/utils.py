import json
import os


def load_files(path):
    results = []

    files = [file for file in os.listdir(path) if file.endswith(".json")]

    for file in files:
        with open(os.path.join(path, file), "r") as combined_file:
            json_data = json.load(combined_file)

        title = json_data.get("title")
        text = json_data.get("text")

        results.append((title, text))

    return results
