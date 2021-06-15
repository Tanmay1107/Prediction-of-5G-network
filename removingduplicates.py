import pandas as pd 
data = pd.read_csv("FinalTotalforcleaning12.csv") 
print(data)
data.drop_duplicates(subset ="Tweet", keep = "first", inplace = True) 
data.to_csv('RapidMinerTwitterData.csv',index=False,encoding='utf-8')
