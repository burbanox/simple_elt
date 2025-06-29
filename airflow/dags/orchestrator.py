
from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
import subprocess
from docker.types import Mount




def run_etl_script():
    script_path='/opt/airflow/etl/etl.py'
    result = subprocess.run(["python3",script_path],capture_output=True,text=True)

    if result.returncode !=0:
        raise Exception(result.stderr)
    
    print(result.stdout)




default_args ={
    'description': 'A simple DAG',
    'start_date':datetime(2025,6,28),
    'catchup':False,
}


dag = DAG(
    dag_id='films_dag_orchestaror',
    default_args=default_args,
    schedule=timedelta(minutes=1),
    catchup=False
)

with dag:
    task1 = PythonOperator(
        task_id='run_etl_script',
        python_callable=run_etl_script
    )

    task2 = DockerOperator(
        task_id='dbt_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/code',
        mounts=[
            Mount(
                source='/home/burbanox/data-engineer-journey/first_etl/dbt/my_dbt_project',
                target='/code',
                type='bind'
            ),
            Mount(
                source='/home/burbanox/data-engineer-journey/first_etl/dbt/profiles.yml',
                target='/root/.dbt/profiles.yml',
                type='bind'
            )
        ],
        network_mode='first_etl_etl_network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
    )


    task1 >> task2