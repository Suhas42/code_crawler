from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup
import urllib3
import json
import requests
from bs4 import BeautifulSoup
# Create your views here.
def calender(request):
    # return render(request, 'home.html')
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://codeforces.com/api/contest.list?gym')
    cf_contest_list = json.loads(r.data.decode('utf-8'))
    cf_contest_list = cf_contest_list["result"]
    cf_contest_list = cf_contest_list[:10]
    string = "BEFORE"
    cf_contest_link = "https://codeforces.com/contests/"

    # function for sorting according to start time
    def fun(e):
        return e['startTimeSeconds']

    cf_contest_list.sort(key=fun)
<<<<<<< HEAD

    soup = requests.get('https://www.codechef.com/contests/?itm_medium=navmenu&itm_campaign=allcontests#future-contests')
    soup = BeautifulSoup(soup.content, 'html')
    soup = soup.find(id='future-contests')
    soup = soup.next_sibling.next_sibling
    soup = soup.find_all('td')
    result = []
    links = []
    for tag in soup:
        # print (tag.text)
        result.extend(tag.stripped_strings)
        link = tag.find('a')
        if link!= None:
            link = link.get('href')
            links.append(link)
    chef_contest_list = []
    count = len(links)
    print(count)
    for i in range(count):
        list = []
=======
    
    
    soup = requests.get('https://www.codechef.com/contests/?itm_medium=navmenu&itm_campaign=allcontests#future-contests')
    soup=BeautifulSoup(soup.content,'html')
    soup=soup.find(id='future-contests')
    soup=soup.next_sibling.next_sibling
    soup=soup.find_all('td')
    result=[]
    links=[]
    for tag in soup:
    #print (tag.text)
        result.extend(tag.stripped_strings)
        link=tag.find('a')
        if link!=None :
            link=link.get('href')
            links.append(link)
    chef_contest_list=[]
    count=len(links)
    print (count)
    for i in range (count):
        list=[]
>>>>>>> d8d991e1f6f0c2a6a0b6a130288c8a4c3b2e421e
        list.append(links[0])
        links.pop(0)
        result.pop(0)
        for j in range(3):
            list.append(result[0])
            result.pop(0)
<<<<<<< HEAD
        result.pop(0), result.pop(0)
        chef_contest_list.append(list)
        print(chef_contest_list)
        chef_contest_link = "https://www.codechef.com"
        context = {'cf_contest_list': cf_contest_list,
                   'string': string,
                   'cf_contest_link': cf_contest_link,
                   'chef_contest_list': chef_contest_list,
                   'chef_contest_link': chef_contest_link }
=======
        result.pop(0),result.pop(0)
        chef_contest_list.append(list)
        print(chef_contest_list)
<<<<<<< HEAD
        chef_context_link = "https://www.codechef.com"
        context = {'cf_contest_list': cf_contest_list, 'string': string, 'cf_contest_link':cf_contest_link,'chef_contest_list':chef_contest_list,}
>>>>>>> d8d991e1f6f0c2a6a0b6a130288c8a4c3b2e421e
=======
        chef_contest_link = "https://www.codechef.com"
        context = {'cf_contest_list': cf_contest_list, 
                   'string': string, 
                   'cf_contest_link':cf_contest_link, 
                   'chef_contest_list':chef_contest_list, 
                   'chef_contest_link':chef_contest_link}
>>>>>>> 0003d5a3f3ac9399fcb96ba5dd838e15c51ffbbf
    return render(request, 'calender.html', context)







