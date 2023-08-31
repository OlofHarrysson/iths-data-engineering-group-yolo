import json
import os

from transformers import PegasusForConditionalGeneration, PegasusTokenizer


def summerise_text_local(blog_text):
    model_name = "google/pegasus-cnn_dailymail"
    model = PegasusForConditionalGeneration.from_pretrained(model_name)
    tokenizer = PegasusTokenizer.from_pretrained(model_name)

    sim_prompt = "Summerise this text: " + blog_text

    # Generate simplified summary
    inputs = tokenizer.encode(sim_prompt, return_tensors="pt", max_length=300, truncation=True)
    summary = model.generate(
        inputs,
        max_length=150,
        num_return_sequences=1,
        length_penalty=2.5,
        num_beams=3,
        early_stopping=True,
    )
    summary_text = tokenizer.decode(summary[0], skip_special_tokens=True)

    return summary_text
