#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

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
		get_wiki(names[i])
		text_str += " " + number[i] + ' \t' + names[i] + '\r\n'
	return text_str 
def get_wiki(name):

	params = urllib.parse.quote(name)
	search = "search/word?word=" + params
	
	#url = 'https://baike.baidu.com/item/%E4%B9%A0%E8%BF%91%E5%B9%B3'
	#url = 'https://baike.baidu.com/search/word?word=%E4%B9%A0%E8%BF%91%E5%B9%B3'
	url = 'https://baike.baidu.com/' + search
	agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
	request = urllib.request.Request(url)
	html = urllib.request.urlopen(request)
	res = html.read().decode('utf-8')
	
	pattern = '<meta name="description" content="(.+)">'
	title = re.search(pattern, res).group(1)
	
	print(title)
if __name__=="__main__":

	#get_congress("c4", 'gbk')
	get_wiki('马善祥')
	
	
	
	