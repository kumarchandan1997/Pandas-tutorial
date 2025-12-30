# 🏥 Healthcare Analytics System  
**Python + Pandas + MySQL | Production-Ready Data Analytics Project**

---

## 📌 Project Overview

The **Healthcare Analytics System** is a real-life, production-ready data analytics project built using **Python, Pandas, and MySQL**.

This project simulates a hospital environment with **large datasets (50k+ records)** and demonstrates how a **Data Analyst / Senior Engineer** works with:
- Relational databases
- Pandas data processing
- Performance-oriented analytics
- Clean project architecture
- Automated reporting

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Pandas**
- **MySQL / MariaDB**
- **SQLAlchemy**
- **Faker (for dummy data generation)**
- **Matplotlib (optional for plots)**

---

## 🗄️ Database Schema

### Patients Table
```sql
CREATE TABLE patients (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    city VARCHAR(100)
);

CREATE TABLE doctors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    specialization VARCHAR(100)
);


CREATE TABLE visits (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    visit_date DATETIME,
    diagnosis VARCHAR(255),
    treatment_cost DECIMAL(10,2),
    FOREIGN KEY (patient_id) REFERENCES patients(id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(id)
);
```
---
### Patients Table

```
### Patients Table
```

