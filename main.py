# Install necessary packages if not already installed
# !pip install numpy matplotlib pandas scikit-learn

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


# Function to perform imputation and save plots
def perform_imputation(strategy, output_filename):
    imp_data = dataFrame.iloc[:, :].values
    imputer = strategy
    imputer = imputer.fit(imp_data[:, 1:3])
    imp_data[:, 1:3] = imputer.transform(imp_data[:, 1:3])
    df_imp = pd.DataFrame(imp_data[:, 1:3])
    export_csv = df_imp.to_csv(output_filename, index=None, header=True)

    X = imp_data[:, 0]
    y1 = imp_data[:, 1]
    y2 = imp_data[:, 2]

    plt.plot(X, y1, label='y1', color='blue')
    plt.plot(X, y2, label='y2', color='red')

    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.title(output_filename.replace(".csv", ""))
    plt.savefig(output_filename.replace(".csv", ".png"))
    plt.close()


# Load the data
dataFrame = pd.read_csv("missingdata.csv")

# Assuming X is the independent variable, and y1 and y2 are dependent variables
X_original = dataFrame.iloc[:, 0].values
y1_original = dataFrame.iloc[:, 1].values
y2_original = dataFrame.iloc[:, 2].values

plt.plot(X_original,y1_original, label='y1', color='blue')
plt.plot(X_original,y2_original, label='y2', color='red')

plt.xlabel('X')
plt.ylabel('y')
plt.legend()

plt.title('Original Data')
plt.savefig("original.png")
plt.close()

plt.show()


# Perform mean imputation
perform_imputation(SimpleImputer(missing_values=np.nan, strategy='mean'), "impute_mean.csv")

# Perform median imputation
perform_imputation(SimpleImputer(missing_values=np.nan, strategy='median'), "impute_median.csv")

# Perform most frequent imputation
perform_imputation(SimpleImputer(missing_values=np.nan, strategy='most_frequent'), "impute_mode.csv")

# Perform KNN imputation
imp_KNN = KNNImputer(n_neighbors=2, weights="uniform")
perform_imputation(imp_KNN, "impute_KNN.csv")

# Perform MICE imputation
imp_MICE = IterativeImputer(max_iter=10, random_state=0)
perform_imputation(imp_MICE, "impute_MICE.csv")
