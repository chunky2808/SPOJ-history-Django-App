
import urllib.request as urllib2
from bs4 import BeautifulSoup
import collections
from datetime import datetime
from multiprocessing import Pool
from operator import itemgetter
import multiprocessing 

ans = []
name_question = []


def link_generate(name_question,user,list_links):
	for name_question in name_question:
		if name_question == '':
			a =1
		else:
			quote_page = "http://www.spoj.com/status/%s,%s/"%(name_question,user) #Replace it with your user name
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
		#print(l)
		return l	
		
#crawling pages by link from list

def main(user):
	
	quote_page = "http://www.spoj.com/users/%s/"%user #Replace it with your user name

	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, "html.parser")

	name_question = [] #list of solved problems

	list_links=[]

	#extract name of question from main page of user
	#print(soup.find_all("table", class_="table table-condensed"))

	for name in soup.find_all("table", class_="table table-condensed"):
		name = name.text.replace('\n',' ')
		#print(name)
		a = len(name)
		c=0
		d=0
		lis = []
		for b in range(a):
			if(name[b]!=' '):
				if(c==0):
					lis.append(name[b])
					c+=1
				elif(d==0 and c!=0):
					lis.append(name[b])
			elif(name[b]==' ' and c!=0):
				c=0
				my = ''.join(lis)
				print(my)
				lis = []
				name_question.append(my)			

		#print(name_question)

	# for name in soup.find_all('td'):
	# 		name_question.append(name.text)
	# #extract name of question from main page of user



	#as each url has fixed pattern , exploit that property and go to each problem page(open the page) and scrap time of each page in dictonary along with their name
	i=0
	ans = []
	print(name_question)

	link_generate(name_question,user,list_links)
	print(list_links)
	startTime = datetime.now()

	with Pool(processes=10) as p:
		ans = p.map(crawl,list_links)
		p.close()
		p.join()
	print(datetime.now() - startTime)	#time taken
	

	ans.sort(key=itemgetter('time'))
	# #print(ans)

	# for ans in ans:
	# 	#print(ans['name'])
	# 	f = open('submission_list.csv', 'a')
	# 	f.write(ans['name'])
	# 	f.write('\n')
			
	print("Time taken in crawling account")
	print(datetime.now() - startTime)	#time taken
	return(ans)