# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.agileone_login import LoginPage


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_agileone_login(self):

        myloginpage = LoginPage(self.driver)
        time.sleep(2) 
        myloginpage.type_username('admin')
        #myloginpage.input_usename() 
        myloginpage.type_password('admin')       
        myloginpage.send_submit_btn()
       
        #time.sleep(5)
        
        time.sleep(5)
        myloginpage.get_windows_img()  # 调用基类截图方法
        myloginpage.get_page_title()
        try:
            assert 'AgileOne - Power to Agile Development' in myloginpage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))
        myloginpage.close()
        
  
if __name__ == '__main__':
    unittest.main()