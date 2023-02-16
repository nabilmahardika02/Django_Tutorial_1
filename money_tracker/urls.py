from money_tracker.views import show_tracker
from django.urls import path, include

app_name = 'money_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
]
