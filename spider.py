from selenium import webdriver
import re
import os

browser = webdriver.Chrome()
blocka = re.compile('<a href="(.*?)" target="_blank" class="small14">(.*?)</a>')
nextpage = re.compile('<a href="(.*?)" target="_blank">下一页</a>')
bodytext = re.compile('<br>\s"(.*?)"')

def getUrl():
	urllist = []
	for i in range(1, 14):
		req_url = "https://www.51test.net/sifa/st/list/%d/" % i
		browser.get(req_url)

		html = browser.page_source
		# browser.close()
		# print(html.encode().decode('gb2312'))
		# print(html[:200])

		tmp = blocka.findall(html)
		urllist += [(v[0], v[1]) for v in tmp]
	# browser.close()
	return urllist

def getTestText(url, title):
	browser.get(url)
	fout = open('html/%s.html' % title, 'w')
	html = browser.page_source
	# alltext = re.findall(r'<br>\n"(.*?)"', html, re.S)
	alltext = re.findall('<div class="content-txt">(.*?)<div class="show_content_next">', html, re.S)
	# print(html[:100000])
	try:
		print('<div class="content-txt">\n%s\n</div>' % alltext[0], file = fout)
	except:
		pass
	# print(html[:50000])
	nextpageurl = nextpage.findall(html)[0]

	browser.get('https://www.51test.net%s' % nextpageurl)
	
	html = browser.page_source
	alltext = re.findall('<div class="content-txt">(.*?)<div class="show_content_next">', html, re.S)
	try:
		print('<div class="content-txt">\n%s\n</div>' % alltext[0], file = fout)
	except:
		pass


if __name__ == '__main__':
	'''
	url = '/show/8577147.html'
	title = re.compile(r'<title>(.*?)_国家司法考试_无忧考网</title>')
	while url:
		try:
			browser.get('https://www.51test.net%s' % url)
			html = browser.page_source
			alltext = re.findall('<div class="content-txt">(.*?)<div class="show_content_next">', html, re.S)
			texttitle = title.findall(html)
			print(texttitle)
			fout = open(os.path.join('exam_wuyou', texttitle), 'w')
			print('<div class="content-txt">\n%s\n</div>' % alltext[0], file = fout)
		except:
			pass
		
		url = nextpage.findall(html)[0]
	print('end!')
	browser.colse()
	'''
	urllist = getUrl()
	for v in urllist:
		try:
			print(v[1])
			getTestText('https://www.51test.net%s' % v[0], v[1])
		except Exception as err:
			print(err)
	print('end!')
	browser.close()
	