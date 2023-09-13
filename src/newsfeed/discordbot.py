import argparse
import os
import threading
from pathlib import Path

import discord
from discord import SyncWebhook

from newsfeed.utils import load_files

# from utils import load_files


WEBHOOK_URL_text = "https://discordapp.com/api/webhooks/1150692823516065792/y2sPB3SRB9aLI1iqYI2egHqSP7anjII9c73lQOA-bRsHVjhn9KHf3SLryGqOaT8ourhc"
WEBHOOK_URL_simple = "https://discordapp.com/api/webhooks/1150693022028288054/-PdMDu3IKsfKQnXE3-GpZD1bi3gVPZjcImyNXRbh54AeAfKVd7uuOLdVioC60qygS4hc"
WEBHOOK_URL_swe = "https://discord.com/api/webhooks/1151478775863853067/-50Xwsf78QXySUn73B8GJW6-DXhVJHL28AHSoC_CBlouuGm2uKEQncI5e4MC81-KOGDs"


def create_embed(blog_name, title, text, link, date):
    embed = discord.Embed(
        title=title, url=link, description=text, color=discord.Color.blue()  # color=0xFF5733
    )
    embed.set_author(name=blog_name.upper(), url="https://news.mit.edu/")
    embed.add_field(name="Published date:", value=date, inline=False)
    embed.add_field(
        name="⭐ Presented by: iths-data-engineering-group-yolo ⭐", value=" ", inline=False
    )
    return embed


def send_to_discord(embed, WEBHOOK_URL):
    webhook = SyncWebhook.from_url(WEBHOOK_URL)
    webhook.send(embed=embed)


def send_summaries(blog_name, latest):
    embed_text_en = create_embed(
        blog_name, latest["title"], latest["text"], latest["link"], latest["date"]
    )

    embed_simple_en = create_embed(
        blog_name, latest["title"], latest["simple"], latest["link"], latest["date"]
    )

    embed_swe = create_embed(
        blog_name, latest["swe_title"], latest["swedish"], latest["link"], latest["date"]
    )

    threading.Thread(target=send_to_discord, args=(embed_text_en, WEBHOOK_URL_text)).start()
    threading.Thread(target=send_to_discord, args=(embed_simple_en, WEBHOOK_URL_simple)).start()
    threading.Thread(target=send_to_discord, args=(embed_swe, WEBHOOK_URL_swe)).start()


def main(blog_name):
    summaries_path = Path("data/data_warehouse") / blog_name / "summaries"

    articles = load_files(summaries_path)

    latest = articles[0]

    sum = send_summaries(blog_name, latest)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--blog_name", type=str, default="mit", choices=["mit", "big_data"])
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(blog_name=args.blog_name)
