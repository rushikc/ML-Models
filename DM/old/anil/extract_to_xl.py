import xlsxwriter
import xlrd


def extract(fname):
    wb = xlrd.open_workbook("fname")
    sheet = wb.sheet_by_index(0)

    ind_comp = []
    temp = []

    for i in range(sheet.nrows):
        for j in range(sheet.ncols):
            str1 = sheet.cell_value(i, j)
            str1 = str(str1).upper()
            if (str1._contains_("FROM DATE")):
                ind_comp = [i, j]
                temp.append(ind_comp)

    count = 0
    start_row = temp[0][0] + 1
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
    print(temp)

    # if(count < temp._len_()):
    #     count+=1

    print(head_col)

    data_dict = {}
    for k in head_col:
        data_dict[k[1]] = []

    for i in range(len(temp) - 1):
        print("11111111111111111111111")
        start = temp[i][0]
        print(start)
        end = temp[i + 1][0]
        print(end)
        for j in range(sheet.ncols):
            rl = []
            if (sheet.cell_value(start, j) != ""):
                name = str(sheet.cell_value(start, j)).upper()
                print(name)
                for k in range(start + 1, end):
                    str2 = str(sheet.cell_value(k, j)).upper()
                    if str2 != '':
                        rl.append(str(sheet.cell_value(k, j)).upper())
                    else:
                        break
                data_dict[name] = rl

    for i in data_dict.keys():
        print(i)
        print(data_dict[i])

    workbook = xlsxwriter.Workbook("data1.xlsx", {'strings_to_numbers': True})
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    # dict1={"a":[1,2,3],"b":[4,5,6],"c":[7,8,9]}
    for i in data_dict.keys():
        row = 0
        worksheet.write(row, col, i)
        for j in data_dict[i]:
            row += 1
            worksheet.write(row, col, j)
        col += 1
    workbook.close()