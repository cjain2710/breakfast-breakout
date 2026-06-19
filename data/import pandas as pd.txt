import pandas as pd

def generate_report(results):
    df = pd.DataFrame(results)
    path = "reports/outputs/daily_report.csv"
    df.to_csv(path, index=False)
    return path