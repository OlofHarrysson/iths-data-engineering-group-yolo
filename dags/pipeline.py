from datetime import datetime

from airflow.decorators import dag, task

from newsfeed import download_blogs_from_rss, extract_articles, summarize


@task(task_id="download_blogs_from_rss_task", provide_context=True)
def download_blogs_from_rss_task(**kwargs):
    download_blogs_from_rss.main(blog_name="mit")
    download_blogs_from_rss.main(blog_name="big_data")


@task(task_id="extract_articles_task", provide_context=True)
def extract_articles_task(**kwargs):
    extract_articles.main(blog_name="mit")
    extract_articles.main(blog_name="big_data")


@task(task_id="summarize_task", provide_context=True)
def summarize_task(**kwargs):
    summarize.main(blog_name="mit", args=kwargs)
    # summarize.main()


@dag(
    dag_id="pipeline",
    start_date=datetime(2023, 9, 7),
    schedule_interval=None,
    catchup=False,
)
def pipeline():
    download_blogs_from_rss_task() >> extract_articles_task() >> summarize_task()


pipeline = pipeline()
