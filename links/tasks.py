import threading
from background_task import background
import requests
from django.conf import settings
from .models import Link
from .utils import get_section
from queue import Queue

TOKEN = settings.DISCORD_TOKEN
CHANNEL_ID = settings.CHANNEL_ID

BASE_URL = "https://discord.com/api"

headers = {
    "Authorization": f"Bot {TOKEN}"
}

q = Queue()


def send_message(msg_text):
    url = BASE_URL + f"/channels/{CHANNEL_ID}/messages"

    message = {
        "content": msg_text
    }

    try:
        requests.post(url, headers=headers, data=message)
    except:
        pass


def my_processes(link):
    if link.linkdetail.lazy < 10:

        print("Currently Checking:", link.link)

        section = get_section(link.link)

        if section != link.linkdetail.section:
            msg = f"Change detected: {link.link}"
            send_message(msg)
            link.linkdetail.section = section
            link.linkdetail.lazy = 0
            link.linkdetail.save()

        else:
            link.linkdetail.lazy = link.linkdetail.lazy + 1
            link.linkdetail.save()


@background
def my_task():
    links = Link.objects.all()

    print("Total links", len(links))

    for link in links:

        # if link.linkdetail.lazy < 10:

        #     print("Currently Checking:", link.link)

        #     section = get_section(link.link)

        #     if section != link.linkdetail.section:
        #         msg = f"Change detected: {link.link}"
        #         link.linkdetail.section = section
        #         link.linkdetail.save()
        #         send_message(msg)
        #     else:
        #         link.linkdetail.lazy = link.linkdetail.lazy + 1
        #         link.linkdetail.save()
        x = threading.Thread(target=my_processes, args=(link,))
        x.start()


@background
def lazy_reset():
    links = Link.objects.all()
    for link in links:
        link.linkdetail.lazy = 0
        link.linkdetail.save()


if __name__ == "__main__":
    send_message("Change detected")
