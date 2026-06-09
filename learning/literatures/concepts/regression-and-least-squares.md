# Regression and Least Squares
**Aliases:** method of least squares; linear regression; logistic regression; ordinary least squares; OLS; residuals; Vandermonde matrix; Random Forest; supervised learning; unsupervised learning; k-means clustering; feature engineering; hyperparameter tuning; scikit-learn; pandas

**Definition:** The method of least squares minimises the sum of squared residuals Σ(yᵢ − f(xᵢ))² to fit a model f to data. For linear models f = Xβ, the normal equations give β = (X^T X)^{−1} X^T y; polynomial fitting uses a Vandermonde matrix. Logistic regression extends linear regression to binary classification via a sigmoid link function. Random Forest is an ensemble tree method using bagged decision trees with random feature subsets; it handles non-linear interactions and provides feature importance estimates. Unsupervised methods (k-means clustering, PCA) find structure in unlabelled data. In Python, scikit-learn provides implementations; pandas handles data wrangling.

**Key relations:**
- related: [error-analysis](error-analysis.md)
- related: [regularisation](regularisation.md)
- related: [statistical-methods](statistical-methods.md)

**Discussed in:**
- [Introduction to Experimental Error (Cartwright)](../notes/00-general-error-measurement/introduction-to-experimental-error-cartwright.md) — least-squares line fitting; residuals; goodness-of-fit
- [Data Science Workshop](../notes/programming/data-science-workshop.md) — feature engineering, supervised/unsupervised learning, Random Forest, k-means in Python
- [Data Visualization Workshop](../notes/programming/data-visualization-workshop.md) — Matplotlib, pandas, Bokeh; correlation analysis; exploratory data analysis
