# 🌱 Smart Crop Analytics System

A web-based data analysis application built with **Django** that allows users to explore Canadian agricultural data.
The system provides insights into crop production and yield trends through **interactive charts and dynamic filtering**.

---

# Features includes:

## Interactive Charts (Chart.js)

* Production by Crop
* Yield Over Time
* Production by Region

## Dynamic Filtering

* Filter by year
* Filter by region
* Search crops or regions
* Sort results

## Database Storage

* Uses **SQLite** (no external setup required)
* Data is **preloaded into the database**
* No CSV upload required (per project requirements)

## Data Analysis

* Aggregations using Django ORM (`Sum`, `Avg`)
* Charts update dynamically based on filters

---

# ❓ Key Questions & How Charts Answer Them

This application is designed to answer specific analytical questions.

---

## 📊 Chart 1: Production by Crop

**Questions:**

* Which crops have the highest production in Canada?
* How does production compare across crops?

**Explanation:**

* Displays total production per crop
* Higher bars = higher production
* Helps identify dominant crops

---

## 📈 Chart 2: Yield Over Time

**Questions:**

* How has crop yield changed over time?
* Are there improvements in agricultural productivity?

**Explanation:**

* Shows average yield per year
* X-axis = Year
* Y-axis = Yield
* Reveals trends over time

---

## 📊 Chart 3: Production by Region

**Questions:**

* Which regions produce the most crops?
* How does production vary by province?

**Explanation:**

* Compares production across regions
* Helps identify high-producing areas

---

## Supporting Features (Filters & Table)

**Questions:**

* What happens when filtering by year or region?
* How can users explore specific crops?

**Explanation:**

* Filters refine the dataset
* Charts update automatically
* Table shows detailed records

---

# Technologies Used

* Python 3.13.7
* Django 5.x
* SQLite
* HTML / CSS
* JavaScript
* Chart.js

---

# 📁 Project Structure

```
smart-crop-analytics/
│
├── crop_project/
│   ├── crop_project/      # Project settings
│   ├── crops/             # App (models, views, templates)
│   ├── db.sqlite3         # Database (preloaded)
│   ├── manage.py
│   ├── import_data.py     # Data import script (not required to run)
│
├── README.md
```

---

# ⚙️ Development Environment Setup

Ensure your system meets the following requirements:

* Python: **3.13.7**
* Django: **5.x**
* Database: SQLite (included with Django)
* Browser: Chrome / Edge / Firefox

---

# Installation & Setup Guide

## 1. Install Python

Check version:

```bash
python --version
```

Expected:

```
Python 3.13.7
```

Download if needed:
https://www.python.org/downloads/

---

## 2. Clone the Repository

```bash
git clone <your-repo-url>
cd smart-crop-analytics/crop_project
```

---

## 3. Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install django
```

---

## 5. Apply Migrations

```bash
python manage.py migrate
```

---

## 6. Database Setup

This project includes a **preloaded SQLite database (`db.sqlite3`)**.

✔ No manual data import required
✔ Application is ready after migrations

---

## 7. Run the Server

```bash
python manage.py runserver
```

---

## 🌐 8. Open in Browser

Go to:

```
http://127.0.0.1:8000/
```

---

# How to Use the App

## Filters

* Select year
* Select region
* Enter search text
* Click **Filter**

 Charts update automatically

---

## 📊 Charts Overview

| Chart                | Description                |
| -------------------- | -------------------------- |
| Production by Crop   | Total production per crop  |
| Yield Over Time      | Average yield per year     |
| Production by Region | Total production by region |

---

## 📋 Table

* Displays filtered crop data
* Limited to improve performance
* Updates dynamically

---

# How Data Works

* Data stored in **SQLite (`db.sqlite3`)**
* Originally processed from CSV
* Managed using Django ORM:

  * `Sum()` → Production
  * `Avg()` → Yield

---

# Troubleshooting

## Charts not showing

Ensure Chart.js is included:

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

---

## Server not starting

Make sure you're in the correct folder:

```bash
cd crop_project
python manage.py runserver
```

---

## Data not appearing

If needed (optional):

```bash
python manage.py shell
exec(open('import_data.py').read())
```

---

# 📄 License

Educational use only
