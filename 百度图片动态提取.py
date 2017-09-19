#necoding="utf-8"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import urllib.request
import re
import os
import time 
#启动谷歌驱动
driver=webdriver.Chrome()
#要访问的网站
driver.get("https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=detail&fr=&hs=0&xthttps=111111&sf=1&fmq=1505741119622_R&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%99%AF%E7%94%9C%E5%9B%BE%E7%89%87&oq=%E6%99%AF%E7%94%9C&rsp=0")
#延时5s是因为页面需要加载时间
time.sleep(5)
#count作用是定位滚动条位置
count=500
#i为统计图片数量
i=1
#当鼠标位置小于4000，执行
while count<4000:
	#将页面的源码赋值给你一个对象
	html_page=driver.page_source
	#创建Beautifulsoup4对象
	soup=bs(html_page,"html.parser")
	#读取页面图像信息
	imgs=soup.findAll('img',{'src':re.compile(r'https:.*\.(jpg|png)')})
	#延时2s保证信息能够读完
	time.sleep(2)
	#将图片写入到C盘img文件夹下
	for img in imgs:
		print(str(i)+':'+img.get('src')+'\n')
		urllib.request.urlretrieve(img.get('src'),r'C:/img/%s.%s'%(i,img.get('src')[-3:]))
		i+=1
	#延时1s保证图片能够写完
	time.sleep(1)
	#鼠标自动向下滚动（很重要的）
	js="$(document).scrollTop(%d)"%count  
	driver.execute_script(js) 
	count+=500
	#延时3s保证页面加载完成
	time.sleep(3)
	#清空之前图像链接列表
	imgs=[]
#等待3s退出浏览器
time.sleep(3)
driver.quit()


