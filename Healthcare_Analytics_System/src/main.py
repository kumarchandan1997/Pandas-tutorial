from extract import load_data
from transform import clean_data
from analytics import analytics
import os

patients,doctors,visits = load_data()
patients,doctors,visits = clean_data(patients,doctors,visits)

monthly_revenue,doctor_perf = analytics(patients,doctors,visits)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_DIR = os.path.join(BASE_DIR, "data", "reports")

os.makedirs(REPORT_DIR, exist_ok=True)

monthly_revenue.to_csv(
    os.path.join(REPORT_DIR, "monthly_revenue.csv"),
    index=False
)

doctor_perf.to_csv(
    os.path.join(REPORT_DIR, "doctor_performance.csv"),
    index=False
)

print("Healthcare Analytics Reports Generated Successfully")