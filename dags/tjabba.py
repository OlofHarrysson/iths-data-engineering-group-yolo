from datetime import datetime

from airflow import DAG
from airflow.decorators import dag, task


@dag(dag_id="test_tjabba", schedule_interval=None, start_date=datetime(2023, 9, 6), catchup=False)
def test_tjabba_dag():
    @task
    def test_tjabba():
        print("Tjabba")

    test_task = test_tjabba()


test_tjabba_dag = test_tjabba_dag()
