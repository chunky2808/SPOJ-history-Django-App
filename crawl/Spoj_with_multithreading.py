import urllib.request as urllib2
from bs4 import BeautifulSoup
import collections
from datetime import datetime
from multiprocessing import Pool
from operator import itemgetter

def link_generate(name_question):
	for name_question in name_question:
		if name_question == '':
			a =1
		else:
			quote_page = "http://www.spoj.com/status/%s,chunky_2808/"%name_question #Replace it with your user name
			list_links.append(quote_page)
						

#crawling pages by link from list
def crawl(name_question):
	l = {}
	quote_page = name_question
	#print(quote_page)
	page = urllib2.urlopen(quote_page)
	if page.getcode() == 200:
		soup = BeautifulSoup(page, "html.parser")
		name_box  = soup.find_all("td", class_="status_sm")[-1]
		name = name_box.text.replace('\n','')#time
		l.update({"time" : name, "name" : name_question})#inserting in list (time of submit ,name of question)
		return l
		#print(l)
#crawling pages by link from list

def main(user):
	startTime = datetime.now()

	quote_page = "http://www.spoj.com/users/chunky_2808/" #Replace it with your user name

	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, "html.parser")

	name_question = [] #list of solved problems

	#extract name of question from main page of user
	for name in soup.find_all('td'):
			name_question.append(name.text)
	#extract name of question from main page of user


	#as each url has fixed pattern , exploit that property and go to each problem page(open the page) and scrap time of each page in dictonary along with their name
	i=0


	list_links = []
	link_generate(name_question)
	#print(list_links)

	with Pool(10) as p:
	    ans = p.map(crawl,list_links)

	ans.sort(key=itemgetter('time'))
	#print(ans)

	for ans in ans:
		print(ans['name'])
		f = open('submission_list.csv', 'a')
		f.write(ans['name'])
		f.write('\n')
			
	print("Time taken in crawling account")
	print(datetime.now() - startTime)	#time taken

