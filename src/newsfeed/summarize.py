# import modules
import json
import os

import openai
from dotenv import load_dotenv

from newsfeed.datatypes import BlogInfo, BlogSummary

# load environment variable from .env file
load_dotenv()

# retrive api key from from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# set api key for making api requests
openai.api_key = OPENAI_API_KEY

# print open_api_key
print(OPENAI_API_KEY)


# Define a function to summarize text using Openai's API
def summarize_text(blog_text):
    # create prompt for the api request
    prompt = f"Summerize the following text : ==={blog_text}=== .summary"

    # creates a GPT-3.5 text completion request using the Openai api.
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt)

    # extract and return the genereted summary
    summary = response.choices[0].text.strip()
    return summary


if __name__ == "__main__":
    # define the directory for articles in the data warehouse
    articles_dir = "data/data_warehouse/mit/articles"

    # define the directory for saving summaries in the data warehouse
    summaries_dir = "data/data_warehouse/mit/summaries"
    os.makedirs(summaries_dir, exist_ok=True)  # creates summaryies directories

    article_files = [
        file for file in os.listdir(articles_dir) if file.endswith(".json")
    ]  # list all article files

    for article_file in article_files:
        with open(os.path.join(articles_dir, article_file), "r") as f:
            article_data = json.load(f)

        # Get article content
        blog_text = article_data["blog_text"]

        # Generate summary
        summary = summarize_text(blog_text)

        # Get article metadata from the JSON data
        article_title = article_data["title"]
        unique_id = article_data["unique_id"]

        # Create a BlogSummary instance
        blog_summary = BlogSummary(unique_id=unique_id, title=article_title, text=summary)

        # Save the summary to the summaries directory in the data warehouse
        summary_filename = blog_summary.get_filename()
        with open(os.path.join(summaries_dir, summary_filename), "w") as f:
            json.dump(blog_summary.dict(), f, indent=4)

        print(f"Summary saved for '{article_title}'")
