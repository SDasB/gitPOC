import logging
import re
import time

import requests
from bs4 import BeautifulSoup
from collections import defaultdict

logger = logging.getLogger(__name__)


class Amazon:
    base_url = "https://alas.aws.amazon.com/"
    info_urls = ["https://alas.aws.amazon.com/", "https://alas.aws.amazon.com/alas2.html"]
    url_map_dictionary = {
        "https://alas.aws.amazon.com/": "https://alas.aws.amazon.com/",
        "https://alas.aws.amazon.com/alas2.html": "https://alas.aws.amazon.com/AL2/",
    }

    advisory_distro_info_regex = re.compile(r"ALAS-([0-9]{4})-([0-9]+)")

    product_name = "Amazon_Linux"

    def _get_advisory_ids(self) -> dict[str, list[str]]:
        # advisory_ids = {}
        # for url in self.url_map_dictionary:
        #     print(url)
        #     raw_response = requests.get(url, timeout=60)
        #     body = BeautifulSoup(raw_response.text, "html.parser")
        #     trs = body.find("table", {"id": "ALAStable"}).find("tbody").find_all("tr")
        #     # advisory_ids[url]=tuple(tr.get("id") for tr in trs)
        #
        #     # filtered_ad_ids = tuple(filter(lambda ad_id: self.advisory_distro_info_regex.match(ad_id), (tr.get("id") for tr in trs)))
        #     filtered_ad_ids = tuple(
        #         ad_id for ad_id in (tr.get("id") for tr in trs) if self.advisory_distro_info_regex.match(ad_id))
        #
        #     advisory_ids[url] = filtered_ad_ids

        advisory_ids = defaultdict(list)

        for url in self.url_map_dictionary:
            print(url)
            raw_response = requests.get(url, timeout=60)
            body = BeautifulSoup(raw_response.text, "html.parser")
            trs = body.find("table", {"id": "ALAStable"}).find("tbody").find_all("tr")

            # filtered_ad_ids = []
            for tr in trs:
                ad_id = tr.get("id")
                if self.advisory_distro_info_regex.match(ad_id):
                    advisory_ids[url].append(ad_id)

        print(len(advisory_ids))
        total = 0
        for url in advisory_ids.keys():
            print(url)
            print(type(advisory_ids[url]))
            total = total + len(advisory_ids[url])
        print(total)
        return advisory_ids

    def _get_advisory_pages(self) -> list[tuple[str, str]]:
        advisory_pages = []
        advisory_ids = self._get_advisory_ids()
        for url in advisory_ids.keys():
            print(url)
            print(advisory_ids[url])
        for info_url, advisory_id_list in advisory_ids.items():
            x = 0
            for advisory_id in advisory_id_list:
                x = x + 1
                url = f"{self.url_map_dictionary[info_url]}{advisory_id}.html"
                print(url)
                raw_response = requests.get(url, timeout=60)
                advisory_details = (raw_response.text, url)
                advisory_pages.append(advisory_details)
                print(advisory_details)
                if (x == 5):
                    break
        return advisory_pages

    def print_advisory_pages(self):
        start_time = time.time()
        advisory_pages = self._get_advisory_pages()
        x=0
        for pages in advisory_pages:
            x=x+1
            print("------------------------------------------------------------------------------------------------------------")
            print(type(pages[0]))
            x1=pages[0]
            x2=pages[1]
            print(pages[0])
            print(type(pages[1]))
            print(pages[1])
            if x==3:
                break
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
        x=0
        for pages,xref in advisory_pages:
            x=x+1
            print("*********************************************************************************************************************")
            print(type(pages))
            y1=pages
            y2=xref
            print(pages)
            print(type(xref))
            print(xref)
            if x==3:
                break
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)

        print(x1==y1)
        print(x2==y2)
        # for i, page_content in enumerate(advisory_pages, start=1):
        #   print(f"Page {i} Content:")
        #  print(page_content)
        # print("-" * 50)


# Create an instance of the Amazon class
amazon_instance = Amazon()

# Call the print_advisory_pages method

amazon_instance.print_advisory_pages()
##Execution with threadpool executor
# def _get_advisory_ids(self) -> dict[str, tuple[str]]:
#     advisory_ids = {}
#
#     with ThreadPoolExecutor(max_workers=5) as executor:  # Adjust max_workers based on your requirements
#         future_to_url = {executor.submit(self._fetch_data, url): url for url in self.url_map_dictionary}
#
#         for future in concurrent.futures.as_completed(future_to_url):
#             url = future_to_url[future]
#             try:
#                 data = future.result()
#                 advisory_ids[url] = data
#             except Exception as e:
#                 print(f"Error fetching data for {url}: {e}")
#
#     return advisory_ids
#
# def _fetch_data(self, url):
#     raw_response = requests.get(url, timeout=60)
#     raw_response.raise_for_status()
#     body = BeautifulSoup(raw_response.text, "html.parser")
#     trs = body.find("table", {"id": "ALAStable"}).find("tbody").find_all("tr")
#
#     filtered_ad_ids = [tr.get("id") for tr in trs if self.advisory_distro_info_regex.match(tr.get("id"))]
#     return tuple(filtered_ad_ids)