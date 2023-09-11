import argparse
import json
import os
from pathlib import Path

import discord
from discord import SyncWebhook

from newsfeed.utils import load_files

# from utils import load_files


WEBHOOK_URL_text = "https://discordapp.com/api/webhooks/1150692823516065792/y2sPB3SRB9aLI1iqYI2egHqSP7anjII9c73lQOA-bRsHVjhn9KHf3SLryGqOaT8ourhc"
WEBHOOK_URL_simple = "https://discordapp.com/api/webhooks/1150693022028288054/-PdMDu3IKsfKQnXE3-GpZD1bi3gVPZjcImyNXRbh54AeAfKVd7uuOLdVioC60qygS4hc"


def create_embed(blog_name, title, text, link, date):
    embed = discord.Embed(
        title=title, url=link, description=text, color=discord.Color.blue()  # color=0xFF5733
    )
    embed.set_author(name=blog_name.upper(), url="https://news.mit.edu/")
    embed.add_field(name="Published Date :", value=date, inline=False)
    embed.add_field(
        name="⭐ Presented by : iths-data-engineering-group-yolo ⭐", value=" ", inline=False
    )
    # embed.set_footer(text=" ⭐ Presented by : --iths-data-engineering-group-yolo-- ⭐")
    return embed


def send_to_discord(embed, WEBHOOK_URL):
    webhook = SyncWebhook.from_url(WEBHOOK_URL)
    webhook.send(embed=embed)


def main(blog_name):
    summaries_path = Path("data/data_warehouse") / blog_name / "summaries"

    articles = load_files(summaries_path)

    if articles:
        latest = articles[0]

        if args.summary_type == "text":
            embed = create_embed(
                blog_name, latest["title"], latest["text"], latest["link"], latest["date"]
            )
            send_to_discord(embed, WEBHOOK_URL_text)

        if args.summary_type == "simple":
            embed = create_embed(
                blog_name, latest["title"], latest["simple"], latest["link"], latest["date"]
            )
            send_to_discord(embed, WEBHOOK_URL_simple)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--blog_name", type=str, default="mit", choices=["mit", "big_data"])
    parser.add_argument("--summary_type", type=str, default="text", choices=["text", "simple"])

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(blog_name=args.blog_name)
