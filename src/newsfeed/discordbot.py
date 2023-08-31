import argparse
import json
import os
from pathlib import Path

import discord
from discord import SyncWebhook

WEBHOOK_URL = "https://discord.com/api/webhooks/1131522847509069874/Lwk1yVc4w623xpRPkKYu9faFdMNvV5HTZ3TCcL5DgsIgeqhEvo9tBookvuh2S4IWysTt"


def create_embed(blog_name, title, text, link):
    embed = discord.Embed(
        title=title, url="https://news.mit.edu/", description=text, color=discord.Color.blue()
    )
    embed.set_author(name=blog_name)
    embed.set_footer(text="iths-data-engineering-group-yolo")
    return embed


def send_to_discord(embed):
    webhook = SyncWebhook.from_url(WEBHOOK_URL)
    webhook.send(embed=embed)


def main(blog_name):
    summaries_path = Path("data/data_warehouse") / blog_name / "summaries"
    summaries = [file for file in os.listdir(summaries_path) if file.endswith(".json")]

    first_summary = summaries[0]
    with open(os.path.join(summaries_path, first_summary), "r") as f:
        json_data = json.load(f)

        title = json_data.get("title", "missing title")
        text = json_data.get("text", "missing text")
        link = json_data.get("link", "missing link")
        embed = create_embed(blog_name, title, text, link)
        send_to_discord(embed)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--blog_name", type=str, default="mit", choices=["mit", "big_data"])
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(blog_name=args.blog_name)


# if __name__ == "__main__":
# path to summeries
# summeries_path = "data/data_warehouse/mit/summaries"

# makes list of json files @path
# summeries = [file for file in os.listdir(summeries_path) if file.endswith(".json")]

# loops through summeries
# for summery in summeries:
#     with open(summeries_path + "/" + summery, "r") as summery_file:
#         json_data = json.load(summery_file)

# extracts title and text from json file, if no title or text exist sends default message
# title = json_data.get("title", "missing title")
# text = json_data.get("text", "missing text")


# formats string and then send it using discord webhook
# message = f":wave::nerd: \n ***Group:*** iths-data-engineering-group-yolo \n:book:\n ***Blog Title:*** {title} \n:page_facing_up:\n ***Summary:*** {text}"

# webhook = SyncWebhook.from_url(
#     "https://discord.com/api/webhooks/1131522847509069874/Lwk1yVc4w623xpRPkKYu9faFdMNvV5HTZ3TCcL5DgsIgeqhEvo9tBookvuh2S4IWysTt"
# )
# webhook.send(message)
