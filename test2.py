# pip install openpyxl
from openpyxl import Workbook, load_workbook
wb = load_workbook('filtertest.xlsx')
print([a for a in wb['filter']])
print(wb['filter']['A2'].value)

