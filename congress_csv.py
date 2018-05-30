#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
获取第13届全国人大代表北京代表团名单
'''
import urllib.request, sys
import re
import csv

file_path = sys.path[0] + "\\wea.txt"
'''
根据代表姓名获取百科信息
'''
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
	return title
	#print(title)
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
		#context = get_wiki(names[i])
		text_str += " " + number[i] + ' \t' + names[i] + '\r\n' 
	#return text_str
	return number,names,Title
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
	#获取省份编号	
	province_num = get_province_num()
	#province_num.remove("c4")		#local 重庆??? 页面有全角字符
	length = len(province_num)
	
	for i in range (0, length):
		res = get_congress(province_num[i], 'gbk')
		f.write(res.encode('utf-8'))  
		
	f.close()
def save_csv():
	csv_path = sys.path[0] + '\\csv_data.csv'
	with open(csv_path,'w',newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		#获取省份编号	
		province_num = get_province_num()
		#province_num = ['c4']
		for item in province_num:
			res = num,name,tit = get_congress(item, 'gbk')
			spamwriter.writerow([tit])
			
			length = len(num)
			for i in range(0,length):
				spamwriter.writerow([num[i]]+[name[i]])
		csvfile.close()
if __name__=="__main__":

	
	#get_congress("c5", 'gbk')
	save_csv()