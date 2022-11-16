# display df rows with empty values
df[df.isna().any(axis=1)]

# merge columns with some aggregator (---char---)
df["new_col"] = df[["col_a","col_b"]].astype(str).agg("---char---".join,axis=1)

# max length of value in column
df["col"].str.len().max()

# display new columns in df_a or [] (ideal for comparing updated dfs)
df_a.columns.difference(df_b.columns)
