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

    # ----------------------------
    # 1. Category Performance
    # ----------------------------
    category_sales = df.groupby('Category')['Sales'].sum()

    best_category = category_sales.idxmax()
    worst_category = category_sales.idxmin()

    insights.append(
        f"📈 {best_category} generates the highest revenue, making it the strongest performing category."
    )

    insights.append(
        f"📉 {worst_category} contributes the least to overall sales, indicating potential for improvement or lower demand."
    )


    # ----------------------------
    # 2. Regional Performance
    # ----------------------------
    region_sales = df.groupby('Region')['Sales'].sum()

    best_region = region_sales.idxmax()
    worst_region = region_sales.idxmin()

    insights.append(
        f"🌎 {best_region} region leads in sales, contributing the largest share of revenue."
    )

    insights.append(
        f"⚠️ {worst_region} region underperforms compared to others and may need targeted strategies to boost sales."
    )


    # ----------------------------
    # 3. Product Dependency
    # ----------------------------
    product_sales = (
        df.groupby('Product Name')['Sales']
        .sum()
        .sort_values(ascending=False)
    )

    top_product = product_sales.index[0]
    top_5_share = product_sales.head(5).sum() / product_sales.sum() * 100

    insights.append(
        f"🏆 {top_product} is the top-selling product."
    )

    insights.append(
        f"📦 Top 5 products contribute ~{top_5_share:.1f}% of total sales, showing reliance on a small set of products."
    )


    # ----------------------------
    # 4. Monthly Trends
    # ----------------------------
    df['Month'] = df['Order Date'].dt.to_period('M')

    monthly_sales = df.groupby('Month')['Sales'].sum()

    best_month = monthly_sales.idxmax()
    worst_month = monthly_sales.idxmin()

    insights.append(
        f"📅 Sales peak in {best_month}, indicating seasonal demand."
    )

    insights.append(
        f"📉 {worst_month} records the lowest sales, suggesting a slow business period."
    )


    # ----------------------------
    # 5. Customer Concentration
    # ----------------------------
    customer_sales = (
        df.groupby('Customer Name')['Sales']
        .sum()
        .sort_values(ascending=False)
    )

    top_customer_share = customer_sales.iloc[0] / customer_sales.sum() * 100

    insights.append(
        f"👤 The top customer contributes ~{top_customer_share:.1f}% of total sales, indicating some level of dependency."
    )

    return insights
