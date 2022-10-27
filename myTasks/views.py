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
    # json_data = open('data.json')
    # data = json.load(json_data)
    
    context = {
        'data': countryData
    }
    logger.info(countryData) 
    return render(request, "myTasks/home.html", context)