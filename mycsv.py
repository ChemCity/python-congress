#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import csv

def write_csv():
	csv_path = sys.path[0] + '\\csv_data.csv'
	print("python csv文件写读操作示例")
	with open(csv_path,'w',newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['中国人']*5+['Deeptest'])
		spamwriter.writerow(['hello', 'Study Python3', 'Auto Testing'])
		csvfile.close()
	with open(csv_path,'r') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			print("row的类型",type(row))
			print(row)
		f.close()
		
if __name__=="__main__":
	write_csv()