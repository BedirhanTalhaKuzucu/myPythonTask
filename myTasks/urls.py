from django.urls import path
from .views import home, sortedId, sortedISO, renderDatabase, fetchData


urlpatterns = [
 path('', home, name="home"),
 path('sortID', sortedId, name="sortedId"),
 path('sortISO', sortedISO, name="sortedISO"),
 path('dataBase', renderDatabase, name="renderDatabase"),
 path('api', fetchData, name="fetchData"),

]
