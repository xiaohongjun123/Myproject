import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
from email.mime.multipart import MIMEMultipart
import os


class EmailSD(object):
    def __init__(self,recivers):
        self.recivers=recivers

    def Send(self):
        mail_host='smtp.qq.com'
        mail_user='879337649@qq.com'
        mail_passwd='adxipngrbrngbcaj'
        mail_send='879337649@qq.com'

        message=MIMEMultipart()
        message['From']=Header('test_xiao','utf-8')#构造发信人昵称
        message['To']=Header('test_leader','utf-8')#构造收信人昵称
        ti=time.strftime('%H-%M-%S',time.localtime())
        subject=str(ti)+'测试日报'
        message['Subject']=Header(subject,'utf-8')#构造邮件主题
        message.attach(MIMEText('本轮自动化测试结果','plain','utf-8'))#构造正文类容
        if os.path.exists(r'E:\apk\app_1.0_1_201907241956.apk')==True:
            att1=MIMEText(open(r'E:\apk\app_1.0_1_201907241956.apk','rb').read(),'base64','utf-8')#构造附件
            att1['Content-Type']='application/octet-stream'#定义内容类型
            att1['Content-Disposition']="attachment;filename='test.apk'"#定义附件名称
            message.attach(att1)
        else:
            time.sleep(3)
            att1 = MIMEText(open(r'E:\apk\app_1.0_1_201907241956.apk', 'rb').read())  # 构造附件
            att1['Content-Type'] = 'application/octet-stream'  # 定义内容类型
            att1['Content-Disposition'] = "attachment;filename='test.apk'"  # 定义附件名称
            message.attach(att1)

        try:
            smtpobj=smtplib.SMTP_SSL(mail_host,465)
            smtpobj.set_debuglevel(1)
            smtpobj.login(mail_user,mail_passwd)
            smtpobj.sendmail(mail_send,self.recivers,message.as_string())
            print('send sucessful')
        except smtplib.SMTPException as e:
            print(e)
if __name__=="__main__":
    EmailSD('979669145@qq.com').Send()




