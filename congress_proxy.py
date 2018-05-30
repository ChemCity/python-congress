#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
代理的使用
测试decode第二个参数,当网页编码含有不标准字符(圆角回车),
可使用ignore
'''
import urllib.request, sys
import re

file_path = sys.path[0] + "\\wea.txt"
'''
代表名单
'''
def get_congress(num_value, type):
	url = "http://www.npc.gov.cn/delegate/dbmd.action?id=" + num_value
	request=urllib.request.Request(url)
	#url = "http://www.npc.gov.cn/delegate/dbmd.action?id=4028819f6178f1fb0162b7fcf0700001"
		#获取页面信息  
	html = urllib.request.urlopen(request)  
	res = html.read().decode(type, 'ignore')  
	
	#正则表达式信息  
	pattern = '"tit1">(.+)</div>'  
	Title = re.search(pattern,res).group(1)
	#代表编号
	pattern = 'dbid=(\d*)'
	number = re.findall(pattern, res)
	#代表姓名
	pattern = '"_blank">(.+)</a>'
	names = re.findall(pattern, res)
	
	length = len(number)
	#print(length)
	print ("\n%35.30s\n"%Title)
	text_str = Title + '\r\n'
	for i in range (0,length):  
		print ('%25.20s'%number[i], '\t%s'%names[i])
		text_str += " " + number[i] + ' \t' + names[i] + '\r\n'
	return text_str 

#使用代理获取local 名单	
def proxy_get_congress(num_value, type):
	#访问网址
	url = "http://www.npc.gov.cn/delegate/dbmd.action?id=" + num_value
	#这是代理IP
	proxy = {'http':'117.36.103.170:8118'}
	#创建ProxyHandler
	proxy_support = urllib.request.ProxyHandler(proxy)
	#创建Opener
	opener = urllib.request.build_opener(proxy_support)
	#添加User Angent
	opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')]
	#安装OPener
	#urllib.request.install_opener(opener)
	#使用自己安装好的Opener
	#response = urllib.request.urlopen(url)

	response = urllib.request.urlopen(url)
	#读取相应信息并解码
	res = response.read().decode(type, 'ignore')  
	
	#正则表达式信息  
	pattern = '"tit1">(.+)</div>'  
	Title = re.search(pattern,res).group(1)
	#代表编号
	pattern = 'dbid=(\d*)'
	number = re.findall(pattern, res)
	#代表姓名
	pattern = '"_blank">(.+)</a>'
	names = re.findall(pattern, res)
	
	length = len(number)
	#print(length)
	print ("\n%35.30s\n"%Title)
	text_str = Title + '\r\n'
	for i in range (0,length):
		print ('%25.20s'%number[i], '\t%s'%names[i])
		text_str += " " + number[i] + ' \t' + names[i] + '\r\n'
	return text_str 
if __name__=="__main__":

	#c4 是重庆 我人在重庆 无法获取
	#proxy_get_congress("c4", 'gbk')
	get_congress("c4", 'gbk')
	
	
	
	