# coding :utf-8

import urllib2
import re

url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/index.html'
baseurl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/'


def get_html(url):
	try:	
		website = urllib2.urlopen(url)
		html =  website.read().decode('gb2312','ignore')
		website.close()
		return html
	except:
		print"warning not_get_html"
		return False

def get_link(html,reg):
	if html:	
		return re.findall(reg,html)
	else:
		return 0
	


reg = r'<a href=\'(\d*/\d*|\d*)\.html\'>'
reg31 = r'<td>(\d{12})</td>'
reg32 = r'<td>(\W*|\W+\d*\W*|\d*\W+|\W+\w+\W+|\W+\w+)</td>'
alllink = get_link(get_html(url),reg)
for link in alllink:
#	print baseurl+link+'.html'
	alllink1 = get_link(get_html(baseurl+link+'.html'),reg)
	for link1 in alllink1:
#		print baseurl+link1+'.html'	
		alllink2 = get_link(get_html(baseurl+link1+'.html'),reg)
		if alllink2:
			for link2 in alllink2:
#				print baseurl+link1.split('/')[0]+'/'+link2+'.html'
				alllink3 = get_link(get_html(baseurl+link1.split('/')[0]+'/'+link2+'.html'),reg)
				if alllink3:
					for link3 in alllink3:
						print baseurl+link1.split('/')[0]+'/'+link2.split('/')[0]+'/'+link3+'.html'
						html3 = get_html( baseurl+link1.split('/')[0]+'/'+link2.split('/')[0]+'/'+link3+'.html')
						if html3:
							code3 = re.findall(reg31,html3)
							name3 = re.findall(reg32,html3)
							print len(code3)
							print len(name3)
							for x3 in range(len(code3)):
								print ("%s %s"%(code3[x3],name3[x3+1]))
		
