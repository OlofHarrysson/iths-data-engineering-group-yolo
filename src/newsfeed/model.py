import json
import os

from transformers import PegasusForConditionalGeneration, PegasusTokenizer


class TextSummarizer:
    def __init__(self) -> None:
        self.model_name = "google/pegasus-cnn_dailymail"
        self.model = PegasusForConditionalGeneration.from_pretrained(self.model_name)
        self.tokenizer = PegasusTokenizer.from_pretrained(self.model_name)

    def summerize_text_local(self, blog_text, non_technical=False):
        if non_technical:
            sim_prompt = "Summerise this text for a child: " + blog_text
            max_length = 150
        else:
            sim_prompt = "Summerise this text concisely: " + blog_text
            max_length = 150

        inputs = self.tokenizer.encode(
            sim_prompt, return_tensors="pt", max_length=300, truncation=True
        )
        summary = self.model.generate(
            inputs,
            max_length=max_length,
            num_return_sequences=1,
            length_penalty=2.5,
            num_beams=3,
            early_stopping=True,
        )
        summary_text = self.tokenizer.decode(summary[0], skip_special_tokens=True)

        return summary_text
