from django.shortcuts import render
import json
import logging
logger = logging.getLogger("django")
def home(request):
    
    context = {
        'data': [
            {"name" : "Afghanistan",  "ID":93, "ISOCode" : "AF" },
            {"name" : "Germany",  "ID":49, "ISOCode" : "DE" },
            {"name" : "Ghana",  "ID":233, "ISOCode" : "GH" },
            {"name" : "Greenland",  "ID":299, "ISOCode" : "GL" },
            {"name" : "France",  "ID":33, "ISOCode" : "FR" },
        ]
    }
    logger.info(context) 
    return render(request, "myTasks/home.html", context)