import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self,username,password,soft_id):
        self.username=username
        password=password.encode('utf8')
        self.password=md5(password).hexdigest()
        self.soft_id=soft_id
        self.base_params={
            'user':self.username,
            'pass2':self.password,
            'softid':self.soft_id
        }
        self.headers={
            'Connection':'Keep_Alive',
            'User_Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'
        }
    def PostPic(self,im,codetype):
        params={
            'codetype':codetype
        }
        params.update(self.base_params)
        files={'userfile':('ccc.jpg',im)}
        r=requests.post('http://upload.chaojiying.net/Upload/Processing.php',data=params,files=files,headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

if __name__=='__main__':
    Yzm=Chaojiying_Client('xhj123456','qazwsx123','899485')
    im=open(r'C:\Users\admin\Desktop\xiao\xiao\test.png','rb').read()
    print(Yzm.PostPic(im,1902)['pic_str'])