import pendulum
from airflow.sdk import DAG, chain
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    bash_t1_orange = BashOperator(
        task_id="bash_t1_orange",
        bash_command="/opt/airflow_t/plugins/shell/select_fruit.sh ORANGE",
    )

    bash_t2_avocado = BashOperator(
        task_id="bash_t2_avocado",
        bash_command="/opt/airflow_t/plugins/shell/select_fruit.sh AVOCADO",
    )

    bash_t1_orange >> bash_t2_avocado