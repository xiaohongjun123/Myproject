import ddt
import unittest
@ddt.ddt
class TestDome(unittest.TestCase):
    @ddt.file_data(r"E:\Users\Administrator\PycharmProjects\untitled\YGGH\TestCase\TestData\LoginData.json")
    def test_case01(self,data):
        value1,value2,value3=tuple(data.strip().split("||"))
        print(value1)
        print(value2)
        print(value3)

if __name__=="__main__":
    unittest.main()
