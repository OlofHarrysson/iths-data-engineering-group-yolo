from datetime import datetime

from airflow.decorators import dag, task

from newsfeed import discordbot, download_blogs_from_rss, extract_articles, summarize


@task(task_id="download_blogs_from_rss_task")
def download_blogs_from_rss_task():
    download_blogs_from_rss.main(blog_name="mit")
    download_blogs_from_rss.main(blog_name="big_data")


@task(task_id="extract_articles_task")
def extract_articles_task():
    extract_articles.main(blog_name="mit")
    extract_articles.main(blog_name="big_data")


@task(task_id="summarize_task")
def summarize_task():
    summarize.main(blog_name="mit", model_type="gpt")
    summarize.main(blog_name="big_data", model_type="gpt")


@task(task_id="discord_task")
def discord_task():
    discordbot.main(blog_name="mit")


@dag(
    dag_id="pipeline",
    start_date=datetime(2023, 9, 8),
    schedule_interval=None,
    catchup=False,
)
def pipeline():
    download_blogs_from_rss_task() >> extract_articles_task() >> summarize_task() >> discord_task()


pipeline = pipeline()
