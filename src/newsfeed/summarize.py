import os

import openai
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY
print(OPENAI_API_KEY)


def summarize_text(blog_text, token=4000):
    prompt = f"Summerize the following text very consise: '{blog_text}'"

    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=token)

    summary = response.choices[0].text.strip()
    return summary


if __name__ == "__main__":
    blog_text = input("Enter the blog text that you want to summarize:\n")
    summary = summarize_text(blog_text)
    print("\nGenerated Summary:", summary)
