import threading
# from background_task import background
import requests
from django.conf import settings
from .models import Link
from .utils import get_section
# from queue import Queue
import time
import random

TOKEN = settings.DISCORD_TOKEN
CHANNEL_ID = settings.CHANNEL_ID

BASE_URL = "https://discord.com/api"

headers = {
    "Authorization": f"Bot {TOKEN}"
}


def send_message(msg_text):
    url = BASE_URL + f"/channels/{CHANNEL_ID}/messages"

    message = {
        "content": msg_text
    }

    try:
        requests.post(url, headers=headers, data=message)
    except:
        pass


# q = Queue()

# thread_count = 0


# def my_processes(link):
#     global thread_count
#     try:
#         if link.linkdetail.lazy < 20:

#             # print("Currently Checking:", link.link)

#             section = get_section(link.link)
#             data = {}
#             data['section'] = section
#             data['link'] = link
#             q.put(data)
#             # if section != link.linkdetail.section:
#             #     msg = f"Change detected: {link.link}"
#             #     send_message(msg)
#             #     link.linkdetail.section = section
#             #     link.linkdetail.lazy = 0
#             #     link.linkdetail.save()

#             # else:
#             #     link.linkdetail.lazy = link.linkdetail.lazy + 1
#             #     link.linkdetail.save()
#     except:
#         pass
#     finally:
#         thread_count -= 1


# @background
def my_task():
    # global thread_count
    while True:
        links = Link.objects.all()

        print("Total links", len(links))

        for link in links:

            # if link.linkdetail.lazy < 10:

            print("Currently Checking:", link.link)

            section = get_section(link.link)

            if section != "" and section != link.linkdetail.section:
                msg = f"Change detected: {link.link}"
                link.linkdetail.section = section
                # link.linkdetail.lazy = 0
                link.linkdetail.save()
                print("change saved in database")
                send_message(msg)
                print("message sent")
            else:
                print("not changed")
                link.linkdetail.lazy = link.linkdetail.lazy + 1
                link.linkdetail.save()
        #     thread_count += 1
        #     x = threading.Thread(target=my_processes,
        #                          daemon=True, args=(link,))
        #     x.start()
        #     time.sleep(0.5)

        # while True:
        #     if thread_count == 0:
        #         break
        #     time.sleep(1)
        time.sleep(1)


# @background
# def queue_process():
#     print("started")
#     while True:
#         while not q.empty():
#             data = q.get()
#             section = data['section']
#             link = data['link']
#             # print("before query")
#             try:
#                 if section != link.linkdetail.section:
#                     msg = f"Change detected: {link.link}"
#                     link.linkdetail.section = section
#                     link.linkdetail.lazy = 0
#                     # print("after query")
#                     link.linkdetail.save()
#                     send_message(msg)
#                 else:
#                     link.linkdetail.lazy = link.linkdetail.lazy + 1
#                     link.linkdetail.save()
#             except Exception as e:
#                 print("Error", e)

#             # print("Hello")
#             # time.sleep(0.5)
#         else:
#             # print("while end")
#             pass

#         # print("Hello")
#         time.sleep(1)


# # @background
# def lazy_reset():
#     while True:
#         links = Link.objects.all()
#         for link in links:
#             link.linkdetail.lazy = 0
#             link.linkdetail.save()
#         time.sleep(600)

def visit_homepage():
    """this will prvent the app from sleeping after 30 minutes"""
    while True:
        
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        ]

        user_agent = random.choice(user_agents)

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
            "Accept-Encoding": "gzip, deflate", 
            "Accept-Language": "en-GB,en-US, de-DE;q=0.9,en;q=0.8", 
            "Dnt": "1",
            "Upgrade-Insecure-Requests": "1", 
            "User-Agent": user_agent
        }

        


        try:
            print("server restarted")
            requests.get('https://link-monitor.herokuapp.com/upload/', headers=headers)
        except:
            pass

        time.sleep(1500) # 25 minute

th = threading.Thread(target=my_task, daemon=True)
th.start()

th = threading.Thread(target=visit_homepage, daemon=True)
th.start()

# th = threading.Thread(target=queue_process, daemon=True)
# th.start()

# th = threading.Thread(target=lazy_reset, daemon=True)
# th.start()

if __name__ == "__main__":
    send_message("Change detected")
