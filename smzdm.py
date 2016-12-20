#!/usr/bin/python\
#coding=utf-8 
# -*- coding: utf-8 -*-

# for Python3
# test in python 3.5.1 and python 2.6.6 (linux) 
# test in python 3.5.2 (windows)
# PLS modify the sender  / mailto_list / mail_host / mail_user / mail_pass 

from bs4 import BeautifulSoup

try:
        import urllib.request as request
except:
        import urllib2 as request

import smtplib 
from email.mime.text import MIMEText 

#from email.header import Header
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart

import pickle
import os

import sys

try:
        reload(sys)
        sys.setdefaultencoding('utf8')
except:
        #just in python3  module 'sys' has no attribute 'setdefaultencoding'
        print ("it is python3")


if len(sys.argv) < 3 :
        print("PLS use %s <serch_key_list> <mail_to_list>" % sys.argv[0])
        print('''such as python3 smzdm_youhui.py "巧克力;纸尿布" "9945853@qq.com;wing_pn@613.com"''')
        quit()

def send_mail(sub, contenti, mail_to): 

 
        #####################
        #设置服务器，用户名、口令

        sender = 'wing_pn@163.com'  

        mail_host = 'smtp.163.com'  
        mail_user = sender
        mail_pass = 'xxxxx'
        ######################
        '''''
        to_list:发给谁
        sub:主题
        content:内容
        send_mail("aaa@126.com","sub","content")
        '''
        me=sender
        msg = MIMEText(content,_charset='utf-8') 
        msg['Subject'] = sub 
        msg['From'] = sender
        msg['To'] = mail_to
        mailto_list = mail_to.split(";")

        try: 
                s = smtplib.SMTP() 
                s.connect(mail_host) 
                s.login(mail_user,mail_pass) 
                s.sendmail(me, mailto_list, msg.as_string()) 
                s.close() 
                print( "Send OK" )
                return  True
        except Exception as e: 
                print( "Exception", str(e) )
                return False

def get_site(url) :


        req = request.Request(url)
        req.add_header('User-agent', 'Mozilla 5.10')

        resp = request.urlopen(req)

        if resp.getcode()!=200 :
                return False
        doc = resp.read()
        resp.close()

        return doc




        #print(cl.contents[0])


url = "http://m.smzdm.com/youhui/"

doc = get_site(url)

page_data=doc.decode('UTF-8')

#print(page_data)
soup=BeautifulSoup(page_data, "html.parser")  

ul = soup.find( id="post_list_preferential")

content = ""

item_list = []
org_list = []

try:
        path = os.environ["TEMP"]

except:
        path = "/tmp"

path = path +'/smzdm_youhui_' + sys.argv[1] + '.txt'


#调出老列表
try:
        with open(path, 'rb')  as f:
                org_list=pickle.load(f)
                f.close()
except :
        print( "open %s for read error" % path )

search_list = sys.argv[1].split(";")

#查找列表
for li in ul.findAll("li"):
        item_title =  li['onclick'].split("'")[7]
        item_id =  li.find('a')['appurl'] 
        item_herf = li.find('a')['href'] 

        item_list.append(item_id)

        if item_id in org_list:
                #print ( "hash found:" , item_title, item_id )
                continue

        print( 'new item: %s ---id--- %s' %( item_title, item_id) )



        #搜索关键字
        for key in search_list:
                if item_title.find(key) > 0 :

                        #print( item_title.split("'")[7] )
                        content = content + item_title +   item_herf + '\n'
                        break


#保存列表
with open( path , 'wb') as f:
        pickle.dump(item_list, f )
        f.close()


#发送邮件提醒
if len(content)>10 :
        print ( "SEND MAIL" +  content ) 
        send_mail("youhui:" + sys.argv[1],   content  , sys.argv[2] )