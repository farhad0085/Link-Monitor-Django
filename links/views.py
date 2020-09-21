from django.shortcuts import render
from .models import Link


def upload(request):
    if request.method == "POST":
        file = request.FILES['file']
        for link in file.readlines():
            Link.objects.create(link=link.decode("utf-8"))

        context = {
            "message": "Upload complete"
        }
        return render(request, "links/upload.html", context)

    return render(request, "links/upload.html")
