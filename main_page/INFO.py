import requests
import bs4
from lxml import etree
tostr = etree.tostring
from io import StringIO



def information(breed):
	dogname=breed
	main=[]
	ans=[]
	main=dogname.split(" ")
	print(main)
	if len(main) == 2:
		r= requests.get("https://en.wikipedia.org/wiki/{}_{}".format(main[0],main[1]))
	else:
		r= requests.get("https://en.wikipedia.org/wiki/{}".format(dogname))
	tree=etree.parse(StringIO(r.text))

	for i in tree.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[3]/td/div/ul'):
		for j in i.xpath('./li'):
			print(tostr(j, method='text', encoding='utf8'))
			ans.append(tostr(j, method='text', encoding='utf8'))
	return ' '.join(ans)		