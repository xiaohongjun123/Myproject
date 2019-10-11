import unittest

import pymysql
from selenium.common.exceptions import NoSuchElementException

from LogCommon import logger
from LoginMode import Login

db=pymysql.connect("192.168.2.200","root","hexinpass001","welfare")
cursor=db.cursor()
logger=logger.mylog("CaseLog").getlog()

class ActAccount(unittest.TestCase):
    driver=Login.EmployeeLogin().Login()
    def test_case(self):
        logger.info("用户激活用例")
        self.driver.implicitly_wait(10)#设置隐式等待
        try:
            self.driver.find_element_by_xpath('''/html/body/div[2]/div[2]/ul/li/a''').click()
            self.driver.find_element_by_xpath('''//*[@id="tab"]/li[3]/a''').click()
            self.driver.find_element_by_xpath('''//*[@id="tab"]/li[3]/ul/li[3]/a''').click()
            self.driver.switch_to.frame("content")
            self.driver.find_element_by_xpath('''//*[@id="ListContent"]/tr[1]/td[8]/a[1]''').click()
            sql="SELECT is_open FROM t_app_user WHERE username='测试肖肖'"
            cursor.execute(sql)
            is_open=cursor.fetchall()
            db.close()
            print(is_open)
            self.assertEqual(is_open[0][0],2)
        except NoSuchElementException as e:
            logger.error("没有发现元素："+str(e))
        except AssertionError as e:
            logger.error("测试结果错误："+str(e) )
            raise AssertionError
    def tearDown(self):
        self.driver.quit()
        logger.info("测试完成")
if __name__=="__main__":
    unittest.main()

