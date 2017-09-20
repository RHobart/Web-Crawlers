#necoding="utf-8"
__author__='Hobart'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import urllib.request
import pymysql
import re
import os
import time 
#启动谷歌浏览器驱动
def start_brower(url):
	driver=webdriver.Chrome()
	driver.get(url)
	time.sleep(5)
	return driver
#动态获取图片信息
def get_img_information(location,last_location,count,driver):
	#当鼠标的位置小于最后的鼠标位置时,循环执行
	while location<last_location:
		#获取页面源码
		html_page=driver.page_source
		#利用Beautifulsoup4创建soup对象并进行页面解析
		soup=bs(html_page,"html.parser")
		time.sleep(2)
		#通过soup对象中的findAll函数图像信息提取
		imgs=soup.findAll('img',{'src':re.compile(r'https:.*\.(jpg|png)')})
		time.sleep(2)
		#将图片信息存储到Mysql数据库中
		for img in imgs:
			print(str(count)+':'+img.get('src')+'\n')
			name=str(count)
			style=img.get('src')[-3:]
			data=img.get('src')
			cursor.execute("insert into img (img_name,img_stype,img_data) values(%s,%s,%s)",(name,style,data))
			conn.commit()
			count+=1
		time.sleep(2)
		#通过Selenium模拟鼠标滚动
		js="$(document).scrollTop(%d)"%location  
		driver.execute_script(js) 
		location+=500
		time.sleep(3)
		imgs=[]


url="https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%B7%E7%BE%B0%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111"
#启动浏览器，打开网站
driver=start_brower(url)
#mysql数据库连接方式
conn=pymysql.connect(host='localhost',port=3306,user='admin',password='admin',db='img')
if conn:
	print("数据库连接成功")
	cursor=conn.cursor()
	get_img_information(0,3000,1,driver)
	cursor.close()
	conn.close()
else:
	print("数据库连接失败")
#退出浏览器
driver.quit()




