import re
import xlrd


wb = xlrd.open_workbook("data/2april_may.xlsx")
sheet = wb.sheet_by_index(0)

ind_comp=[]
temp = []

for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        str1 = sheet.cell_value(i,j)
        str1 = str(str1).upper()
        if(str1.__contains__("FROM DATE")):
            ind_comp=[i,j]
            temp.append(ind_comp)

count=0


start_row = temp[0][0]+1
head_col = []
temp_list = []
for i in temp:
    for j in range(sheet.ncols):
        count = i[0]
        str1 = sheet.cell_value(count, j)
        str1 = str(str1).upper()
        if (str1 != ''):
            head_col.append([j, str1])

temp.append([sheet.nrows, 0])
        # if(count < temp.__len__()):
        #     count+=1

print(head_col)

data_dict={}
for k in head_col:
    data_dict[k[1]]=[]

for i in range(len(temp)-1):
    # print("11111111111111111111111")
    start=temp[i][0]
    # print(start)
    end=temp[i+1][0]
    # print(end)
    for j in range(sheet.ncols):
        rl=[]
        if(sheet.cell_value(start,j)!=""):
            name=str(sheet.cell_value(start,j)).upper()
            # print(name)
            for k in range(start+1,end):
                str2=str(sheet.cell_value(k,j)).upper()
                if str2!='':
                    rl.append(str(sheet.cell_value(k,j)).upper())
                else:
                    break
            data_dict[name]=rl




# for i in data_dict["AT"]:
#     print(i)


for i in head_col:
    # print(i)
    print(i[1])
    print(data_dict[i[1]].__len__())

print(head_col.__len__())