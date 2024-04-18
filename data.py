import pandas as pd


df = pd.concat(
    map(
        pd.read_csv,
        [
            "data/daily_sales_data_0.csv",
            "data/daily_sales_data_1.csv",
            "data/daily_sales_data_2.csv",
        ],
    ),
    ignore_index=True,
)


pink_morsels_df = df.loc[df["product"].str.contains("pink")]


pink_morsels_df["sales"] = (
    pink_morsels_df["price"]
    .apply(lambda x: x.replace("$", "").replace(",", "") if isinstance(x, str)
           else x)
    .astype(float)) * (pink_morsels_df["quantity"])


cols = list(pink_morsels_df.columns.values)
df_pink_morsels_sales = pink_morsels_df[[cols[-1]] + [cols[-3]] + [cols[-2]]]


df_pink_morsels_sales = df_pink_morsels_sales.sort_values("region")
print(df_pink_morsels_sales)

df_pink_morsels_sales.to_csv("sales_pink_morsels.csv", index=False)
