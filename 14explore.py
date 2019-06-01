

import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
os.makedirs('plots/7matplot_explore', exist_ok=True)

df = pd.read_csv(filepath_or_buffer='~/class6/wine.data',
                sep=',',
                header=None)
df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols',
                   'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity',
                 'hue', 'od280 od315_of_diluted_wines', 'proline']

os.makedirs('plots/14seaborn', exist_ok=True)

sns.set()

for jointplot_kind in ['reg', 'hex', 'kde', 'scatter']:
    sns.jointplot('flavanoids', 'total_phenols', data=df, kind=jointplot_kind)
    plt.savefig(f'plots/14seaborn/Flavonoids_Totphenols_{jointplot_kind}.png')

plt.close()

