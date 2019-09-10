from selenium import webdriver
from LogCommon import logger
from verify_code import VerfyCode
from PIL import Image
from selenium.common.exceptions import NoSuchElementException
import traceback
import ddt
import unittest
import time
logger=logger.mylog('CaseLog').getlog()
VerCode=VerfyCode.Chaojiying_Client('xhj123456','qazwsx123','899485')
@ddt.ddt
class TrueLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        self.driver.get("http://192.168.2.200:8081/login")

    @ddt.file_data(r"G:\Myproject\TestCase\LoginModule\LoginData.json")
    def test_case(self,logindata):
        logger.info("正确账号进行登录用例")
        filename="ScreemshotVerfycode.png"
        self.driver.save_screenshot(filename)
        ele=self.driver.find_element_by_xpath('''//*[@id="form"]/ul[3]/li[3]/img''')
        left=ele.location["x"]
        top=ele.location["y"]
        print(ele.location)
        right=left+ele.size["width"]
        bottom=top+ele.size["height"]
        print(ele.size)
        im=Image.open(filename)
        im1=im.crop((left,top,right,bottom))
        im1.save(filename)
        pic=open(filename,"rb").read()
        code=VerCode.PostPic(pic,1902)["pic_str"]
        account,passwd=tuple(logindata.strip().split("||"))
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_xpath('''//*[@id="M_username"]''').send_keys(account)
            self.driver.find_element_by_xpath('''//*[@id="M_password"]''').send_keys(passwd)
            self.driver.find_element_by_xpath('''//*[@id="code"]''').send_keys(code)
            self.driver.find_element_by_xpath('''//*[@id="form"]/input''').click()
            time.sleep(1)
            self.assertIn("肖的测试企业",self.driver.page_source)
        except NoSuchElementException as e:
            logger.error("没有发现元素")
        except AssertionError as e:
            logger.error("结果错误"+str(e))
            raise AssertionError

    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()
