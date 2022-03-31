from django.http import HttpResponse
from django.shortcuts import render
import urllib.request
import pandas as pd
from .models import Stocks

# Create your views here.
def api(text):
    apiUrl = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"

    with urllib.request.urlopen(apiUrl) as response:
        html=response.read()
    str=html.decode('UTF-8')
    with open("test.csv", "w") as f:
        f.write(str)

    apiUrl = "https://archives.nseindia.com/products/content/sec_bhavdata_full_30032022.csv"

    with urllib.request.urlopen(apiUrl) as response:
        html=response.read()
    str=html.decode('UTF-8')
    with open("test1.csv", "w") as f:
        f.write(str)
        
    import pandas as pd
    
    data1 = pd.read_csv('test.csv')
    data2 = pd.read_csv('test1.csv')
    
    output1 = pd.merge(data1, data2, 
                    on='SYMBOL', 
                    how='inner')

    output1[' DELIV_PER'] = output1[' DELIV_PER'].replace(" -", 0)
    output1[' DELIV_QTY'] = output1[' DELIV_QTY'].replace(" -", 0)
    output1[' LAST_PRICE'] = output1[' LAST_PRICE'].replace(" ", 0)

    #for i in range(len(output1.SYMBOL)):
        #stock=Stocks(Stock_sym= output1.SYMBOL[i], Stock_name =output1['NAME OF COMPANY'][i], Paid_u = output1[' PAID UP VALUE'][i], Isin_n = output1[' ISIN NUMBER'][i], Face_v = output1[' FACE VALUE'][i], Open_v = output1[' OPEN_PRICE'][i], Close_v = output1[' CLOSE_PRICE'][i], High_v = output1[' HIGH_PRICE'][i], Last_v = output1[' LAST_PRICE'][i], Low_v = output1[' LOW_PRICE'][i], Prev_v =output1[' PREV_CLOSE'][i], Total_w = output1[' TURNOVER_LACS'][i], Total_rd = output1[' TTL_TRD_QNTY'][i], Total_t = output1[' NO_OF_TRADES'][i], AVG_PRICE = output1[' AVG_PRICE'][i], DELIV_QTY =output1[' DELIV_QTY'][i], DELIV_PER =output1[' DELIV_PER'][i] )
        #stock.save()
    try:
        id=output1['SYMBOL'][output1['SYMBOL']==text].index[0]
    except:
        id=-1
    return id, output1
    

def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method == 'GET':
        param = request.GET.get("sym", "")
        id,output=api(param)
        if id==-1:
            return render(request, 'index.html', {'error': 'nothing is found for given "'+ param+'"'})
        param={"sym": output['SYMBOL'][id], "com": output['NAME OF COMPANY'][id],"Paid" : output[' PAID UP VALUE'][id], "Isin" : output[' ISIN NUMBER'][id], "Face" : output[' FACE VALUE'][id], "Open" : output[' OPEN_PRICE'][id], "Close" : output[' CLOSE_PRICE'][id], "High" :output[' HIGH_PRICE'][id], "Last" : output[' LAST_PRICE'][id], "Low" : output[' LOW_PRICE'][id], "Previous" : output[' PREV_CLOSE'][id], "Turnover" : output[' TURNOVER_LACS'][id], "Trades" : output[' NO_OF_TRADES'][id], "AvgPrice" : output[' AVG_PRICE'][id], "DELIVQ" : output[' DELIV_QTY'][id], "DELIVP" : output[' DELIV_PER'][id] }
        return render(request, 'index.html', {'param': param})
