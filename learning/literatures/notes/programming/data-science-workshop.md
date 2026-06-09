# The Data Science Workshop

- **Source:** TheDataScienceWorkshopebook-200131-093120.pdf
- **Drive link:** https://drive.google.com/file/d/1xRqjWJrVUPxE_QKr3PrL2WqMhFXtnFwd/view?usp=drivesdk
- **Type:** book
- **Author/Year:** Anthony So, Thomas V. Joseph, Robert Thas John, Andrew Worsley, Dr. Samuel Asare / 2020
- **Coverage:** partial (large file, truncated extraction)

## Overview
A Packt workshop-style introduction to data science using Python, covering the full machine learning pipeline from data loading and exploratory analysis through regression, binary classification, multiclass classification with Random Forest, and unsupervised clustering. All concepts use hands-on exercises on real-world datasets with scikit-learn, statsmodels, and pandas.

## Unique contribution
Structures learning around a business-problem framing: each ML chapter starts by defining the business context before introducing the algorithm. It also gives substantial coverage to feature engineering (both business-driven and data-driven) and model evaluation metrics alongside the modeling itself.

## Key concepts
- Supervised learning (regression, classification)
- Unsupervised learning (clustering)
- Reinforcement learning (overview)
- pandas DataFrame, Series
- scikit-learn API (fit/predict, hyperparameters)
- Simple and multiple linear regression
- Least squares estimation
- Log-linear transformation
- Statsmodels formula API
- F-test, t-test
- Logistic regression
- Binary classification
- Confusion matrix, accuracy, classification report
- Feature engineering
- Random Forest classifier
- Hyperparameter tuning (n_estimators, max_depth, min_samples_leaf, max_features)
- k-means clustering
- Elbow method (choosing k)
- Cluster centroid, Euclidean distance
- Data standardization (z-score scaling)
- Exploratory data analysis (EDA)
- Correlation matrix

## Methods / results / takeaways
- Regression chapter covers least-squares from first principles before moving to statsmodels, helping readers understand what the library is computing.
- Log transformations are introduced as a practical fix for right-skewed response variables before applying OLS.
- The logistic regression chapter explicitly separates data preprocessing steps from model fitting, reinforcing the importance of encoding categorical variables.
- Random Forest tuning exercises show that increasing tree depth beyond a threshold increases overfitting without accuracy gains on validation data.
- k-means sensitivity to initialization is demonstrated empirically; `k-means++` initialization is recommended over random.
- Standardizing features before clustering is emphasized as essential when features have different scales.
