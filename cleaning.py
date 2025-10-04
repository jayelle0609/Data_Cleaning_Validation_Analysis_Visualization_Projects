
def summary_df(df, name="Data Frame"):
  print(df.columns.tolist())
  print('------------')
  print(f"Head : {df.head()}")
  print("------------")
  print(f"Shape of {name} (row,cols) : {df.shape}")
  print("------------")
  print(f"Summary stats : {df.describe()}")
  print("------------")
  print(f"Missing values : {df.isnull().sum()}")
  print("------------")
  print(f"Duplicated values : {df.duplicated()}")