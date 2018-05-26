# coding=utf-8
from framework.base_page import BasePage


class LoginPage(BasePage):
    input_username = 'id=>username'
    input_password ='id=>password' 
    login_submit_btn = 'id=>login'
    lbl_message='xpath=>//*[@id=\"msg\"]'
    # 百度新闻入口
    #news_link login= "xpath=>//*[@id='u1']/a[@name='tj_trnews']"

    def type_username(self, text):
        self.type(self.input_username, text)
        #self.type_username(text)
        
    def type_password(self,text):
        self.type(self.input_password, text)
        
    def send_submit_btn(self):
        self.click(self.login_submit_btn)
    def get_message(self):
        s=self.get_element_text(self.lbl_message)
        #print (s)
        return s