import pandas as pd
from db_connection import get_connection


def load_data():
    conn = get_connection()

    patients = pd.read_sql("SELECT * FROM patients",conn)
    doctors  = pd.read_sql("SELECT * FROM doctors",conn)
    visits   = pd.read_sql("SELECT * FROM visits",conn)

    conn.close()

    return patients,doctors,visits