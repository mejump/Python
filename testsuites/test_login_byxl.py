# -*- coding: utf_8 -*-

import requests
import re
import json
import unittest
from framework.excelreader import Create_excel
import os
import time
from framework.browser_engine import BrowserEngine
from pageobjects.agileone_login import LoginPage

class Testapi():
    def testapi(self,url,data):
        results = requests.post(url,data)
        return results

class Testcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ("接口测试开始")
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        
    @classmethod
    def tearDownClass(cls):
        print ("接口测试结束")
        cls.driver.quit()
        
    def test_post(self):
        global report
        api = Testapi()
        excel = Create_excel()
        file_path = os.path.dirname(os.path.abspath('.')) + '\\testcase\\'
        testpath = file_path+"testlogin.xlsx"
        testtable = excel.open_excel(testpath)
        testnrows = excel.get_nrows(testtable)
        
        
        myloginpage = LoginPage(self.driver)
        time.sleep(2) 
        
        for i in range(0,testnrows-1):
            testname = excel.testname(testtable,testnrows)[i]          

            testdata = excel.testdata(testtable,testnrows)[i]
            testcheckpoint=excel.testcheckpoint(testtable, testnrows)[i]
            
            
            json_str = json.dumps(testdata)
            testdatajson = json.loads(json_str)
            testusername=testdatajson['username']
            testpassword=testdatajson['password']  
                                
            #print(testdata)
            myloginpage.type_username(testusername)
            #myloginpage.input_usename() 
            myloginpage.type_password(testpassword)       
            myloginpage.send_submit_btn()
           
            testurl = excel.testurl(testtable,testnrows)[i]
            testContent= requests.get(testurl).content
            
            #print(testContent)
            #time.sleep(5)
            
            time.sleep(5)
            
            #myloginpage.get_page_title()
            
            #print(spagemessage)
            #print(testcheckpoint)
            
            try:
                spagemessage=myloginpage.get_message()
            except Exception as e:
                spagemessage='None'
            
            try:                
                assert spagemessage == testcheckpoint  # 调用页面对象继承基类中的获取页面标题方法
                print('Test Pass.')
            except Exception as e:
                print('Test Fail.', format(e))
                
            myloginpage.get_windows_img()  # 调用基类截图方法     
                        
            '''''
            testurl = excel.testurl(testtable,testnrows)[i]
            testpattern = excel.testpattern(testtable,testnrows)[i]
            testreport = excel.testreport(testtable,testnrows)[i]
            testresults = api.testapi(testurl,testdata)
            pattern = re.compile(testpattern)
            match = pattern.search(testresults.url)
            
            
            try:
                if testresults.status_code == 200:
                    if match.group() == testpattern:
                        report = "pass"
                else:
                    print ("测试请求失败")
            except AttributeError:
                report = "no"
            if report == testreport:
                print ("用例名称："),testname,"测试结果：测试通过"
            else:
                print ("用例名称："),testname,"测试结果：测试失败"
            
            '''''
            

        
if __name__ == "__main__":
    unittest.main()