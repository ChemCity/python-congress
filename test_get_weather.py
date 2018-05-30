#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
打印窗口事件
'''
import urllib.request ,sys  
import re  
import json

file_path = sys.path[0] + "\\wea.txt"
def get_weather():  

	#provice = input('输入省份名（请使用拼音）：')  
	#city = input('输入城市名（请使用拼音）：') 
	provice = "chongqing"
	city = 'yongchuan'
	#获取天气的url  
	url = "http://qq.ip138.com/weather/"+provice+'/'+city+'_7tian.htm'  

	#获取页面信息  
	weatherhtml = urllib.request.urlopen(url)  
	res = weatherhtml.read().decode('GB2312')  
	
	#将获取信息写入  
	f=open(file_path,'wb')  
	f.write(res.encode('GB2312'))  
	f.close()  
	
	#正则表达式获取天气信息  
	pattern = 'Title.+<b>(.+)</b>'  
	Title = re.search(pattern,res).group(1)  

	pattern = '>(\d*-\d*-\d*.+?)<'  
	date = re.findall(pattern,res)  

	pattern = 'alt="(.+?)"'  
	weather = re.findall(pattern,res)  
	
	pattern = '<td>(\d.+?\d.)</td>'
	temperature = re.findall(pattern, res)
	
	pattern = '<td>(\w.+)<br/>'		#\w 匹配汉字
	wind = re.findall(pattern, res)
	#print(wind)
	print ("\n%35.30s\n"%Title)  
	length = len(date)
	#l = len(temperature)'\t%s' %temperature[i]
	#print(l)
	for i in range (0,length):  
		print ('%25.20s'%date[i], '\t%s'%weather[i], 
		'\t%s' %temperature[i], '\t%s' %wind[i])  
  
if __name__=="__main__":  
    get_weather()  




