##pandas 
#huge data handling 

import pandas as pd 
#read_csv  -> comma seperated values  
##data frame ->table like structure using the values in the file
df=pd.read_csv("C:/Users/makam/Downloads/sample_data.csv")
# print(df)
# dfhead=df.head(-25)
# print(dfhead)

# dftail=df.tail(-40)
# print(dftail)

# df=pd.DataFrame(
#     {
#         "name":["sai","ram"],
#         "age":[28,30]
#     }
# )

# df2=pd.DataFrame({
#      "name":["siva","praveen"],
#      "age":[22,22]
# })

# combined=pd.concat((df,df2))
# print(combined)


#info 
# print(df.info())
# print(df.info(memory_usage="deep"))
# df.info(show_counts=False) 
# print(df.info(show_counts=False) ) 

# print(df.describe(include="all"))
# print(df.describe(include="all"))



#is
# print(df.isna())

#fillna 
# print(df.fillna("empty"))
# print(df.fillna({"Name":"username","Age":0,"Performance_Rating":"no rating"}))


#dropna 
# print(df.dropna(axis=1)) 
# print(df.dropna(axis=1,how="all")) 


#groupby 

# print(df.groupby("Age").sum()) 
# print(df.groupby("Name").sum()) 
# print(df.groupby("Age",sort=False).count()) 



#sort_values 
# print(df.sort_values(by="Performance_Rating",ascending=False)) 

# print(df.drop([0,10,20,30,40]))
# print(df.drop(["Department"],axis=1))


# df=df.fillna({"Department":"empty"})

# print(df["Department"].value_counts(dropna=False))


# df=df.fillna("empty") 
# df.to_csv("updated_file")
# df.to_excel("updated")


# print(df.apply(lambda x: x.sum(),axis=1)) 

#merge 

# df1=pd.DataFrame({
#     "name":["udayasree","bindhu","kalyan"],
#     "marks":[20,30,35],
#     "batch":["37r","37r","37r"],
#     "yrs":[20,20,22]
# })
# df2=pd.DataFrame({
#     "name":["udayasree","bindhu","kalyan"],
#     "marks":[50,70,35],
#     "age":[20,20,22]
# })

# # merged=df1.merge(df2,on="name")
# merged=df1.merge(df2,left_on="yrs",right_on="age",how="inner")
# print(merged)


# print(df.loc[0:44])
# print(df.iloc[0:4])