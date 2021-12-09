
# Import those libraries
import pandas as pd
from scipy.stats import pearsonr
# Plotting
import matplotlib.pyplot as plt
import seaborn as sns

houses = {'area': [40, 50, 60, 70, 80],
          'price': [120000, 150000, 200000,
                    250000, 300000]}
df = pd.DataFrame(houses)



# Convert dataframe into series
list1 = df['area']
list2 = df['price']

# Apply the pearsonr()
corr, _ = pearsonr(list1, list2)
print('Pearsons correlation: %.3f' % corr)

df = pd.DataFrame(houses)
plt.xlabel('Area (metres sq.)')
plt.ylabel('Price (€)')
sns.scatterplot(data=df, x='area', y='price')
plt.show()
