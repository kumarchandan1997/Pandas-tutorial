import pandas as pd

def analytics(patients,doctors,visits):
    df = visits.merge(patients, on="patient_id") \
               .merge(doctors, on="doctor_id")
    

    df["month"] = df["visit_date"].dt.month
    df["year"]  = df["visit_date"].dt.year

    monthly_revenue = df.groupby(["year", "month"])["treatment_cost"].sum()

    doctor_performance=df.groupby("name_y")["treatment_cost"].agg(
        total_revenue="sum",
        avg_cost ="mean",
        patient_count="count"
    )

    return monthly_revenue,doctor_performance
    
