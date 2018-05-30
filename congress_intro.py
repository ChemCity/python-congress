#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
获取第13届全国人大代表北京代表团名单
'''
import urllib.request, sys
import re
import random
import csv

file_path = sys.path[0] + "\\wea.txt"
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
获取全国各省份编号
''' 
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
		print('\t' + item[0] + '\t' + item[1])
	print(len(num))
	return num
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
'''	
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
'''	
def save_csv():
	csv_path = sys.path[0] + '\\csv_data_info.csv'
	with open(csv_path,'w',newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		#获取省份编号	
		province_num = get_province_num()
		#province_num = ['c4']
		for item in province_num:
			res = num,name,info,tit = get_congress(item[0], 'gbk')
			spamwriter.writerow([tit])

			length = len(num)
			for i in range(0,length):
				spamwriter.writerow([num[i]]+[name[i]] + info[i])
		csvfile.close()
if __name__=="__main__":

	save_csv() 
	#get_congress("c5", 'gbk')