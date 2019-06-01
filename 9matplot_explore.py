
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D

os.makedirs('plots/7matplot_explore', exist_ok=True)

df = pd.read_csv(filepath_or_buffer='~/class6/wine.data',
                sep=',',
                header=None)
df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols',
                   'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity',
                 'hue', 'od280 od315_of_diluted_wines', 'proline']

# df.drop('class', axis=1, inplace=True)


os.makedirs('plots/9matplotlib', exist_ok=True)

# Histogram
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.hist(df['flavanoids'], bins=30, color='g', label='flavanoids')
axes.set_title('Flavanoids')
axes.set_xlabel('Buckets')
axes.set_ylabel('flavanoids')
axes.legend()
plt.savefig('plots/9matplotlib/wine9_matplot.png', dpi=300)

# Pie
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.pie(df['class'].value_counts(), labels=df['class'].value_counts().index.tolist())
axes.set_title('Class')
axes.legend()
plt.savefig('plots/9matplotlib/wine_pie.png', dpi=300)

# Bar
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.bar(np.arange(0, len(df['nonflavanoid_phenols'])), df['nonflavanoid_phenols'], color='y', label='nonflavanoid_phenols')
axes.set_title('Nonflavanoid_phenols')
axes.set_xlabel('Index')
axes.set_ylabel('nonflavanoid_phenols')
axes.legend()
plt.savefig('plots/9matplotlib/wine_nonflavanoid_phenols_bar.png', dpi=300)

# Correlation Heatmap
# fig, axes = plt.subplots(1, 1, figsize=(20, 20))
# df['class']=df['total_phenols'].map({'1': 0, '2': 1, '3':2})
# correlation = df.corr().round(2)
# im = axes.imshow(correlation)
# cbar = axes.figure.colorbar(im, ax=axes)
# cbar.ax.set_ylabel('Correlation', rotation=-90, va="bottom")
# numrows = len(correlation.iloc[0])
# numcolumns = len(correlation.columns)
# axes.set_xticks(np.arange(numrows))
# axes.set_yticks(np.arange(numcolumns))
# axes.set_xticklabels(correlation.columns)
# axes.set_yticklabels(correlation.columns)
# plt.setp(axes.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
# for i in range(numrows):
#     for j in range(numcolumns):
#         text = axes.text(j, i, correlation.iloc[i, j], ha='center', va='center', color='w')
# axes.set_title('Heatmap of Correlation of Dimensions')
# fig.tight_layout()
# plt.savefig('plots/9matplotlib/wine_correlation_heatmap.png')

# 3D
Class1 = df[df['class'] == '1']
Class2 = df[df['class'] == '2']
Class3 = df[df['class'] == '3']
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1, projection='3d')
line1 = axes.scatter(Class1['flavanoids'], Class1['total_phenols'], Class1['od280 od315_of_diluted_wines'])
line2 = axes.scatter(Class2['flavanoids'], Class2['total_phenols'], Class2['od280 od315_of_diluted_wines'])
line3 = axes.scatter(Class3['flavanoids'], Class3['total_phenols'], Class3['od280 od315_of_diluted_wines'])
axes.legend((line1, line2, line3), ('Class1', 'Class2', 'Class3'))
axes.set_xlabel('flavanoids')
axes.set_ylabel('total_phenols')
axes.set_zlabel('od280 od315_of_diluted_wines')
plt.savefig('plots/9matplotlib/9wine_scatter_3d.png')

plt.close()

