#necoding="utf-8"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import urllib.request
import re
import os
import time 

driver=webdriver.Chrome()
driver.get("https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=detail&fr=&hs=0&xthttps=111111&sf=1&fmq=1505741119622_R&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%99%AF%E7%94%9C%E5%9B%BE%E7%89%87&oq=%E6%99%AF%E7%94%9C&rsp=0")
time.sleep(5)
count=500
i=1
while count<4000:
	html_page=driver.page_source
	soup=bs(html_page,"html.parser")
	imgs=soup.findAll('img',{'src':re.compile(r'https:.*\.(jpg|png)')})
	time.sleep(2)

	for img in imgs:
		print(str(i)+':'+img.get('src')+'\n')
		urllib.request.urlretrieve(img.get('src'),r'C:/img/%s.%s'%(i,img.get('src')[-3:]))
		i+=1
	time.sleep(1)

	js="$(document).scrollTop(%d)"%count  
	driver.execute_script(js) 
	count+=500
	time.sleep(3)
	imgs=[]

time.sleep(3)
driver.quit()


