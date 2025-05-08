import os
import pandas as pd
from datetime import datetime, timedelta

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data', 'sales')

def get_csv_path(date: datetime) -> str:
    """Return the extpected CSV path for a given date."""
    return os.path.join(DATA_DIR, f"{date.strftime('%Y-%m-%d')}.csv")

def load_sales_data(start_date: datetime, end_date: datetime) -> pd.DataFrame:
    """Load sales data for a date range (inclusive)."""
    dfs = []
    for i in range((end_date - start_date).days + 1):
        day = start_date + timedelta(days=i)
        path = get_csv_path(day)
        if os.path.exists(path):
            df = pd.read_csv(path)
            df['date'] = day
            dfs.append(df)
    if dfs:
        df_all = pd.concat(dfs, ignore_index=True)
        df_all['date'] = pd.to_datetime(df_all['date'])
        return df_all
    else:
        return pd.DataFrame() # Empty if no data

def analyse_sales():
    """Analyse yesterday's sales vs. 7-day average and return a summary report."""
    today = datetime.today().date()
    yesterday = today - timedelta(days=1)
    week_ago = yesterday - timedelta(days=6)

    # Load last 7 days of sales (including yesterday)
    sales_df = load_sales_data(week_ago, yesterday)
    if sales_df.empty:
        return "No sales data avaliable from the 7 days."
    
    # Group by product and date
    grouped = sales_df.groupby(['product_id', 'date'])['units_sold'].sum().reset_index()

    # Convert yesterday to pandas Timestamp for comparison
    yesterday_ts = pd.Timestamp(yesterday)

    # Calculate 7-day average (excluding yesterday)
    last_6_days = grouped[grouped['date'] < yesterday_ts]
    avg_7d = last_6_days.groupby('product_id')['units_sold'].mean().rename('avg_7d')

    # Get yesterday's sales
    yest_sales = grouped[grouped['date'] == yesterday_ts].set_index('product_id')['units_sold']

    # Join and calculate drop
    report_df = pd.DataFrame({'yesterday': yest_sales}).join(avg_7d)
    report_df = report_df.dropna()
    report_df['drop_pct'] = (report_df['avg_7d'] - report_df['yesterday']) / report_df['avg_7d']

    # Filter for >20% drop
    alert_df = report_df[report_df['drop_pct'] > 0.2]

    if alert_df.empty:
        return "No products had a >20% drop in units sold vs. their 7-day average."
    
    report_lines = [
        "Products with >20% drop in units sold vs. 7-day average:",
        "Product ID | 7-Day Avg | Yesterday | Drop %"
    ]
    for idx, row in alert_df.iterrows():
        report_lines.append(
            f"{idx} | {row['avg_7d']:.2f} | {row['yesterday']:.2f} | {row['drop_pct']*100:.1f}%"
        )

    return "\n".join(report_lines)

if __name__ == "__main__":
    result = analyse_sales()
    print(result)
    