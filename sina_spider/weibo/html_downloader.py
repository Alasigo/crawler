#coding:utf8
'''
Created on 2018��5��8��

@author: Administrator
'''
from urllib.parse import quote
import string
from urllib import request


class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        
        url_ = quote(url,safe = string.printable)
        response = request.urlopen(url_)
        if response.getcode() != 200:
            '''
            getcode()页面请求的状态值：
            200 请求成功
            303 重定向
            400 请求错误
            401 未授权
            403 禁止访问
            404 文件未找到
            500 服务器错误
            '''
            return None
        return response.read()
    
    



