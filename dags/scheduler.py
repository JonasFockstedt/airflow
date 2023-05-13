import datetime
import os
import pendulum
from airflow.decorators import dag, task

@dag(
    dag_id="schedule-training",
    schedule_interval="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
)
def ScheduleTraining():

    @task
    def print_models():
        json_path = "/opt/airflow/dags/models.json"
        #print(f"PRINTING CURRENT DIR\n{os.getcwd()}")
        with open(json_path, "r") as file:
           print(file.read()) 


    print_models()


dag = ScheduleTraining()
