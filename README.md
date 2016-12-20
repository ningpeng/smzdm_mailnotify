# 关于
可以用于什么值得买的特定优惠提醒，只要 smzdm 里面有特定关键字的新优惠， 就可以发给指定邮箱。



# 运行方式  
命令行运行，关键字和邮箱都可以以分号间隔:  

python   smzdm.py "狗粮" 9945853@qq.com  

python3  smzdm.py "u盘;纸尿;巧克力" "9945853@qq.com;nolan.peng@surcdn.com"  

#平台
已经在  python 3.5.2 (windows) , python 3.5.1 and python 2.6.6 (linux)  进行过测试  

# 补充
建议加入linux中的crontab，让脚本每分钟自动运行，这样可以不断地扫描特定的优惠信息。 也可以加入到windows的计划任务  
比如：  
# crontab  -l  
* * * * *   date >> /var/log/smzdm.log ; /usr/local/bin/python3  /home/anth/smzdm.py "u盘;纸尿;巧克力" "9945853@qq.com;nolan.peng@surcdn.com" >> /var/log/smzdm.log
