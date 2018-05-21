import urllib.request as urllib2
from bs4 import BeautifulSoup
import collections
from datetime import datetime
from operator import itemgetter


def main(strin):

	startTime = datetime.now()

	quote_page = "http://www.spoj.com/problems/tag/%s"%strin

	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, "html.parser")
	name_box  = soup.find_all("td", class_="text-center")

	solve = []
	ques = []
	name = []

	for link in soup.select('td.text-center a[href]'):
		a = link['href']
		b,c,d=link['href'].split('/')
		qe = "http://www.spoj.com/problems/%s/"%d
		par = []
		par.append(int(link.text))
		par.append(qe)
		par.append(d)
		solve.append(par)
	solve.sort(reverse = True)	
	
	return 	solve

	
