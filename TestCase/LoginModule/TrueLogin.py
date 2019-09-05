from selenium import webdriver
from LogCommon import logger
from verify_code import VerfyCode
from selenium.common.exceptions import NoSuchElementException
import traceback
import ddt
import unittest
logger=logger.mylog('CaseLog').getlog()
VerCode=VerfyCode.Chaojiying_Client('xhj123456','qazwsx123','899485')
class TrueLogin(unittest.TestCase):

