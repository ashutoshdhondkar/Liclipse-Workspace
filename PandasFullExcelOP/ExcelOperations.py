import pandas as pd

def convert_cell(cell):
    if(cell == 'Female'):
        return 'F'
    elif(cell == 'Male'):
        return 'M'
    else:
        return cell
    
'''
    converters = {
        'column_name' : function to be applied
    }
'''

df = pd.read_excel('trial.xlsx')

print(df)
print(df.columns.values)
# print(df.sort_values('1',ascending = False))
print(df)
# writing to excel
# df.to_excel("new.xlsx",sheet_name = 'Sheet2',index = False)