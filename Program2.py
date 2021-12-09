import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mp

# Always display all the columns
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

df1 = pd.read_csv("kc_house_data.csv")

dataplot = sb.heatmap(df1.corr(), cmap="YlGnBu", annot=True)

# displaying heatmap
mp.show()# plotting correlation heatmap
