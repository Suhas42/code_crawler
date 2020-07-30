from django.shortcuts import render, HttpResponse
import urllib3
import json

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

    context = {'cf_contest_list': cf_contest_list,'string': string, 'cf_contest_link': cf_contest_link}
    return render(request, 'calender.html', context)







