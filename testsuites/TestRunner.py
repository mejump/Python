# coding = utf-8
import unittest
import HTMLTestRunner
import os
import time




if __name__=='__main__':
    #执行用例
    suite = unittest.TestLoader().discover("testsuites")
    runner=unittest.TextTestRunner()
    #runner.run(suite)
    #filePath = "//Users//Mr_Chen//Desktop//PythonWork//pyResult.html"
    file_path = os.path.dirname(os.path.abspath('.')) + '\\html\\pyResult_'
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    file_path = file_path + rq +'.html'

    fp = open(file_path,'wb')

    #生成报告的Title,描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Python Test Report',description='This  is Python  Report')
    runner.run(suite)
    