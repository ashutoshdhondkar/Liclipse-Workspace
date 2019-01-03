import pandas as pd
df = pd.read_csv("trial.csv",header = None)
'''
    skiprows = rows which you dont want to read
    names = [] is optional i.e. if you want names for each column
    nrows= read only that much rows
    na_values = ['value in excel'] repleces that specified value to NAN
    na_values = {column_name : [specified value]}
    
    
    Writing to csv
    
    df.to_csv("file.csv",index = False)
    
    index = False manje it does not writes index in first column
    columns = [] means the columns whch you want to write to new csv 
    by default it writes all the columns
'''
try:
    name = input("Enter column : ")

#     print(df.sort_values(name))
    print(df)
#     print(df.columns)
    df.to_csv("new.csv",index=False,columns = ['Name','Sex'])
except Exception as e:
    print(e)