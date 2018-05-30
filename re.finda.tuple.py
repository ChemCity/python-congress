#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
re.finda()函数返回值可以是元素包含两个字符串的元组
'''
import urllib.request, sys
import re

file_path = sys.path[0] + "\\wea.txt"

def get_province_num():
	#将获取信息写入  
	url = 'http://www.npc.gov.cn/delegate/delegateArea.action'
	html = urllib.request.urlopen(url) 
	#print(html.encoding)
	res = html.read().decode("gbk")
	
	pattern = 'value="(.\d)">(.+)</option>'
	num = re.findall(pattern, res)
	
	#pattern = 'value=".\d">(.+)</option>'
	#province = re.findall(pattern, res)
	for item in num:
		print('\t' + item[0] + '\t' + item[1] + '\r\n')
	print(len(num))
	return num
	
if __name__=="__main__":

	get_province_num() 