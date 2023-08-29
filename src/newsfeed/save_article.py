import json
import os

# path to summariezed articles
input_directory = "data/data_warehouse/mit/summaries"
# output path
parent_directory = "data/saved_articles"

# loop to iterate through
for filename in os.listdir(input_directory):
    # creating file path
    file = os.path.join(parent_directory, filename)

    # checking to make suree file has been created correctly
    if os.path.isfile:
        print(f"{file}")
