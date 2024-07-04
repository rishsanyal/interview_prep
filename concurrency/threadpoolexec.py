import time
import requests
import concurrent.futures
# from multiprocessing import Event
from threading import Event

def get_web_page(web_url, events):

    print("\nGetting started", end="\n", flush=True)
    events.wait()
    print("\nwe started", end="\n", flush=True)


    response = requests.get(web_url, timeout=10)

    if response.status_code == 200:
        return web_url + " True"
    else:
        return web_url + " False"


if __name__ == '__main__':
    wiki_page_urls = [
        "https://en.wikipedia.org/wiki/Ocean",
        "https://en.wikipedia.org/wiki/Island",
        "https://en.wikipedia.org/wiki/this_page_does_not_exist",
        "https://en.wikipedia.org/wiki/Shark",
    ]


    event_lock = Event()
    with concurrent.futures.ThreadPoolExecutor() as manager:
        futures = []

        for url in wiki_page_urls:
            futures.append(
                manager.submit(get_web_page, url, event_lock)
            )

        time.sleep(2)
        event_lock.set()

        for future in concurrent.futures.as_completed(futures):
            try:
                print(future.result())
            except Exception as e:
                print(e)