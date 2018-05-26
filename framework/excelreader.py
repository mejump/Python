# _*_ coding: utf-8 _*_
import json
import xlrd

class Create_excel:
    def open_excel(self,path):
        workbook = xlrd.open_workbook(path)
        table = workbook.sheets()[0]
        return table
    #获取sheet

    def get_nrows(self,table):
        nrows = table.nrows
        return nrows
    #获取行号

    def testname(self,table,nrows):
        TestName = []
        for i in range(1,nrows):
            TestName.append(table.cell(i,0).value)
        return TestName
    #获取用例name

    def testdata(self,table,nrows):
        TestData = []
        for i in range(1,nrows):
            data = json.loads(table.cell(i,1).value)
            TestData.append(data)
        return TestData
    #获取data接口参数

    def testurl(self,table,nrows):
        TestUrl = []
        for i in range(1,nrows):
            TestUrl.append(table.cell(i,2).value)
        return TestUrl
    #获取接口测试url

    def testpattern(self,table,nrows):
        TestPattern = []
        for i in range(1,nrows):
            TestPattern.append(table.cell(i,3).value)
        return TestPattern
    #获取接口期望响应结果

    def testreport(self,table,nrows):
        TestReport = []
        for i in range(1,nrows):
            TestReport.append(table.cell(i,4).value)
        return TestReport
    #获取用例期望的运行结果
    
    def testcheckpoint(self,table,nrows):
        TestCheckpoint=[]
        for i in range(1,nrows):
            TestCheckpoint.append(table.cell(i,5).value)
        return TestCheckpoint
    
if __name__ == "__main__":
    Create_excel()