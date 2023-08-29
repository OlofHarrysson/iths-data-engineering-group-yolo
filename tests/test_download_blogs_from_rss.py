from newsfeed import download_blogs_from_rss


def test_import_project() -> None:
    download_blogs_from_rss.main(blog_names=["mit", "big_data"], save_data=False)
