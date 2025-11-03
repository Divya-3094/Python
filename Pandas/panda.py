#Pandas
#Panel + Data Analysis
#data analysis.data manipulation,machine learning, data science,statistics
import pandas as pd

details={
    "names":["divya","chitti","cryso","sanju"],
    "marks":[30,40,50,60]
}
#1d--single dimension -- row or column   ---- Series
#2d--two dimension--  both rows and columns   ----dataframe


#creating a dataframe 
df=pd.DataFrame(details)
print(df)
print(type(df))                 #for checking whether it is dataframe or not
#creating series
df_2=pd.Series([1,2,3,4])
print(df_2)
print(type(df_2))

#for storing data we use json, excel, csv(comma separated value)--- data storage formats
# df=pd.read_csv("csv file path",headers=none)
# print(df)
# print(type(df))

#by default it converts the first row into headings

#df.head() method  -- it returns top most rows in the dataframe
#default is 5 -- shows first n rows
# df=read_csv("./orders.csv")
# print(df.head())    # it returns top 5 rows default
#print(df.head(10))   #it returns top 10 rows


#df.tail() method ---it returns bottom rows-- shows last n rows
# print(df.tail())
# print(df.tail(10))

#df.info() method --Summery of Dataframe
# print(df.info())

#df.describe() method -- statistical summery of numerical columns  
# print(df.describe())     it returns the statistical data

#df.shape() method --
# print(df.shape)      #returns the row and columnn count

#df.columns() method
#df.dtypes() methof=d

