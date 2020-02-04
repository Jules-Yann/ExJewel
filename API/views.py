from django.shortcuts import render
from django.http import HttpResponse
import requests
from API.models import Response


"""
Create JSON object.
"""

def createJSON(request):
    body_value = ""

    if request.GET.get('shape') != None:
        body_value += "\"shape\":\"" + request.GET.get('shape') + "\""

    if (request.GET.get('size')) != None:
        if (body_value == ""):
            body_value += "\"size\":\"" + request.GET.get('size') + "\""
        else:
            body_value += ",\"size\":\"" + request.GET.get('size') + "\""

    if (request.GET.get('color')) != None:
        if (body_value == ""):
            body_value += "\"color\":\"" + request.GET.get('color') + "\""
        else:
            body_value += ",\"color\":\"" + request.GET.get('color') + "\""

    if (request.GET.get('clarity')) != None:
        if (body_value == ""):
            body_value += "\"clarity\":\"" + request.GET.get('clarity') + "\""
        else:
            body_value += ",\"clarity\":\"" + request.GET.get('clarity') + "\""

    data = "{\"request\": " \
           "{\"header\": {" \
           "\"username\": \"rjxv5uua06jrvssd8axhpgfw9aqb66\", " \
           "\"password\": \"CvdDAMzJ\"}, " \
           "\"body\": {" + body_value + "}}}"

    return data



"""
Send a request to an URL, take the request in parameters.
"""

def send_request(request, URL):
    json = createJSON(request)

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    resp = requests.request("GET", URL, data=json, headers=headers)

    return resp



"""
To get a special item from Rapaport
"""

def get_item(request):
    url = "https://technet.rapaport.com/HTTP/JSON/Prices/GetPrice.aspx"

    return HttpResponse(send_request(request, url))



"""
To get all items from Rapaport, take request in parameters to by shape
"""

def get_all_item(request):
    url = "https://technet.rapaport.com/HTTP/JSON/Prices/GetPriceSheet.aspx"

    return HttpResponse(send_request(request, url))



"""
To store an item in the Data base
"""

def store_one(request):
    url = "https://technet.rapaport.com/HTTP/JSON/Prices/GetPrice.aspx"

    json = send_request(request, url)

    Response.objects.create(shape=json.json()['response']['body']['shape'],
                            low_size=json.json()['response']['body']['low_size'],
                            high_size=json.json()['response']['body']['high_size'],
                            color=json.json()['response']['body']['color'],
                            clarity=json.json()['response']['body']['clarity'],
                            caratPrice=json.json()['response']['body']['caratprice'],
                            date=json.json()['response']['body']['date'])
    return (HttpResponse('Done'))



""""
To store all items from Rapaport
"""

def store_all(request):
    url = "https://technet.rapaport.com/HTTP/JSON/Prices/GetPriceSheet.aspx"

    json = send_request(request, url)

    for val in json.json()['response']['body']['price']:
        Response.objects.create(shape=val['shape'],
                                low_size=val['low_size'],
                                high_size=val['high_size'],
                                color=val['color'],
                                clarity=val['clarity'],
                                caratPrice=val['caratprice'],
                                date=val['date'])

    return (HttpResponse('Done'))


# def show_data(request):
#     for row in Response:
#        print("Shape = ", row[1])
#        print("Low_size  = ", row[2])
#        print("High_size  = ", row[3])
#        print("Color  = ", row[4])
#        print("Clarity = ", row[5])
#        print("caratPrice = ", row[6])
#        print("Date = ", row[7])



"""
To delete all items in the Data base
"""

def delete(self):
    Response.objects.all().delete()

    return HttpResponse('Done')



def search(request):
    data = Response.objects.all()

    if (request.GET.get('id')) != None:
        data = data.filter(id=request.GET.get('id'))

    if (request.GET.get('shape')) != None:
        data = data.filter(shape=request.GET.get('shape'))

    if (request.GET.get('low_size')) != None:
        data = data.filter(low_size=request.GET.get('low_size'))

    if (request.GET.get('high_size')) != None:
        data = data.filter(high_size=request.GET.get('high_size'))

    if (request.GET.get('color')) != None:
        data = data.filter(color=request.GET.get('color'))

    if (request.GET.get('clarity')) != None:
        data = data.filter(clarity=request.GET.get('clarity'))

    if (request.GET.get('caratPrice')) != None:
        data = data.filter(caratPrice=request.GET.get('caratPrice'))

    if (request.GET.get('date')) != None:
        data = data.filter(date=request.GET.get('date'))

    return HttpResponse(data)
