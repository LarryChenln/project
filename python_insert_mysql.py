#!/usr/bin/env python
# coding=utf-8
import pymysql
import requests
import json,re
import datetime
url = 'http://xx.95.211.xxx:8081/slb/monitor?key=a400ba49ebda6b3236439bb30c84977'
mysql_config = {
    "host":"192.168.10.11",
    "user":"test",
    "password":"123456",
    "database":"test",
    "charset":"utf8"
}
def connectdb(**mysql_config):
    #db = pymysql.connect(host="192.168.10.11",user="test",password="123456",database="test",charset='utf8')  
    db = pymysql.connect(**mysql_config)
    cursor = db.cursor()
    text = requests.get(url)
    if text.status_code == 200:
        ip = url.split('/')[2].split(':')[0]
        port = url.split('/')[2].split(':')[1]
        data = json.loads(text.text)
        data = data.get('data').get('databody').get('result')
        try:
            for i in data.split('\n'):
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                kv = re.sub('/','_',i)
                kv = re.sub('^_','',kv)
                key = kv.split('=')[0]
                value = kv.split('=')[1]
                #sql = "insert into collect(ip,port,key,value,timestamp)VALUES (%d,%d,%s,%s,%s)" % (int(ip),int(port),key,value,now)
                sql = "insert into collect(my_ip,my_port,my_key,my_values,creatime) VALUES ('%s','%s','%s','%s','%s')" % (ip,port,key,value,now_time)
                #print(sql)
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    #print('insert failed')
                    db.rollback()
            db.close()
        except:
            #print('was failed')
            db.close()
            pass		
	
	
if __name__ == '__main__':
    connectdb(**mysql_config)	
