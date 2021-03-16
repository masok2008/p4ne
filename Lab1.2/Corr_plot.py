#2nd Lab file

from matplotlib import pyplot as pplt
from openpyxl import load_workbook as ld_wb

wb=ld_wb('data_analysis_lab.xlsx')
sht=wb['Data']

def getvalue(x): return x.value

list_x=list(map(getvalue, sht['A'][1:]))
list_temp=list(map(getvalue, sht['C'][1:]))
list_act=list(map(getvalue, sht['D'][1:]))

pplt.plot(list_x, list_temp, label='temp')
pplt.plot(list_x, list_act, label="Sun_Activity")
pplt.show()
