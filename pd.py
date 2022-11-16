
# display df(all rows) with empty values
df[df.isna().any(axis=1)]