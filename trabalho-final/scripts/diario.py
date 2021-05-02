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
# Criação da DAG Diário
with DAG('talend_api_jobs',
         schedule_interval='@daily',
         default_args=default_args
         ) as dag:

    diarioRawData = BashOperator(
        task_id='talend_diario_raw',
        bash_command="""
        cd $AIRFLOW_HOME/dags/etl_scripts/diario
        unzip -zxvf Raw_Data_01.zip
        cd  $AIRFLOW_HOME/dags/etl_scripts/diario/Raw_Data_01/Raw_Data/
        chmod 775 Raw_Data_run.sh
        ./Raw_Data_run.sh
        """)
    diarioHarmonized = BashOperator(
        task_id='talend_diario_harmonized',
        bash_command="""
        cd $AIRFLOW_HOME/dags/etl_scripts/diario
        unzip -zxvf Harmonized_Data_0.1.zip
        cd  $AIRFLOW_HOME/dags/etl_scripts/diario/Harmonized_Data_0.1/Harmonized_Data/
        chmod 775 Harmonized_Data_run.sh
        ./Harmonized_run.sh
        """)

    diarioCurated = BashOperator(
        task_id='talend_diario_curated',
        bash_command="""
        cd $AIRFLOW_HOME/dags/etl_scripts/diario
        unzip -zxvf Curated_DS_Data_0.1.zip
        cd  $AIRFLOW_HOME/dags/etl_scripts/diario/Curated_DS_Data_0.1/Curated_DS_Data/
        chmod 775 Curated_DS_Data_run.sh
        ./Curated_DS_Data_run.sh
        """)
diarioRawData >> diarioHarmonized >> diarioCurated
