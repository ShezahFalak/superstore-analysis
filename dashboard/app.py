import os
import sys
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)


st.set_page_config(
    page_title="Retail Analytics",
    page_icon="📊",
    layout="wide"
)


from src.preprocessing import load_data, clean_data
from src.analysis import kpis, sales_by_category, monthly_sales,generate_insights



# --------------------
# LOAD DATA
# --------------------

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "superstore.csv"
)


df = load_data(DATA_PATH)
df = clean_data(df)



# --------------------
# SIDEBAR
# --------------------

st.sidebar.title("⚙ Dashboard Filters")


region = st.sidebar.selectbox(
    "Select Region",
    ["All Regions"] + list(df["Region"].unique())
)


category = st.sidebar.selectbox(
    "Select Category",
    ["All Categories"] + list(df["Category"].unique())
)



filtered_df = df.copy()


if region != "All Regions":
    filtered_df = filtered_df[
        filtered_df.Region == region
    ]


if category != "All Categories":
    filtered_df = filtered_df[
        filtered_df.Category == category
    ]



# --------------------
# TITLE
# --------------------

st.title("Retail Analytics Dashboard")

st.caption(
    "Interactive sales analysis using Superstore Dataset"
)



# --------------------
# KPI CARDS
# --------------------

sales, orders = kpis(filtered_df)



products = (
    filtered_df["Product Name"]
    .nunique()
)



c1,c2,c3,c4 = st.columns(4)


c1.metric(
    "💰 Total Sales",
    f"${sales:,.0f}"
)


c2.metric(
    "🛒 Total Orders",
    orders
)


c3.metric(
    "📦 Products",
    products
)


c4.metric(
    "📈 Avg Sale",
    f"${filtered_df.Sales.mean():,.2f}"
)




# --------------------
# SALES CATEGORY CHART
# --------------------


st.subheader("📊 Category Sales Overview")


cat_sales = (
    filtered_df
    .groupby("Category")
    ["Sales"]
    .sum()
    .reset_index()
)


fig = px.bar(
    cat_sales,
    x="Category",
    y="Sales",
    text="Sales",
    title="Sales by Category"
)


fig.update_layout(
    height=350
)


st.plotly_chart(
    fig,
    use_container_width=True
)



# --------------------
# MONTHLY SALES
# --------------------


st.subheader("📈 Monthly Sales Trend")


monthly = (
    filtered_df
    .groupby("Month")
    ["Sales"]
    .sum()
    .reset_index()
)


fig2 = px.line(
    monthly,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Revenue Growth"
)


fig2.update_layout(
    height=350
)


st.plotly_chart(
    fig2,
    use_container_width=True
)




# --------------------
# TOP PRODUCTS
# --------------------


st.subheader("🏆 Top Selling Products")


top_products = (
    filtered_df
    .groupby("Product Name")
    ["Sales"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(5)
    .reset_index()
)


fig3 = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 5 Products"
)


fig3.update_layout(
    height=350
)


st.plotly_chart(
    fig3,
    use_container_width=True
)




# --------------------
# AI INSIGHTS
# --------------------
st.subheader(" Business Insights")

insights = generate_insights(filtered_df)

for insight in insights:
    st.write(insight)





# --------------------
# REGION ANALYSIS
# --------------------


if category == "All Categories":


    st.subheader(
        "🌎 Regional Performance"
    )


    region_sales = (
        filtered_df.groupby("Region")
        ["Sales"]
        .sum()
        .reset_index()
    )


    fig4 = px.pie(
        region_sales,
        names="Region",
        values="Sales",
        title="Sales Distribution by Region"
    )


    st.plotly_chart(
        fig4,
        use_container_width=True
    )