# 关于
可以用于什么值得买的特定优惠提醒，只要 smzdm 里面有特定关键字的新优惠， 就可以发给指定邮箱。



# 运行方式  
命令行运行，关键字和邮箱都可以以分号间隔:  
注意 smzdm.py 里面的发送邮件服务器，用户名密码需要使用者自行修改~！   

python   smzdm.py "狗粮" 9945853@qq.com  

python3  smzdm.py "u盘;纸尿;巧克力" "9945853@qq.com;nolan.peng@surcdn.com"  

注意每次运行以后都会保存在临时目录一个文件，保存已经扫描过的内容，所以多次运行不会发送同样的优惠信息。  

#平台
已经在  python 3.5.2 (windows) , python 3.5.1 and python 2.6.6 (linux)  进行过测试  

#细节
1. 使用urllib/urllib2获取 m.smzdm.com 的网页  
2. 使用beautifulsoup库解析HTML，得到这一时间点页面上的items  
3. 根据历史记录过滤 items ， 上次已经扫描过的 items 不再扫描  
4. 根据关键字匹配 items  
5. 符合关键字的 items 信息使用 send_mail 发送到指定邮箱  

# 补充
建议加入linux中的crontab，让脚本每分钟自动运行，这样可以不断地扫描特定的优惠信息。 也可以加入到windows的计划任务  
比如：  
# crontab  -l  
* * * * *   date >> /var/log/smzdm.log ; /usr/local/bin/python3  /home/anth/smzdm.py "u盘;纸尿;巧克力" "9945853@qq.com;nolan.peng@surcdn.com" >> /var/log/smzdm.log
