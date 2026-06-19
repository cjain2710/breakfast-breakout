def is_active_stock(df):
    return (df["High"].max() - df["Low"].min()) > 0.5
