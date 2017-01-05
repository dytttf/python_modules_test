#coding:utf8
'''
xlrd模块测试
'''
import xlrd
import xlwt

#xlrd只读
book = xlrd.open_workbook('./test_files/test.xlsx', on_demand=True)

#工作表数目sheet
print book.nsheets

#工作表名字列表
print book.sheet_names()

#获取工作表sheet对象 两种方法
sheet_1 = book.sheet_by_index(0)
sheet_name_1 = book.sheet_by_name(book.sheet_names()[0])

#读操作
#行
print sheet_1.row_values(0)
#列
print sheet_1.col_values(0)
#单元格
print sheet_1.cell(0,0).value
print sheet_1.row(0)[0].value
print sheet_1.cell_value(0,0)



if 0:
    #xlwt只写
    #cell_overwrite_ok 重复写同一个单元格
    excel_file = xlwt.Workbook()
    sheet = excel_file.add_sheet('sheet1', cell_overwrite_ok=True)
    sheet.write(0,0,'测试'.decode('utf8'))

    #style用法
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'Times New Roman'
    font.bold = True
    font.colour_index = 13
    style.font = font
    sheet.write(0, 1, "Times New Roman", style)

    #不能写xlsx，打开报错
    excel_file.save('./test_files/ttt.xls')


