from django.shortcuts import render

# Create your views here.
import requests

def home(request):
    data_request = requests.get('https://s3.us-east-2.wasabisys.com/akshit/dataset-django/ft_assignment.json')
    data = data_request.json()
    # print(data)
    context = {
        'pakage':data[0]['package_id'],
        'app_name':data[0]['app_name'],
        'data_list':list(data[0]['date_wise_metrics']['daily_active_users'].keys()),
        'daily_active_users':list(data[0]['date_wise_metrics']['daily_active_users'].values()),
    }
    return render(request,'chart/home1.html',{'context':context})