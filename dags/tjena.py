from datetime import datetime

from airflow.decorators import dag, task

from newsfeed.tjena_test import test_tjena_src


@dag(dag_id="test_tjena", schedule_interval=None, start_date=datetime(2023, 9, 6), catchup=False)
def test_tjena_dag():
    @task
    def test_tjena():
        return test_tjena_src()

    test_task_tjena = test_tjena()


test_tjena_dag = test_tjena_dag()
