import unittest
from selenium.common.exceptions import NoSuchElementException
import pymysql
from LoginMode import Login
from LogCommon import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
logger=logger.mylog("Caselog").getlog()

class SendIntegrals(unittest.TestCase):
    driver=Login.EmployeeLogin().Login()
    def test_case(self):
        logger.info("发放积分用例")
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_xpath('''/html/body/div[2]/div[2]/ul/li/a''').click()
            self.driver.find_element_by_xpath('''//*[@id="tab"]/li[4]/a/span/b''').click()
            self.driver.find_element_by_xpath('''//*[@id="tab"]/li[4]/ul/li[1]/a''').click()
            self.driver.switch_to.frame("content")
            self.driver.find_element_by_xpath('''//*[@id="tree"]/ul/li/div/div[2]/div[1]/button''').click()
            self.driver.find_element_by_xpath('''//*[@id="monery"]''').send_keys(100)
            self.driver.find_element_by_xpath('''//*[@id="homePage"]/div[2]/div/div/div[5]/button''').click()

            self.driver.find_element_by_xpath('''//*[@id="Recharge"]/div[2]/div/div[1]/div[1]/span[2]/div/div[2]/div/label/div[1]/span/input''').click()
            self.driver.find_element_by_xpath('''//*[@id="quanxian1"]/div/label/div[1]/span/input''').click()
            self.driver.find_element_by_xpath('''//*[@id="firstStepsBtn"]''').click()
            time.sleep(5)
            self.driver.find_element_by_xpath('''//*[@id="Recharge1"]/div[2]/div/div/div[1]/div/div/div/button[1]''').click()
            location=(By.XPATH,'''//*[@id="uploadFile"]''')
            WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located(location))
            self.driver.find_element_by_id("uploadFile").send_keys(r"C:\Users\admin\Desktop\pic\tim1g.jpg")
            self.driver.find_element_by_xpath('''//*[@id="form"]/div/div[2]/div/button[1]''').click()
        except NoSuchElementException as e:
            logger.error("没有发现元素"+str(e))
        except AssertionError as e:
            logger.error("测试结果错误"+str(e))
            raise  AssertionError
    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()






