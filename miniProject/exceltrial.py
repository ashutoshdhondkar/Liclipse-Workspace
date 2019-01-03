import xlrd
workbook=xlrd.open_workbook("C:\\Users\\Admin\\My Documents\\LiClipse Workspace\\miniProject\\Book1.xlsx")
sheet=workbook.sheet_by_index(0)

print(sheet.nrows)
print(sheet.ncols)

for i in range(sheet.nrows):
    print(sheet.cell_value(i,0))