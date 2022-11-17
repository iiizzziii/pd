# display df rows with empty values
df[df.isna().any(axis=1)]

# sum of empty values in a column
df["col"].isna().sum()

# merge columns with some aggregator (---char---)
df["new_col"] = df[["col_a","col_b"]].astype(str).agg("---char---".join,axis=1)

# max length of value in column
df["col"].str.len().max()

# display new columns in df_a or [] (ideal for comparing updated dfs)
df_a.columns.difference(df_b.columns)

# open multiple files in pathlib folder into 1 file
pd.concat((pd.read_csv(f) for f in files_path), ignore_index=True)
