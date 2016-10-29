import pandas as pd
import csv

path = 'E:/NEU/Sem 3/Data Science/Assignment 2/Assignment 2(1)/'

df1 = pd.read_csv(path+"output.csv")    # reading first file in dataframe df1
df2 = pd.read_csv(path+"api_full_data.csv") # reading second ( api extracted data) in dataframe df2
merged = df1.merge(df2, on=["year","month","day","hour"], how="outer").fillna("0")  #merging file based on index, converting NA data to 0
merged.to_csv(path+"merged.csv", index=False)   # writing to file , removing index from created csv file