from robot.libraries.BuiltIn import BuiltIn


class Loging(object):
    User_Email_ID_Txt = "xpath=//img[@alt='Outcome Health Logo']"
    #User_Email_ID_Txt = "id=user_email"
    User_Password_Txt = "id=user_pass"
    User_Login_Btn = "xpath=//input[contains(@value,'Login']"

    def __init__(self):
        self._rwebdriver = BuiltIn().get_library_instance('Selenium2Library')
        rwebdriver = BuiltIn().get_library_instance('Selenium2Library')
    def loginapp(self,user_email,user_pass):
        self._rwebdriver.wait_until_element_is_visible(self.User_Email_ID_Txt)
        #return 'hel'
        #self._rwebdriver.input_text(self.User_Email_ID_Txt)
  