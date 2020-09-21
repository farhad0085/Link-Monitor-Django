from links.tasks import my_task, lazy_reset
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
]

# background tasks
my_task(repeat=30, repeat_until=None)

# reset all lazy after 10 minute
lazy_reset(repeat=600, repeat_until=None)
