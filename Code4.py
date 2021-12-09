# Import those libraries
import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns

houses = {'area': [40, 50, 60, 70, 80],
          'price': [300000, 200000, 400000,
                    75000, 10000]}
df = pd.DataFrame(houses)



# Convert dataframe into series
list1 = df['area']
list2 = df['price']

# Apply the pearsonr()
corr, _ = pearsonr(list1, list2)
print('Pearsons correlation: %.3f' % corr)
plt.xlabel('Area (metres sq.)')
plt.ylabel('Price (€)')
sns.scatterplot(data=df, x='area', y='price')
plt.show()
