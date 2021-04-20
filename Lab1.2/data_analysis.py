#!/usr/local/bin/python

from matplotlib import pyplot
from openpyxl import load_workbook

wb=load_workbook('data_analysis_lab.xlsx')
sheet=wb['Data']

def getvalue(x): return x.value

colA=list(map(getvalue, sheet['A'][1:]))
colD=list(map(getvalue, sheet['D'][1:]))
colC=list(map(getvalue, sheet['C'][1:]))

pyplot.plot(colA, colC)
pyplot.plot(colA, colD)
pyplot.show()