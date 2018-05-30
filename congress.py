#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
获取第13届全国人大代表北京代表团名单
'''
import urllib.request, sys
import re

file_path = sys.path[0] + "\\wea.txt"
'''
获取各个省份的人大代表名单
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
'''
获取全国各省份编号
''' 
def get_province_num():
	#将获取信息写入  
	url = 'http://www.npc.gov.cn/delegate/delegateArea.action'
	html = urllib.request.urlopen(url) 
	#print(html.encoding)
	res = html.read().decode("gbk")
	
	pattern = 'value="(.\d)"'
	num = re.findall(pattern, res)
	
	pattern = 'value=".\d">(.+)</option>'
	province = re.findall(pattern, res)
	#print(province)
	return num
	

def save_file():
		#将获取信息写入  
	f=open(file_path,'wb')  
		
	province_num = get_province_num()
	#province_num.remove("c4")		#local 重庆??? 页面有全角字符
	length = len(province_num)
	
	for i in range (0, length):
		res = get_congress(province_num[i], 'gbk')
		f.write(res.encode('utf-8'))  
		
	f.close()
if __name__=="__main__":

	save_file() 
	#get_congress("c5", 'gbk')