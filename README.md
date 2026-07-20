# Retail Analytics Dashboard

This is a simple interactive dashboard built using **Streamlit** to explore and analyze the Superstore sales dataset. The idea behind this project was to turn raw data into something visual and easy to understand.

---

##  What this project does

The dashboard lets you explore sales data by filtering it based on region and product category. As you change filters, all the charts and metrics update instantly, making it easier to see patterns and trends.

---

##  Features

* Filter data by **Region** and **Category**
* Quick overview using key metrics:

  * Total Sales
  * Total Orders
  * Number of Products
  * Average Sale Value
* Visualizations:

  * Sales by Category
  * Monthly Sales Trend
  * Top 5 Selling Products
  * Regional Sales Distribution
* Basic **automated insights** generated from the data

---

## Tech Used

* Python
* Streamlit
* Pandas
* Plotly

---

##  Project Structure

```
superstore-analysis/

data/
  └── superstore.csv

src/
  ├── preprocessing.py
  └── analysis.py

dashboard/
  └── app.py

requirements.txt
README.md
```

---

##  How to run it

1. Clone the repo

```
git clone https://github.com/your-username/superstore-analysis.git
cd superstore-analysis
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the app

```
streamlit run dashboard/app.py
```

---

## 📊 What you can learn from it

* Which categories bring in the most sales
* How sales change over time
* Which products perform the best
* How different regions compare

---

## Why I built this

I wanted to practice working with real datasets and build something interactive instead of just static charts. This project helped me understand how to structure a small analytics pipeline — from data cleaning to visualization.

---

##  Things I could improve

* Add profit analysis
* Add more advanced insights
* Improve UI design
* Maybe include forecasting later

---

##  Notes

The dataset used here is the Superstore dataset, which is commonly used for learning and practice in data analytics.

---
