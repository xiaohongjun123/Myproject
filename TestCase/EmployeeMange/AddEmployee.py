from selenium.common.exceptions import NoSuchElementException
from LogCommon import logger
from LoginMode import Login
import unittest
import time
import pymysql
logger=logger.mylog("Caselog").getlog()
db=pymysql.connect("192.168.2.200","root","hexinpass001","welfare")
cursor=db.cursor()
class AddEmployeeCase(unittest.TestCase):
    driver=Login.EmployeeLogin().Login()

    def test_case(self):
        logger.info("用户导入用例")
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_xpath('''/html/body/div[2]/div[2]/ul/li/a''').click()
            self.driver.find_element_by_xpath('''//*[@id="tab"]/li[3]/a''').click()
            self.driver.find_element_by_xpath('''//*[@id="tab"]/li[3]/ul/li[2]/a''').click()
            self.driver.switch_to.frame("content")
            self.driver.find_element_by_xpath('''//*[@id="list"]/div[1]/button[2]''').click()
            self.driver.find_element_by_id("file").send_keys(r"G:\testfile\userImport.xlsx")
            time.sleep(3)
            self.driver.find_element_by_xpath('''//*[@id="form"]/div/div[2]/button''').click()
            self.assertIn("肖测试",self.driver.page_source)
        except NoSuchElementException as e:
            logger.error("没有发现元素"+str(e))
        except AssertionError as e:
            logger.error("测试结果错误"+str(e))
            raise AssertionError
    def tearDown(self):
        sql="DELETE FROM t_app_user WHERE username='肖测试后'"
        cursor.execute(sql)
        db.commit()
        db.close()
        print("清除成功")
        self.driver.quit()






if __name__=="__main__":
    unittest.main()


