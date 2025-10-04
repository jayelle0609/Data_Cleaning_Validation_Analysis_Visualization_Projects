# Data Analysis Projects

Each project will have 4-5 sections.

## 1. Data Preprocessing / Data Cleaning
  - Mean/mode/median imputation for missing values
  - Drop unnecessary columns : df.drop[listofcols], listofcols = ['col1','col2']
  - Drop rows with all nulls : df.dropna(how='all', axis =0)
  - Drop duplicates :df.dropduplicates()
  - Correct the data types : df['col'] = df['col'].astype(float/int/str)
  - Convert date cols to datetime 
  - Clean text, remove whitespace, lowercase :
  - Normalize data
  - Scale numeric data (normalization)
  - Outlier detection, remove extreme outliers
  - Convert categorical data into dummy variables (for ML purposes, with one hot encoding or label encoding)
  - pd.merge or pd.join if joining multiple data files
    
## 2. Data Validation
  - Check for valid ranges and values (no negative ages)
  - Check unique IDs, no duplicates
  - Use data constraints for... type checks, value checks (ex. gender should only have M/F, no other values)
  - Check consistency (ex. start date > end date)
  - Check against database if customer exists
  - Check  if email is in correct format, IC is in correct format (regex)

## 3. Exploratory Data Analysis
  - Descriptive statistics : df.info(), df.describe(), df.shape
  - Aggregation / group analysis : df.groupby('col')[agg : value_counts(), mean()
  - Correlation : df.corr()  --> numeric cols only, linear rs
  - Feature Engineering : Combine new features, PCA to reduce dimensionality

## 4. Data Visualization (matplotlib, seaborn, plotly, bokeh, altair or tableau)
  - Histograms, distribution of continuous data, checks for normality : sns.histplot(df['col1']) or df['col1'].hist()
        - Statistical tests to check for normality, skew, kurtosis :
        - KDE = true
  - Bar charts : categorical comparison
  - Box plots : outlier detection, distribution, helps to check for normality, skew, kurtotsis (if mean == median)
  - Violin plots
  - Scatterplots : rs betw 2 numerical variables
  - Heatmaps (corr matrix)
  - Line charts (trend over time)
  - Pie chart, donut chart

## 5. Predictions using Machine Learning (sci-kit learn, tensorflow, keras, pytorch, prophet, statsmodels, scipy)
  - Feature Engineering
       - Select relevant columns
       - Create new features
       - PCA to reduce features and dimensionality
  - Encode categorical variables
       - One-hot encoding : pd.get_dummies(df['col1'])
       - Label encoding
  - Scaling of variables (StandardScaler, MinMaxScaler, Normalization)
  - Train-test split
  - Cross validation 
  - Model selection 
  - Model evaluation
       - MAE, MSE, R2 --> regression metrics
       - Accuracy, Precision, Recall, F1 score, confusion matrix --> classification metrics
             - MAE, MSE, RMSE, MAPE, SMAPE --> time series analysis, regression type forecasts (numeric)
             - AIC, BIC, R2, **cross validation error** (rolling window --> impt, can compare to existing values~!)
             - (ARIMA, SARIMA, ETS, Holts Winters - triple exponential smoothing, etc)
             - Preprocessing TSA : resample, differencing, lag features, ADF test, cross validation (lags)
             - statsmodel OLS regression
    
