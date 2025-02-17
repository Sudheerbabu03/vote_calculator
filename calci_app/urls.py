from django.urls import path # type: ignore
from calci_app.views import calci,display,vote
urlpatterns=[
    path('',calci,name='calci'),
    path('display/',display,name='display'),
    path('vote/',vote,name='vote')
]