# Script AirFlow do grupo:
# Jenifer Caroline Correa da Silva - RM 338631
# Leonardo Simões- RM 337598
# Márcio Amaral - RM 338396
# Mayara Lopes Pires - RM 336697
# Importando as bibliotecas
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
# definição de argumentos básicos
default_args = {
    'owner': 'dataops_11abd',
    'depends_on_past': False,
    'start_date': datetime(2021, 5, 2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
# Criação da DAG Semanal
with DAG('talend_api_jobs',
         schedule_interval='@weekly',
         default_args=default_args
         ) as dag:

    mensal = BashOperator(
        task_id='talend_semanal',
        bash_command="""
        cd $AIRFLOW_HOME/dags/etl_scripts/diario
        unzip -zxvf Curated_Product_Sales_0.1.zip
        cd $AIRFLOW_HOME/dags/etl_scripts/diario/Curated_Product_Sales_0.1/Curated_Product_Sales/
        chmod 775 Curated_Product_Sales_run.sh
        ./Curated_Product_Sales_run.sh
        """)
