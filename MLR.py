import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

sns.set()

df = pd.read_csv(filepath_or_buffer='~/class6/wine.data',
                 sep=',',
                 header=0)

df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids',
              'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280 od315_of_diluted_wines',
              'proline']

os.makedirs('plots/MLR', exist_ok=True)


g = sns.lmplot(x='total_phenols', y='flavanoids', hue='class',
               truncate=True, height=5, data=df)

# Use more informative axis labels than are provided by default
g.set_axis_labels('total_phenols', 'flavanoids')

plt.savefig(f'plots/MLR/multlinreg.png', dpi=300)

plt.close()