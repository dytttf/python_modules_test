#coding:utf8
import tkFileDialog


# options
# defaultextension: 默认文件扩展名
# filetypes: [("python文件", "*.py")]  # 文件类型
# initialdir: "C:\\"    # 默认打开路径
# initialfile: "C:\\Python27\\Lib\\lib-tk\\tkCommonDialog.py" # 默认选中文件名
# parent: 父窗口
# title: 窗口标题
# multiple： 是否支持多选

# 文件夹可以使用的选项
# initialdir, parent, title
# mustexist: 必须选择已存在的文件夹


# 函数列表

# 询问文件夹对话框
# askdirectory(**options)
if 0:
    dir_name = tkFileDialog.askdirectory()
    print(u"目录: {}".format(dir_name))

# 询问一个文件并打开返回文件对象
# askopenfile(mode='r', **options)
if 0:
    file_content = tkFileDialog.askopenfile()
    print(len(file_content.read()))

# 询问文件名
# askopenfilename(**options)
if 0:
    file_name = tkFileDialog.askopenfilename()
    print(file_name)

# 询问文件名列表 多选
# askopenfilenames(**options)
if 0:
    file_list = tkFileDialog.askopenfilenames()
    print(file_list)

# 询问文件名列表 返回文件对象列表
# askopenfiles(mode='r', **options)
if 0:
    file_obj_list = tkFileDialog.askopenfiles()
    print(file_obj_list)

# 询问保存文件地址 返回文件对象
# asksaveasfile(mode='w', **options)
if 0:
    file_obj = tkFileDialog.asksaveasfile()
    print(file_obj)
    file_obj.close()

# 询问保存文件地址 返回文件名
# asksaveasfilename(**options)
if 0:
    file_name = tkFileDialog.asksaveasfilename()
    print(file_name)

