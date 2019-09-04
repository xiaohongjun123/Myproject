import pymysql
from openpyxl import Workbook

wb=Workbook()
sheet=wb.create_sheet("test",0)
db=pymysql.connect('192.168.2.240','root','hexinpass001','jiaotou')
cursor=db.cursor()
sql='SELECT * FROM t_app_user ORDER BY user_id ASC'
try:
    cursor.execute(sql)
    results=cursor.fetchall()
    listdata=[['userid','username','account','phone']]
    for row in results:
        list=[]
        list.append(row[0])
        list.append(row[1])
        list.append(row[2])
        list.append(row[5])
        listdata.append(list)
    print(listdata)
    newlist=[]
    for new in listdata:
        new[1]=new[1].strip(b'\x00'.decode())
        new[2]=new[2].strip(b'\x00'.decode())
    print(listdata)
        #print('userid:%s,username:%s,account:%s,phone:%s'%(userid,username,account,phone))
except:
    print("error:unable to fetch data")
db.close()
for val in listdata:   #向Excel中同时插入多条数据
    sheet.append(val)
wb.save(r'G:\Myproject\Mysql\test.xlsx')