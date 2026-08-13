# 📊 Shiksha Saathi Dashboard

## Overview

Shiksha Saathi Dashboard is a simple analytics dashboard developed using Python, SQLite, and Streamlit.

The dashboard tracks outbound call performance by displaying:

- Total Calls
- Successful Calls
- Failed Calls

This project is part of the AI Voice Agent Challenge and demonstrates basic call analytics visualization.

---

## Technologies Used

- Python
- SQLite
- Streamlit

---

## Project Structure

├── analytics.py
├── dashboard.py
├── call_analytics.db
└── README.md

---

## Features

### Call Analytics Storage
- Stores call outcomes in SQLite database.
- Supports successful and failed call tracking.

### Dashboard Metrics
- Total Calls
- Successful Calls
- Failed Calls

### Real-Time Visualization
- Dashboard updates automatically based on database records.

---

## Database Schema

Table: calls

| Column | Type |
|----------|----------|
| id | INTEGER |
| outcome | TEXT |

---

## Sample Data

```python
save_call("success")
save_call("success")
save_call("failed")
