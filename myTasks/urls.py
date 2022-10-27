from django.urls import path
from .views import home, sortedId, sortedISO


urlpatterns = [
 path('', home, name="home"),
 path('sortID', sortedId, name="sortedId"),
 path('sortISO', sortedISO, name="sortedISO"),

]
