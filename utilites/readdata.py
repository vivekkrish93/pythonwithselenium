# import csv
#
# def getcsvdata(filename):
#     file_1=[]
#     reads=open(filename, "r") #file open
#     willreadfile=csv.reader(reads) #will return iertartable values
#     next(willreadfile) #will skip header
#     for a in willreadfile:
#         file_1.append(a)
#     return file_1

import xlrd
#comments two
#final updatedgit init

def getxldata(filename):
    data=[]
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)
    for i in range(1, sheet.nrows):
        data.append((sheet.cell_value(i, 0),sheet.cell_value(i, 1)))
    return data


