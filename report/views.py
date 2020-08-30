from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
from . import utils
import requests

# Create your views here.
def getdata(request):
    url = 'https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json'
    response = requests.get(url)
    response = response.json()
    print(response)

    for x in response:
        y = x['year']
        p = x['petroleum_product']
        s = x['sale']
        d = Data(year=y, petroleum_product=p, sale=s)
        d.save()
    return HttpResponse('done')

def home(request):
    #taking the refined data from utils.py
    refined_data = utils.rdata
    context = {
        'data' : refined_data,
    }
    return render(request,'report/index.html',context)
    