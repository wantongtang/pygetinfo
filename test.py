# coding:utf-8
import urllib2
import re
import sys
reload(sys)  
sys.setdefaultencoding('utf8') 
reg1 = r'a href=\'\d\d/\d\d\d\d\.html\'>(\d*)</a>'
reg2 = r'a href=\'\d\d/\d\d\d\d\.html\'>(\W*)</a>'
output1=open('myresult.txt','a')
mycode=[]
myplace=[]
for x in range(11,66):
	url='http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/'+str(x)+'.html'
	try:
		req = urllib2.Request(url)
		res = urllib2.urlopen(req)
		content = res.read().decode('gb2312')
		item = re.findall(reg1,content)
		item2 = re.findall(reg2,content)
		
		for ite in item:
			mycode.append(ite)
		for ite in item2:
			myplace.append(ite)
	except:
		pass
for x in range(len(mycode)):
	print "%s : %s "%(mycode[x],myplace[x])
	output1.write("\n %s   %s "%(mycode[x],myplace[x]))

output1.close()

	
