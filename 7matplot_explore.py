
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs('plots/7matplot_explore', exist_ok=True)


                sep=',',
                header=None)
wine_df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols',
                   'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity',
                 'hue', 'od280 od315_of_diluted_wines', 'proline']

for col1_idx, column1 in enumerate(wine_df.columns):
    for col2_idx, column2 in enumerate(wine_df.columns):
        if col1_idx < col2_idx:
            fig, axes = plt.subplots(1, 1, figsize=(5, 5))
            axes.scatter(wine_df[column1], wine_df[column2], label=f'{column1} to {column2}', color='blue', marker='d')
            axes.set_title(f'{column1} to {column2}')
            axes.set_xlabel(column1)
            axes.set_ylabel(column2)
            axes.legend()
            plt.savefig(f'plots/7matplot_explore/wine_{column1}_{column2}_scatter.png', dpi=300)
            plt.close(fig)

plt.close()
