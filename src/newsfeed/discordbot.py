import argparse
import json
import os
from pathlib import Path

import discord
from discord import SyncWebhook
from utils import load_files

from newsfeed.utils import load_files

WEBHOOK_URL = "https://discord.com/api/webhooks/1131522847509069874/Lwk1yVc4w623xpRPkKYu9faFdMNvV5HTZ3TCcL5DgsIgeqhEvo9tBookvuh2S4IWysTt"


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


def send_to_discord(embed):
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
            send_to_discord(embed)

        if args.summary_type == "simple":
            embed = create_embed(
                blog_name, latest["title"], latest["simple"], latest["link"], latest["date"]
            )
            send_to_discord(embed)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--blog_name", type=str, default="mit", choices=["mit", "big_data"])
    parser.add_argument("--summary_type", type=str, default="text", choices=["text", "simple"])

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(blog_name=args.blog_name)
