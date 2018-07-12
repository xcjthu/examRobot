import re
import json

import os
import time

def trans():
	l = os.listdir('html')
	for v in l:
		fin = open(os.path.join('html', v), 'r', encoding = 'gbk')
		fout = open(os.path.join('examP', v), 'w', encoding = 'utf8')
		html = fin.read()
		alltext = re.findall('<div class="content-txt">(.*?)<div class="clear-both"></div>', html, re.S)
		try:
			print('<div class="content-txt">\n%s\n</div>' % alltext[0], file = fout)
		except:
			print('err')

def analyzer():
	l = os.listdir('examP')
	for v in l:
		fin = open(os.path.join('examP', v), 'r')
		html = fin.read()
		fout = open(os.path.join('tmp', v), 'w')
		html = re.sub('<div class="describe"><i></i>.*?</div>', '', html)
		html = re.sub('<p style="text-indent:2em;"><font color="#0000FF">司法考试频道为大家推出【<a href="http://union.chinaacc.com/union/advertHit/advertHit.shtm\?advertID=508&amp;agentID=68&amp;toUrl=http://www.chinalawedu.com/project/2014sfks\.shtml#bc" target="_blank">2017年司法考试一次课程！</a>】考生可点击以下入口进入免费试听页面！足不出户就可以边听课边学习，为大家的取证梦想助力!</font></p><br /><p style="text-indent:2em;"><a href="http://union.chinaacc.com/union/advertHit/advertHit.shtm\?advertID=2256&amp;agentID=68&amp;toUrl=http://m.chinalawedu.com/project/2014sfks.shtml" target="_blank"><strong><font style="FONT-SIZE: 18px" color="#ff0000"><font color="#0000ff">【手机用户】→</font>点击进入免费试听&gt;&gt;</font></strong></a></p><br /><p style="text-indent:2em;"><a href="http://union.chinaacc.com/union/advertHit/advertHit.shtm\?advertID=2256&amp;agentID=68&amp;toUrl=http://www.chinalawedu.com/project/2014sfks.shtml" target="_blank"><font style="FONT-SIZE: 18px"><strong><font color="#0000ff">【电脑用户】→</font><font color="red">点击进入免费试听&gt;&gt;</font></strong></font></a></p><br /><a href="http://union.chinaacc.com/union/advertHit/advertHit.shtm\?advertID=1659&amp;agentID=68" target="_blank"><img name="AdsHttp" src="http://img.cdeledu.com/ADVC/2016/0902/1472779573036-0.jpg" width="500" height="189" alt="" border="0" /></a>', '', html)
		html = re.sub('<div class="content-txt">', '', html)
		html = re.sub('</div>', '', html)
		# html = re.sub('<p>', '', html)
		# html = re.sub('</p>', '', html)
		html = re.sub('【导语】.*?<.*?>', '', html)
		html = re.sub('导语.*<.*?>', '', html)
		html = html.replace(r'\n', '')
		html = html.replace('\u3000', '')

		print(html, file = fout)


answerSign = re.compile(r'[\[【]?(?:参考)?(?:正确)?答案[】\]]')
answerDraw = re.compile(r'([\[【]?(?:参考)?(?:正确)?答案[】\]]?.*?)<')
repre0 = re.compile(r'(\d+[\.、].+?)<.*?>(A.*?)<.*?>(B.*?)<.*?>(C.*?)<.*?>(D.*?)<.*?>([\[【]?(?:参考)?(?:正确)?答案[】\]]?.*?)<')
repre1 = re.compile(r'(\d+[\.、].+?)<.*?>(A.*?)<.*?>(B.*?)<.*?>(C.*?)<.*?>(D.*?)<.*?>')

def draw_Test(alltext):
	a = len(answerSign.findall(alltext))
	if a > 1:
		pass
		drawout = repre0.findall(alltext)
		return drawout
		
	elif a == 1:
		drawout = repre1.findall(alltext)
		drawout += answerDraw.findall(alltext)
		print(drawout)
		return drawout
	elif a == 0:
		pass


if __name__ == '__main__':
	l = os.listdir('examP')
	fout = open('drawout.json', 'w')
	for v in l:

		fin = open(os.path.join('examP', v), 'r')
		html = fin.read()
		if '卷四' in v or '卷4' in v:
			pass
		elif '题及答案' in v:
			tmp = draw_Test(html)
			if not tmp is None and len(tmp) > 0:
				print(v)
				print(json.dumps(tmp, ensure_ascii = False), file = fout)

		time.sleep(0.1)

# analyzer()

