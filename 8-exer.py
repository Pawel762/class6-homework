
import os
import pandas as pd
import matplotlib.pyplot as plt

wine_df = pd.read_csv(filepath_or_buffer='~/class5-homework/wine.data',
                sep=',',
                header=None)
wine_df.columns = ['Class','Alcohol','Malic_Acid','Ash','Alcalinity_of_Ash','Magnesium',
                'Total_Phenols','Flavanoids','Nonflavanoid_Phenols','Proanthocyanins',
                'Color_Intensity','Hue','OD280_OD315_of_Diluted_Wines','Proline']

wine_B = wine_df.drop(['Class'], axis = 1)

os.makedirs('plots/7-matplotlib_dataset_exploration', exist_ok=True)

for col1_idx, column1 in enumerate(wine_B.columns):
    for col2_idx, column2 in enumerate(wine_B.columns):
        if col1_idx < col2_idx:
            fig, axes = plt.subplots(1, 1, figsize=(5, 5))
            axes.scatter(wine_B[column1], wine_B[column2], label=f'{column1} to {column2}', color='green', marker='x')
            axes.set_title(f'{column1} to {column2}')
            axes.set_xlabel(column1)
            axes.set_ylabel(column2)
            axes.legend()
            plt.savefig(f'plots/7-matplotlib_dataset_exploration/wine_{column1}_{column2}_scatter.png', dpi=300)
            plt.close(fig)

plt.close()
