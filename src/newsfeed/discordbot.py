import argparse
import json
import os
from pathlib import Path

import discord
from discord import SyncWebhook
from utils import load_files

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1143848187539509299/TWwa_kiI4Fbb2g59mod_rG9zRxNc3WSVMPkbfk9xhAi-7X017ZGvmxZ6CIYJrk0n52_c"


def create_embed(blog_name, title, text, link):
    embed = discord.Embed(
        title=title, url=link, description=text, color=discord.Color.blue()  # color=0xFF5733
    )
    embed.set_author(name=blog_name.upper(), url="https://news.mit.edu/")
    embed.set_footer(text=" ⭐ Presented by : iths-data-engineering-group-yolo ⭐")
    return embed


def send_to_discord(embed):
    webhook = SyncWebhook.from_url(WEBHOOK_URL)
    webhook.send(embed=embed)


def main(blog_name):
    summaries_path = Path("data/data_warehouse") / blog_name / "summaries"
    # summaries = [file for file in os.listdir(summaries_path) if file.endswith(".json")]
    articles = load_files(summaries_path)

    first_summary = articles[2]
    # with open(os.path.join(summaries_path, first_summary), "r") as f:
    # json_data = json.load(f)

    # title = json_data["title"]
    title = first_summary[0]
    print(title)
    # text = json_data["text"]
    text = first_summary[1]
    # link = json_data["link"]
    link = "https://news.mit.edu/2023/honing-robot-perception-mapping-0710"
    embed = create_embed(blog_name, title, text, link)
    send_to_discord(embed)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--blog_name", type=str, default="mit", choices=["mit", "big_data"])
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(blog_name=args.blog_name)
