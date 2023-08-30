# import modules
import argparse
import json
import os
from pathlib import Path

import openai
from dotenv import load_dotenv

from newsfeed.datatypes import BlogInfo, BlogSummary

# load environment variable from .env file
load_dotenv()

# retrive api key from from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# set api key for making api requests
openai.api_key = OPENAI_API_KEY


# Define a function to summarize text using Openai's API
def summarize_text(blog_text):
    # create prompt for the api request
    prompt = f"Summarize the following text : {blog_text}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    # extract and return the genereted summary
    summary = response.choices[0].message["content"].strip()
    return summary


def load_articles(blog_name):
    articles_path = Path("data/data_warehouse") / blog_name / "articles"

    article_files = [file for file in os.listdir(articles_path) if file.endswith(".json")]

    return article_files


def extract_summaries_from_articles(article_files, blog_name):
    summaries = []
    # try:
    for article_file in article_files:
        with open(Path("data/data_warehouse", blog_name, "articles", article_file), "r") as f:
            article_data = json.load(f)

        blog_text = article_data["blog_text"]
        summary = summarize_text(blog_text)
        article_title = article_data["title"]
        unique_id = article_data["unique_id"]

        blog_summary = BlogSummary(unique_id=unique_id, title=article_title, text=summary)
        print(blog_summary)
        summaries.append(blog_summary)

    # except FileExistsError:
    # print("Summary already exists")

    return summaries


def save_summaries(summaries, blog_name):
    save_dir = Path("data/data_warehouse", blog_name, "summaries")
    save_dir.mkdir(exist_ok=True, parents=True)
    for summary in summaries:
        save_path = save_dir / summary.get_filename()
        with open(save_path, "w") as f:
            f.write(summary.json(indent=2))


def main(blog_name):
    print(f"Processing {blog_name}")
    article_files = load_articles(blog_name)
    summaries = extract_summaries_from_articles(article_files, blog_name)
    save_summaries(summaries, blog_name)
    print(f"Done processing {blog_name}")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--blog_name", type=str, default="mit", choices=["mit", "big_data"])
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(blog_name=args.blog_name)
