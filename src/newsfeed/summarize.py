# import modules
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
def summarize_text(blog_text, token=4000):
    # create prompt for the api request
    prompt = f"Summerize the following text very consise: '{blog_text}'"

    # creates a GPT-3.5 text completion request using the Openai api.
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=token)

    # extract and return the genereted summary
    summary = response.choices[0].text.strip()
    return summary


if __name__ == "__main__":
    ## Prompt the user to input the blog text to be summarized
    blog_text = input("Enter the blog text that you want to summarize:\n")

    # call the summarize function to generate summary
    summary = summarize_text(blog_text)

    # print the generated summary
    print("\nGenerated Summary:", summary)
