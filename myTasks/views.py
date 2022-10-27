import json
from django.shortcuts import render
from .models import Country
import requests
import logging
logger = logging.getLogger("django")


countryData = {
    'infoList': [
            {"name" : "Afghanistan",  "ID":93, "ISOCode" : "AF" },
            {"name" : "Germany",  "ID":49, "ISOCode" : "DE" },
            {"name" : "Ghana",  "ID":233, "ISOCode" : "GH" },
            {"name" : "Greenland",  "ID":299, "ISOCode" : "GL" },
            {"name" : "France",  "ID":33, "ISOCode" : "FR" },
        ]
}

def home(request):
    # logger.info(countryData) 
    sortedId = sorted(countryData['infoList'], key=lambda x: x['ID'])
    sortedISO = sorted(countryData['infoList'], key=lambda x: x['ISOCode'])

    countries = Country.objects.all()
    logger.info(countries) 
    
    context = {
        'data': countryData,
        "sortedId" :sortedId,
        "sortedISO" : sortedISO, 
    }
    return render(request, "myTasks/home.html", context)

def sortedId(request):
    sortedId = sorted(countryData['infoList'], key=lambda x: x['ID'])
    
    context = {
        "sortedId" :sortedId,
    }
    return render(request, "myTasks/sortedId.html", context)

def sortedISO(request):
    sortedISO = sorted(countryData['infoList'], key=lambda x: x['ISOCode'])
    
    context = {
        "sortedISO" :sortedISO,
    }
    return render(request, "myTasks/sortedISO.html", context)


def renderDatabase(request):
    # logger.info(countryData) 
    # sortedId = sorted(countryData['infoList'], key=lambda x: x['ID'])
    # sortedISO = sorted(countryData['infoList'], key=lambda x: x['ISOCode'])

    countries = Country.objects.all()
    logger.info(countries) 
    
    context = {
        'countries': countries, 
    }
    return render(request, "myTasks/renderedDataBase.html", context)

def fetchData(request):
    url = "https://restcountries.com/v3.1/all"
    dataList = []

    response = requests.request("GET", url)
    if response.ok:
        content = response.json()
        for i in range(5):
            data = {
                "name":content[i]["name"]["official"],
                "ISO": content[i]["cca2"],
                "id" : content[i]["idd"]["suffixes"][0],
            }
            dataList.append(data)
    
    print(dataList)

    context = {
        "dataList" :dataList,
    }
    return render(request, "myTasks/fetchData.html", context)