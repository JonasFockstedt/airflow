import datetime
import requests
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
        json_path = "https://raw.githubusercontent.com/JonasFockstedt/airflow/main/models.json"
        
        response = requests.get(json_path)

        print(response.text)

        #with open(json_path, "r") as file:
           #print(file.read()) 


    print_models()


dag = ScheduleTraining()
