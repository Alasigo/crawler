# coding:utf8
'''
Created on 2018��5��8��

@author: Administrator
'''
from weibo import url_manager, html_downloader, html_outputer, html_parser


class SpiderMain(object):
    def __init__(self):
        #初始化URL管理器，下载器、解析器、输出器
        #Ctrl+1 import 引入
        #ctrl+1 create class 创建class
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_url):
        count = 1#计数
        self.urls.add_new_url(root_url)#将入口url添加进管理器
        while self.urls.has_new_url():#当URL管理器中有带爬取得URL时启动爬虫循环
           # try:#捕获异常
            new_url = self.urls.get_new_url()#获取管理器中的URL
            print ("craw %d : %s" % (count,new_url))#输出这是爬取得第几个URL以及它的URL
            html_cont = self.downloader.download(new_url)#下载器下载页面
            new_urls,new_data = self.parser.parse(new_url,html_cont)#利用解析器解析出新的URL和收集数据
            self.urls.add_new_urls(new_urls)#新的URL添加到URL管理器
            self.outputer.collect_data(new_data)#数据添加到输出器
                
            if count == 1000:#爬取1000个URL
                break
                
            count = count + 1
          #  except Exception as e:
           #     print (str(e))
        self.outputer.output_html()#输出收集好的数据
    
    



if __name__=="__main__":
    root_url = "https://weibo.com/u/1750157883?refer_flag=1001030101_&is_hot=1"#入口url
    obj_spider = SpiderMain()#爬虫总调ctrl+1 create class
    obj_spider.craw(root_url)#启动爬虫  ctrl+1 create method