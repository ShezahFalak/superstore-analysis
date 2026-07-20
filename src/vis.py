import matplotlib.pyplot as plt
omport seaborn as sns

def plot_category_sales(data):
    data.plot(kind='bar', figsize=(10, 6))
    plt.title('Sales by Category')
    plt.ylabel('Sales')
    plt.savefig('output/plots/category_sales.png')
    plt.close()

def plot_sales_trend(data):
    data.plot(kind='line',figsize=(10, 6))
    plt.title('Monthly Sales Trend')
    plt.savefig('outputs/plots/sales_trend.png')
    plt.close()

def plot_top_cities(data):
    sns.barplot(x=data.values,y=data.index)
    plt.title('Top 10 Cities by Sales')
    plt.savefig('outputs/plots/top_cities.png')
    plt.close()
