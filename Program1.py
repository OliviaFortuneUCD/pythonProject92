import pandas as pd


# Always display all the columns
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

df1 = pd.read_csv("kc_house_data.csv")
print(df1)

