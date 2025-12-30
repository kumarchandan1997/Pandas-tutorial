import random

import mysql.connector
from faker import Faker
from datetime import datetime,timedelta

fake = Faker()

conn = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="chandan1997@A",
    database="db_hospital_management"
)

cursor = conn.cursor()

for _ in range(5000):
    cursor.execute("INSERT INTO patients (name,gender,age,city,created_at) VALUES (%s,%s,%s,%s,%s)",(
        fake.name(),
        random.choice(["Male","Female"]),
        random.randint(1,90),
        fake.city(),
        fake.date_time_this_year()
    ))

for _ in range(200):
    cursor.execute("INSERT INTO doctors (name,specialization,experience_years) VALUES(%s,%s,%s)",(
        fake.name(),
        random.choice(['Cardiology','Ortho','Neuro','ENT','General']),
        random.randint(1,30)
    ))

conn.commit()   


for _ in range(50000):
    cursor.execute("INSERT INTO visits (patient_id,doctor_id,visit_date,diagnosis,treatment_cost) VALUES(%s,%s,%s,%s,%s)",(
        random.randint(1,5000),
        random.randint(1,200),
        fake.date_time_this_year(),
        random.choice(["Fever","Injury","Infection","Checkup"]),
        round(random.uniform(500,50000),2)
    ))

conn.commit()
conn.close()    