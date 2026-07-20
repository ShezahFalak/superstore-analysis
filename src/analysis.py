def kpis(df):
    total_sales = df['Sales'].sum()
    total_orders = df['Order ID'].nunique()

    return total_sales, total_orders


def sales_by_category(df):
    return df.groupby('Category')['Sales'].sum()


def monthly_sales(df):
    return df.groupby('Month')['Sales'].sum()

import pandas as pd


def generate_insights(df):

    insights = []

    # 1. Best Category
    category_sales = df.groupby('Category')['Sales'].sum()
    best_category = category_sales.idxmax()
    category_value = category_sales.max()

    insights.append(
        f"📈 {best_category} is the highest revenue-generating category "
        f"with total sales of ${category_value:,.2f}."
    )


    # 2. Best Region
    region_sales = df.groupby('Region')['Sales'].sum()
    best_region = region_sales.idxmax()
    region_value = region_sales.max()

    insights.append(
        f"🌎 {best_region} region contributes the highest sales "
        f"with revenue of ${region_value:,.2f}."
    )


    # 3. Best Product
    product_sales = df.groupby('Product Name')['Sales'].sum()
    best_product = product_sales.idxmax()
    product_value = product_sales.max()

    insights.append(
        f"🏆 {best_product} is the top-performing product "
        f"generating ${product_value:,.2f} in sales."
    )


    # 4. Best Month
    df['Month'] = df['Order Date'].dt.month_name()

    monthly_sales = df.groupby('Month')['Sales'].sum()

    best_month = monthly_sales.idxmax()
    month_value = monthly_sales.max()

    insights.append(
        f"📅 {best_month} recorded the highest sales volume "
        f"with ${month_value:,.2f} revenue."
    )


    # 5. Customer Insight
    customer_sales = (
        df.groupby('Customer Name')['Sales']
        .sum()
        .sort_values(ascending=False)
    )

    top_customer = customer_sales.index[0]

    insights.append(
        f"👤 {top_customer} is the highest-value customer "
        f"with ${customer_sales.iloc[0]:,.2f} in purchases."
    )


    return insights