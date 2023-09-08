import json
import os


def load_files(path):
    results = []

    files = [file for file in os.listdir(path) if file.endswith(".json")]

    for file in files:
        with open(os.path.join(path, file), "r") as combined_file:
            json_data = json.load(combined_file)

        results.append(
            {
                "title": json_data.get("title"),
                "text": json_data.get("text"),
                "simple": json_data.get("simple", "missing"),
                "link": json_data.get("link", "missing"),
                "date": json_data.get("published", "missing"),
            }
        )

    results = sorted(results, key=lambda x: x["date"], reverse=True)

    return results
