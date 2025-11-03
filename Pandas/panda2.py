# import pandas as pd

# places={
#     "placenames":["Ooty","Switzerland","Kerala","Kashmir"],
#     "favspot":["Hills","Lakes","Fields","snowfall"]
# }
# df=pd.DataFrame(places)
# print(df)
# #methods
# print(df.head(1))
# print(df.tail(1))
# print(df.info())
# #properties
# #shape()
# #colmns()
# #details()
# #data selection
# #loc[] property
# print(df.loc[0:1])  
# print(df.loc[0,'favspot'])
# print(df.loc[1,'placenames'])
# print(df.loc[2,['placenames','favspot']])

# df=pd.read_csv("./orders.csv")
# # print(df)

# print(df.iloc[0,1])
# print(df.iloc[2,3])
# print(df.get("region"))    #get is one of the dictionary method if we don't provide existed value
# #it won't throw an error instead of it gives a value none 
# print(df.query('ship_mode=="Second Class" and region=="South"'))

# print(df[(df["ship_mode"]=="Second Class") | (df["region"]=="South")])

# print(df[(df["profit"]).between(5,10)])

# print(df.isnull())
# print(df["profit"].isnull())

# print(df.dropna(axis=1))
# print(df.fillna("example"))
# #replace()
# # print(df.replace(to_replace=None, Value="somthing")["region"])
# print(df.drop_duplicates())

#astype() method --- to check the datatype for the column in gthe dataframe
import pandas as pd

df=pd.read_csv("./orders.csv")
print(df)
print(df.info())

# df["Duration"]=df["Duration"].astype(float)
# print(df)

# df["Votes"]=df["Votes"].astype(str)
# print(df.info())

df.rename(columns={"Duration":"Dur"},inplace="Plase")
print(df)
# df.rename(columns={"Release year":})



