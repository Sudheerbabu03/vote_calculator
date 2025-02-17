from django.urls import path # type: ignore
from vote_app.views import vote,vote_check,calci

urlpatterns=[
    path('',vote,name='vote'),
    path('vote_check/',vote_check,name='vote_check'),
    path('calci/',calci,name='calci')
]