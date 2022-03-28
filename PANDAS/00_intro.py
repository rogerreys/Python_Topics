import pandas as pd
#DataFrames
print("\nDATAFRAMES")
#Display the first three rows:
df = pd.DataFrame({"a":[11,21,31],"b":[21,22,23]})
print("\n\tHEAD")
print(df.head(2))

#Obtain column  'a' :
print("\n\tColumn A")
print(df[["a"]])

#Obtain conditions in column 'a' :
print("\n\tCondicional")
print(df[df["a"]>11])

# Get to Know a Pandas Array
print("Unique")
df2 = pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
print(df2["a"].unique())



