from datetime import datetime

from airflow.decorators import dag, task, task_group

from newsfeed import download_blogs_from_rss, extract_articles

# from newsfeed import summarize


@task(task_id="download_blogs_from_rss_task")
def download_blogs_from_rss_task():
    download_blogs_from_rss.main(blog_name="mit")
    download_blogs_from_rss.main(blog_name="big_data")


@task(task_id="extract_articles_task")
def extract_articles_task():
    extract_articles.main(blog_name="mit")


@dag(
    dag_id="pipeline",
    start_date=datetime(2023, 9, 7),
    schedule_interval=None,
    catchup=False,
)
def pipeline():
    download_blogs_from_rss_task() >> extract_articles_task()


pipeline = pipeline()
