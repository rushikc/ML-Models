import re
import xlrd

total_data_dict={}
head_col=[]
temp=[]
def final(fname):
    wb = xlrd.open_workbook(fname)
    sheet = wb.sheet_by_index(0)
    ind_comp = []
    #temp = []

    for i in range(sheet.nrows):
        for j in range(sheet.ncols):
            str1 = sheet.cell_value(i, j)
            str1 = str(str1).upper()
            if (str1.__contains__("FROM DATE")):
                ind_comp = [i, j]
                temp.append(ind_comp)

    count = 0
    #start_row = temp[0][0] + 1
    #head_col = []
    #temp_list = []
    for i in temp:
        for j in range(sheet.ncols):
            count = i[0]
            str1 = sheet.cell_value(count, j)
            str1 = str(str1).upper()
            if (str1 != ''):
                head_col.append([j, str1])
    #return sheet
def initfinal():
    #print(head_col)
    #print(temp)
    for i in head_col:
        total_data_dict[i[1]]=[]
    #print(total_data_dict)
def finalprocess(fname):
    wb = xlrd.open_workbook(fname)
    sheet = wb.sheet_by_index(0)
    data_dict = {}
    for k in head_col:
        data_dict[k[1]] = []

    for i in range(len(temp) - 1):
        start = temp[i][0]
        #print(start)
        end = temp[i + 1][0]
        #print(end)
        for j in range(sheet.ncols):
            rl = []
            if (sheet.cell_value(start, j) != ""):
                name = str(sheet.cell_value(start, j)).upper()
                #print(name)
                for k in range(start + 1, end):
                    str2 = str(sheet.cell_value(k, j)).upper()
                    if str2 != '':
                        rl.append(str(sheet.cell_value(k, j)).upper())
                    else:
                        break
                data_dict[name] = rl
                total_data_dict[name]+=data_dict[name]
    #print(data_dict["FROM DATE"])
def display():
    print(total_data_dict["FROM DATE"])

file_names=["1mar_april","2april_may","3may_june","4june_july","5july_aug","6aug_sept","7sept_oct","8oct_nov"]
for i in file_names:

    final("data/"+i+".xlsx")
    initfinal()
    finalprocess("data/"+i+".xlsx")
display()