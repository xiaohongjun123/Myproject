from selenium import webdriver
from verify_code import VerfyCode
import time
verifycode=VerfyCode.Chaojiying_Client('xhj123456','qazwsx123','899485')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PIL import Image
class EmployeeLogin(object):
    def Login(self):
        try:
            driver=webdriver.Chrome(r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
            driver.get("http://192.168.2.200:8081/login")
            filename = "ScreemshotVerfycode.png"
            driver.save_screenshot(filename)
            ele = driver.find_element_by_xpath('''//*[@id="form"]/ul[3]/li[3]/img''')
            left = ele.location["x"]
            top = ele.location["y"]
            print(ele.location)
            right = left + ele.size["width"]
            bottom = top + ele.size["height"]
            print(ele.size)
            im = Image.open(filename)
            im1 = im.crop((left, top, right, bottom))
            im1.save(filename)
            pic = open(filename, "rb").read()
            code=verifycode.PostPic(pic,1902)["pic_str"]
            print(code)
            driver.find_element_by_xpath('''//*[@id="M_username"]''').send_keys("te_admin")
            driver.find_element_by_xpath('''//*[@id="M_password"]''').send_keys("Aa123456")
            driver.find_element_by_xpath('''//*[@id="code"]''').send_keys(code)
            driver.find_element_by_xpath('''//*[@id="form"]/input''').click()
            location=(By.XPATH,'''/html/body/div[2]/div[1]/a/img''')
            WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located(location))
            driver.find_element_by_xpath("/html/body/div[2]/div[1]/a/img")
            return driver
        except:
            driver.quit()
            EmployeeLogin().Login()


if __name__=="__main__":
    EmployeeLogin().Login()