##pandas 

# it is a third party library:


# what is pandas explain pandas pls give examples similar to general terms


# csv-comma seperated values

import pandas as pd

#read_csv


# df=pd.read_csv("C:/Users/makam/Downloads/sample_students_data.csv") 
# print(df)


df = pd.read_csv("C:/Users/makam/Downloads/sample_students_data.csv") 

# print(df.head(-1))


# print(df.tail(-1))


df1 = pd.DataFrame(
       {
        "B": ["B0", "B1", "B2", "B3"],
         "C": ["C0", "C1", "C2", "C3"],
         "D": ["D0", "D1", "D2", "D3"],
        "A": ["A0", "A1", "A2", "A3"],
     },
     index=[ 1, 2, 3,0],
 )


df2 = pd.DataFrame(    {
       "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
        },
       index=[4, 5, 6, 7],
    )
 
 
 
df3=pd.DataFrame(
    {
        "A":["shiva","harsha","ramesh","sudheer"],
        "B":["paul","henry","kiran","shakespear"],
        "C":["kalyan","akhila","kishore","praveen"],     
        "D":["teja","deepak","ramu","raju"]
    },
    index=[8,9,10,11]
)
print(df3)
itr=[df1,df2,df3]
res=pd.concat(itr)
print(res)


# read_csv - (delimiter= , nrows=int)
# head () +ve   -ve
# tail()  ve    -ve
# Dataframe ({})   index
# concat(iterable)   -->we need to pass iterable