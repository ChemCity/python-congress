# -*- coding: UTF-8 -*-
from urllib import request
import sys
if __name__ == "__main__":
	#访问网址
	url = 'http://www.dianping.com/search/category/2/10/g311'
	#这是代理IP
	proxy = {'http':'124.88.67.81:80'}
	#创建ProxyHandler
	proxy_support = request.ProxyHandler(proxy)
	#创建Opener
	opener = request.build_opener(proxy_support)
	#添加User Angent
	#opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
	opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48')]
	# 使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理。
	response = opener.open(url)
	
	# 就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
	#安装OPener
	#request.install_opener(opener)
	#使用自己安装好的Opener
	#response = request.urlopen(url)
	
	#读取相应信息并解码
	html = response.read().decode("utf-8")
	#打印信息
	print(html)
	
		#将获取信息写入 
	file_path = sys.path[0] + "\\wea.txt"		
	f=open(file_path,'wb')  
	f.write(html.encode('utf-8'))  
	f.close()