import pandas as pd
df = pd.read_csv("sept20_publish.csv") 
df.dorpna(inplace=True)
print(df)