# from links.tasks import *
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name="upload"),
]


# background tasks
# my_task(repeat=180)
# queue_process(schedule=1)

# # reset all lazy after 10 minute
# lazy_reset(repeat=600, repeat_until=None)
