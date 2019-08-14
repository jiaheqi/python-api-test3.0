#coding:utf-8
import datetime

from module import unittest_module


class SuiteReporter():
    def __init__(self):
        pass

    def make_report_file_name(self, test_module):
        """
        报告命名规范
        :param test_module:被测模块
        :return: 返回报告名称：路径+当前时间+，模块名称+后缀
        """
        __date = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        __report_file_name = "../report/"+ __date + test_module +".html"
        return __report_file_name

    def run_and_report(self):
        suite_list = []
        unittest_utils = unittest_module
