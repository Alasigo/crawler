#coding:utf8
'''
Created on 2018��5��8��

@author: Administrator
'''


class UrlManager(object):
    def __init__(self):
        #初始化
        self.new_urls = set()#待爬取的URL集合
        self.old_urls = set()#已爬取的URL集合
    
    def add_new_url(self,url):#向管理器中添加一个URL
        if url is None:#如果没有URL，则返回
            return
        if url not in self.new_urls and url not in self.old_urls:#如果URL既不在待爬取的集合中也不在已爬取的集合中（即是新的url），则添加进待爬取的url集合中
            self.new_urls.add(url)
    
    
    def add_new_urls(self,urls):#向管理器中批量添加URL
        if urls is None or len(urls) == 0:
            return
        for url in urls:#向url管理器中一条一条添加
            self.add_new_url(url)
    
    
    def has_new_url(self):#判断管理器中是否存在新的待爬取得URL
        return len(self.new_urls) != 0#待爬取的集合长度不为0，即表示存在带爬取得url

    
    def get_new_url(self):#从管理器中获取一个新的待爬取得URL
        new_url = self.new_urls.pop()#pop方法会获取在set中获取一个url并移除此url
        self.old_urls.add(new_url)#将这个url添加进已爬取集合
        return new_url#返回此url

    
    
    
    
    
    
    
    
    
    



