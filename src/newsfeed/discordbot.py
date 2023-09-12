import argparse
import os
import threading
from pathlib import Path

import discord
from discord import SyncWebhook
from googletrans import Translator

from newsfeed.utils import load_files

# from utils import load_files


WEBHOOK_URL_text = "https://discordapp.com/api/webhooks/1150692823516065792/y2sPB3SRB9aLI1iqYI2egHqSP7anjII9c73lQOA-bRsHVjhn9KHf3SLryGqOaT8ourhc"
WEBHOOK_URL_simple = "https://discordapp.com/api/webhooks/1150693022028288054/-PdMDu3IKsfKQnXE3-GpZD1bi3gVPZjcImyNXRbh54AeAfKVd7uuOLdVioC60qygS4hc"


def create_embed(blog_name, title, text, link, date, language="en"):
    if language == "sv":
        published = "Publiceringsdatum"
        group = "Presenterat av"
    else:
        published = "Published Date"
        group = "Presented by"

    embed = discord.Embed(
        title=title, url=link, description=text, color=discord.Color.blue()  # color=0xFF5733
    )
    embed.set_author(name=blog_name.upper(), url="https://news.mit.edu/")
    embed.add_field(name=f"{published}:", value=date, inline=False)
    embed.add_field(name=f"⭐ {group} : iths-data-engineering-group-yolo ⭐", value=" ", inline=False)
    # embed.set_footer(text=" ⭐ Presented by : --iths-data-engineering-group-yolo-- ⭐")
    return embed


def send_to_discord(embed, WEBHOOK_URL):
    webhook = SyncWebhook.from_url(WEBHOOK_URL)
    webhook.send(embed=embed)


def send_english_summaries(blog_name, latest):
    embed_text_en = create_embed(
        blog_name, latest["title"], latest["text"], latest["link"], latest["date"]
    )

    embed_simple_en = create_embed(
        blog_name, latest["title"], latest["simple"], latest["link"], latest["date"]
    )

    threading.Thread(target=send_to_discord, args=(embed_text_en, WEBHOOK_URL_text)).start()
    threading.Thread(target=send_to_discord, args=(embed_simple_en, WEBHOOK_URL_simple)).start()


def send_swedish_summaries(blog_name, latest):
    translator = Translator()
    swedish_title = translator.translate(latest["title"], src="en", dest="sv").text
    swedish_text = translator.translate(latest["text"], src="en", dest="sv").text
    swedish_simple = translator.translate(latest["simple"], src="en", dest="sv").text

    embed_text_sv = create_embed(
        blog_name, swedish_title, swedish_text, latest["link"], latest["date"], language="sv"
    )

    embed_simple_sv = create_embed(
        blog_name, swedish_title, swedish_simple, latest["link"], latest["date"], language="sv"
    )

    threading.Thread(target=send_to_discord, args=(embed_text_sv, WEBHOOK_URL_text)).start()
    threading.Thread(target=send_to_discord, args=(embed_simple_sv, WEBHOOK_URL_simple)).start()


def main(blog_name, language="en"):
    summaries_path = Path("data/data_warehouse") / blog_name / "summaries"

    articles = load_files(summaries_path)

    if articles:
        latest = articles[0]
        if language == "sv":
            send_swedish_summaries(blog_name, latest)
        else:
            send_english_summaries(blog_name, latest)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--blog_name", type=str, default="mit", choices=["mit", "big_data"])
    parser.add_argument("--language", type=str, default="en", choices=["en", "sv"])

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(blog_name=args.blog_name, language=args.language)
