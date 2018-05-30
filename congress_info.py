#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
获取单个代表的信息
'''
import urllib.request, sys
import re
import random


'''
获取各个省份的人大代表名单
'''
def get_congress(num_value, cod):
	url = "http://www.npc.gov.cn/delegate/dbmd.action?id=" + num_value
	request=urllib.request.Request(url)
	#url = "http://www.npc.gov.cn/delegate/dbmd.action?id=4028819f6178f1fb0162b7fcf0700001"
		#获取页面信息  
	html = urllib.request.urlopen(request)  
	res = html.read().decode(cod, 'ignore')  
	
	#正则表达式信息  
	pattern = '"tit1">(.+)</div>'  
	Title = re.search(pattern,res).group(1)
	#代表编号
	pattern = 'dbid=(\d*)'
	number = re.findall(pattern, res)
	#代表姓名
	pattern = '"_blank">(.+)</a>'
	names = re.findall(pattern, res)
	#print(type(number))
	#print(type(names))
	length = len(number)
	#print(length)
	print ("\n%35.30s\n"%Title)
	text_str = Title + '\r\n'
	info = []
	#print(type(number))
	for i in range (0,length):  
		#print ('%25.20s'%number[i], '\t%s'%names[i])
		info.append( get_congress_info(number[i], cod) )
		
	return number,names,info,Title

'''
获取每个代表的个人信息
'''
def get_congress_info(num, cod):
	
	randstr = str(random.randint(10,99))	#网址最后两位是随机数
	year = '2008'				#固定
	url = 'http://www.npc.gov.cn/delegate/viewDelegate.action?dbid=' + year + num + randstr
	request = urllib.request.Request(url)
	html = urllib.request.urlopen(request)
	res = html.read().decode(cod, 'ignore')
	#print(res)
	pattern = 'bg2>(.+)</TD>'
	info = re.findall(pattern, res)
	#print(type(info))
	return info
	
	
if __name__=="__main__":
	#get_congress_info('132034','gbk')
	res = get_congress('c5', 'gbk')
	print(res)
	