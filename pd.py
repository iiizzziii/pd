
# display df(all rows) with empty values
df[df.isna().any(axis=1)]

# merge columns with some aagregator (---char---)
df["new_col"] = df[["col_a","col_b"]].astype(str).agg("---char---".join,axis=1)
