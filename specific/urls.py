from specific.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('third/',third,name='third'),
    path('fourth/',fourth,name='fourth'),
]