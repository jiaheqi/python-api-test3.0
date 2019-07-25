#coding：utf-8
import xlrd


class Read_Excel(object):

    def __init__(self, file_name):
        """
        Read_Excel类的初始化（实例化）方法
        :param file_name:
        data:返回的是一个xlrd的workbook对象
        """
        self.data = xlrd.open_workbook(file_name)

    def get_all_sheet_by_name(self):
        """
        获取表格对象的所有sheet名称
        “单下划线” 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；
        “双下划线” 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。
        :return:['sheet1','sheet2']返回所有sheet名称的一个list
        """
        __sheet_list = self.data.sheet_names()
        return __sheet_list

    def get_sheet_by_name(self, sheet_name):
        """
        根据sheet名称回去当前sheet
        :param sheet_name: sheet页名称
        :return:<xlrd.sheet.Sheet object at 0x0000000002C20630>,返回当前sheet对象
        """
        __sheet = self.data.sheet_by_name(sheet_name)
        return __sheet

    def get_row_values(self, sheet_obj, row_index):
        """
        根据行索引获取当前行的内容list
        :param sheet_obj: sheet对象
        :param row_index: 行索引，从0开始
        :return: 返回当前行内容的list
        """
        __row_values = sheet_obj.row_values(row_index)
        return __row_values

    def get_col_values(self, sheet_obj, col_index):
        """
        根据列索引获取当前行的内容list
        :param sheet_obj: sheet对象
        :param col_index: 列索引，从0开始
        :return: 当前列内容的list，包含抬头
        """
        __col_values = sheet_obj.col_values(col_index)
        return __col_values

    def get_number_of_rows(self, sheet_obj):
        """
        返回当前sheet的行数
        :param sheet_obj: sheet对象
        :return: 行数
        """
        __row_number = sheet_obj.nrows
        return __row_number

    def get_number_of_cols(self, sheet_obj):
        """
        返回当前sheet的列数
        :param sheet_obj: sheet对象
        :return: 列数
        """
        __col_number = sheet_obj.ncols
        return __col_number

    def get_cell_value(self, sheet_obj, row_index, col_index):
        """
        返回某一个单元格的内容
        :param sheet_obj: sheet对象
        :param row_index: 行索引
        :param col_index: 列索引
        :return: 单元格值
        """
        __cell_value = sheet_obj.cell_value(row_index, col_index)
        return __cell_value

    def get_sheet_all_content(self, sheet_obj):
        """
        返回sheet也的所有行的值于一个list中
        :param sheet_obj: sheet对象
        :return: 所有行的值的list，中的元素也是list，为每一行的内容
        """
        __content = []
        __row_number = self.get_number_of_rows(sheet_obj)
        for tmp in range(__row_number):
            __row_values = self.get_row_values(sheet_obj, tmp)
            print(__row_values)
            __content.append(__row_values)
        return __content


read_excel = Read_Excel("test_sms_data.xlsx")
sheet = read_excel.get_sheet_by_name('短信服务降级')
print(read_excel.get_sheet_all_content(sheet))


