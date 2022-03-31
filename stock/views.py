from django.http import HttpResponse
from django.shortcuts import render
import urllib.request
import pandas as pd


def index(request):
    return render(request, 'index.html')

def api():
    apiUrl = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"

    with urllib.request.urlopen(apiUrl) as response:
        html=response.read()
    str=html.decode('UTF-8')
    with open("test.csv", "w") as f:
        f.write(str)

def search(request):
    if request.method == "GET":

        param = request.GET.get("sym", "")
        return render(request, 'index.html', {'param': param})
