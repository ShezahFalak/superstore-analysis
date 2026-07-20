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
    category_profit = df.groupby('Category')['Profit'].sum()

    best_category = category_sales.idxmax()
    worst_profit_category = category_profit.idxmin()

    insights.append(
        f" {best_category} drives the highest revenue, making it a key growth category."
    )

    insights.append(
        f"! {worst_profit_category} shows the lowest profitability, indicating potential issues with pricing or high discounts."
    )


    # ----------------------------
    # 2. Regional Performance
    # ----------------------------
    region_sales = df.groupby('Region')['Sales'].sum()

    best_region = region_sales.idxmax()
    worst_region = region_sales.idxmin()

    insights.append(
        f"🌎 {best_region} leads in overall sales, contributing significantly to total revenue."
    )

    insights.append(
        f" {worst_region} underperforms compared to other regions, suggesting a need for targeted marketing or pricing strategies."
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
    top_5_contribution = product_sales.head(5).sum() / product_sales.sum() * 100

    insights.append(
        f" {top_product} is the top-selling product."
    )

    insights.append(
        f" Top 5 products contribute ~{top_5_contribution:.1f}% of total sales, indicating reliance on a small set of products."
    )


    # ----------------------------
    # 4. Monthly Trend
    # ----------------------------
    df['Month'] = df['Order Date'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Sales'].sum()

    best_month = monthly_sales.idxmax()
    worst_month = monthly_sales.idxmin()

    insights.append(
        f" Sales peaked in {best_month}, suggesting seasonal demand patterns."
    )

    insights.append(
        f"Lowest sales were recorded in {worst_month}, indicating a potential off-season period."
    )

    # ----------------------------
    # 5. Discount vs Profit (IMPORTANT)
    # ----------------------------
    if 'Discount' in df.columns and 'Profit' in df.columns:

        discount_impact = df.groupby(pd.cut(df['Discount'], bins=3))['Profit'].mean()

        insights.append(
            f" Higher discount ranges tend to reduce average profit, suggesting over-discounting may be impacting margins."
        )

    # ----------------------------
    # 6. Customer Concentration
    # ----------------------------
    customer_sales = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False)

    top_customer_share = customer_sales.iloc[0] / customer_sales.sum() * 100

    insights.append(
        f" The top customer contributes ~{top_customer_share:.1f}% of total sales, indicating moderate customer concentration."
    )


    return insights
