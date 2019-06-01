import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

os.makedirs('plots/15-seaborn_pairplot', exist_ok=True)

wine_df = pd.read_csv(filepath_or_buffer='~/class6/wine.data',
                sep=',',
                header=None)
wine_df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols',
                   'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity',
                 'hue', 'od280 od315_of_diluted_wines', 'proline']
sns.pairplot(wine_df, hue='class', diag_kind='hist')
plt.savefig('plots/15-seaborn_pairplot/wine_pairplot.png')

plt.close()