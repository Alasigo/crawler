#coding:utf8
'''
Created on 2018��5��8��

@author: Administrator
'''
from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a',href = re.compile(r"/u/\d"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
            return new_urls
    
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        
        res_data['url'] = page_url
        
        user_note = soup.find('h1',class_ = 'username')
        res_data['user'] = user_note.get_text()
        
        return res_data
    
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding = 'utf-8')
        new_urls = self._get_new_urls(page_url,soup)#解析得到新的url
        new_data = self._get_new_data(page_url,soup)#解析得到页面内容
        return new_urls,new_data
    
    



