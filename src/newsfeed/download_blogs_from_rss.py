import argparse
from pathlib import Path

import requests

LINK_TO_XML_FILE = {
    "mit": "https://news.mit.edu/rss/topic/artificial-intelligence2",
    "big_data": "https://news.mit.edu/rss/topic/big-data",
}


def get_metadata_info(blog_name):
    assert (
        blog_name in LINK_TO_XML_FILE
    ), f"{blog_name=} not supported. Supported blogs: {list(LINK_TO_XML_FILE)}"
    blog_url = LINK_TO_XML_FILE[blog_name]
    response = requests.get(blog_url)
    xml_text = response.text
    return xml_text


def save_metadata_info(xml_text, blog_name):
    path_xml_dir = Path("data/data_lake") / blog_name
    path_xml_dir.mkdir(exist_ok=True, parents=True)
    with open(path_xml_dir / "metadata.xml", "w") as f:
        f.write(xml_text)


def main(blog_names, save_data=True):
    for blog_name in blog_names:
        print(f"Processing {blog_name}")
        xml_text = get_metadata_info(blog_name)
        if save_data == True:
            save_metadata_info(xml_text, blog_name)
        print(f"Done processing {blog_name}")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--blog_names", type=str, default=["mit", "big_data"])
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(blog_names=args.blog_names)
