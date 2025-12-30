import pandas as pd



def clean_data(patients,doctors,visits):
    visits.drop_duplicates(inplace=True)
    visits["visit_date"] = pd.to_datetime(visits["visit_date"])
    visits["treatment_cost"] = visits["treatment_cost"].astype(float)

    return patients,doctors,visits
