import json
import os

from discord import SyncWebhook
from utils import load_files

if __name__ == "__main__":
    # path to summeries
    summeries_path = "data/data_warehouse/mit/summaries"

    articles = load_files(summeries_path)

    """# makes list of json files @path
    summeries = [file for file in os.listdir(summeries_path) if file.endswith(".json")]

    # loops through summeries
    for summery in summeries:
        with open(summeries_path + "/" + summery, "r") as summery_file:
            json_data = json.load(summery_file)

        # extracts title and text from json file, if no title or text exist sends default message
        title = json_data.get("title", "missing title")
        text = json_data.get("text", "missing text")"""

    for article in articles:
        # formats string and then send it using discord webhook
        message = f":wave::nerd: \n ***Group:*** iths-data-engineering-group-yolo \n:book:\n ***Blog Title:*** {article[0]} \n:page_facing_up:\n ***Summary:*** {article[1]}"

        webhook = SyncWebhook.from_url(
            "https://discord.com/api/webhooks/1131522847509069874/Lwk1yVc4w623xpRPkKYu9faFdMNvV5HTZ3TCcL5DgsIgeqhEvo9tBookvuh2S4IWysTt"
        )
        webhook.send(message)
