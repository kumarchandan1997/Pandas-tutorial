# 🐼 Pandas Complete Notes (Theory + Examples + Interview Ready)

Pandas is a powerful **Python library** used for **data manipulation, cleaning, analysis, and transformation**.  
It is built on top of **NumPy** and is widely used in **Data Analytics, Data Science, and Backend Reporting**.

---

## 📌 Why Pandas?
- Handle large datasets easily
- Clean messy real-world data
- Fast operations using vectorization
- SQL-like operations in Python

---

## 🧱 Core Data Structures

### 1️⃣ Series (1D Data Structure)
A Series is like a **single column** of data with an index.

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)
```

### 2️⃣ DataFrame (2D Data Structure)
A DataFrame is like an Excel sheet or SQL table.

```python
data = {
    "Name": ["Amit", "Ravi", "Neha"],
    "Age": [25, 30, 28],
    "Salary": [40000, 50000, 45000]
}

df = pd.DataFrame(data)
print(df)
```
