import pandas as pd
import numpy as np
from sympy import false, subsets

path = './imports-85.data'
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]


df = pd.read_csv(path, header=None)
df.columns = headers
    # Replace ? with NaN
df1 = df.replace('?', np.NaN)
    # Drop index (0) 
df = df1.dropna(subset=['price'], axis=0)

    # Show the first ten values
# print(df.head(10))

    # Show the last ten values
# print(df.tail(10))

    # Show columns name
# print(df.columns)
# df.to_csv("automobile.csv", index=false)

    # Data Type
# print(df.dtypes)
    # method will provide various summary statistics
# print(df.describe())
print(df.describe(include="all"))
    #  select the columns of a dataframe
# print(df[["length","compression-ratio"]])
print(df[["length","compression-ratio"]].describe())
    # Info
print("\n\nINFO")
print(df.info())