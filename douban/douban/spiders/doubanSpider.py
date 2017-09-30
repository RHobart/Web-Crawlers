import scrapy
from douban.items import *

class doubanmovie(scrapy.Spider):
    name='douban'
    allowed_domains=["douban.com"]
    start_urls=[
        #"https://movie.douban.com/top250"
        "https://movie.douban.com/chart"
    ]

    def parse(self,response):
        #inf = response.xpath('//div[@class="indent"]/div[@class=""]/table/tbody/tr[@class="item"]')
        inf=response.xpath('//tr[@class="item"]')
        i = 1
        for img in inf:
            name=img.xpath('td[2]/div/a/span/text()').extract()[0]
            url=img.xpath('td[2]/div/a/@href').extract()[0]
            img=img.xpath('td[1]/a/img/@src').extract()[0]
            print("第"+str(i)+"电影信息:"+'\n')
            print("name:"+str(name)+'\n')
            print("url:"+str(url)+'\n')
            print("img:"+str(img)+'\n')
            i+=1
