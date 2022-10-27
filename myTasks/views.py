import json
from django.shortcuts import render
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
    logger.info(countryData) 
    sortedId = sorted(countryData['infoList'], key=lambda x: x['ID'])
    sortedISO = sorted(countryData['infoList'], key=lambda x: x['ISOCode'])
    
    
    context = {
        'data': countryData,
        "sortedId" :sortedId,
        "sortedISO" : sortedISO, 
    }
    return render(request, "myTasks/home.html", context)