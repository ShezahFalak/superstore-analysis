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

    import pandas as pd

    insights = []

    # Ensure datetime
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    # ----------------------------
    # 1. Category Performance
    # ----------------------------
    category_sales = df.groupby('Category')['Sales'].sum()

    best_category = category_sales.idxmax()
    worst_category = category_sales.idxmin()

    insights.append(
        f"📈 {best_category} drives the highest revenue, indicating strong demand — expanding this category could further accelerate growth."
    )

    insights.append(
        f"📉 {worst_category} contributes the least to total sales, suggesting a need for targeted promotions or product strategy improvements."
    )


    # ----------------------------
    # 2. Regional Performance
    # ----------------------------
    region_sales = df.groupby('Region')['Sales'].sum()

    best_region = region_sales.idxmax()
    worst_region = region_sales.idxmin()

    insights.append(
        f"🌎 {best_region} region leads in overall sales — allocating more inventory and marketing resources here could maximize returns."
    )

    insights.append(
        f"⚠️ {worst_region} region underperforms relative to others, indicating an opportunity to improve through localized strategies."
    )


    # ----------------------------
    # 3. Product Concentration
    # ----------------------------
    product_sales = (
        df.groupby('Product Name')['Sales']
        .sum()
        .sort_values(ascending=False)
    )

    top_product = product_sales.index[0]
    top_5_share = product_sales.head(5).sum() / product_sales.sum() * 100

    insights.append(
        f"🏆 {top_product} is the top-performing product by revenue."
    )

    insights.append(
        f"📦 The top 5 products contribute ~{top_5_share:.1f}% of total sales, indicating reliance on a limited set of products."
    )


    # ----------------------------
    # 4. Monthly Trends
    # ----------------------------
    df['Month'] = df['Order Date'].dt.to_period('M')

    monthly_sales = df.groupby('Month')['Sales'].sum()

    best_month = monthly_sales.idxmax()
    worst_month = monthly_sales.idxmin()

    insights.append(
        f"📅 Sales peak in {best_month}, highlighting seasonal demand — inventory and marketing should align with this trend."
    )

    insights.append(
        f"📉 {worst_month} shows the lowest sales, representing a slower business period that may benefit from promotional campaigns."
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
        f"👤 The highest-value customer contributes ~{top_customer_share:.1f}% of total revenue, indicating a diversified customer base with low dependency risk."
    )


    # ----------------------------
    # 6. Average Order Value (AOV)
    # ----------------------------
    total_sales = df['Sales'].sum()
    total_orders = df['Order ID'].nunique()

    aov = total_sales / total_orders

    insights.append(
        f"💰 The average order value is ${aov:,.2f}, reflecting typical customer spending per transaction."
    )


    return insights
