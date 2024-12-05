import logging
import re
import time

import requests
from bs4 import BeautifulSoup
from collections import defaultdict

logger = logging.getLogger(__name__)


class Amazon:
    products = {
        "Amazon Linux": ("https://alas.aws.amazon.com/", "https://alas.aws.amazon.com/"),
        "Amazon Linux 2": ("https://alas.aws.amazon.com/alas2.html", "https://alas.aws.amazon.com/AL2/"),
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

        for product, urls in self.products.items():
            info_url = urls[0]
            print("URL is " + info_url)
            # print("Advisory URL is "+advisory_url)
            raw_response = requests.get(info_url, timeout=60)
            body = BeautifulSoup(raw_response.text, "html.parser")
            trs = body.find("table", {"id": "ALAStable"}).find("tbody").find_all("tr")

            # filtered_ad_ids = []
            for tr in trs:
                ad_id = tr.get("id")
                if self.advisory_distro_info_regex.match(ad_id):
                    advisory_ids[product].append(ad_id)

        print(len(advisory_ids))
        total = 0
        for product in advisory_ids:
            url, advisory_url = self.products[product]
            print(url)
            print(type(advisory_ids[product]))
            total = total + len(advisory_ids[product])
        print(total)
        return advisory_ids

    def _get_advisory_pages(self) -> list[tuple[str, str, str]]:
        advisory_pages = []
        advisory_ids = self._get_advisory_ids()
        for product, advisory_id_list in advisory_ids.items():
            print(product)
            print(advisory_ids[product])
        for product, advisory_id_list in advisory_ids.items():
            x = 0
            for advisory_id in advisory_id_list:
                x = x + 1
                advisory_url = self.products[product][1]
                url = f"{advisory_url}{advisory_id}.html"
        return advisory_pages

    def print_advisory_pages(self):
        start_time = time.time()
        advisory_pages = self._get_advisory_pages()

        for advisory_page, advisory_xref, advisory_product_name in advisory_pages:
            # print("advisory_page :" + advisory_page)
            # print("advisory_xref :" + advisory_xref)
            # print("advisory_product_name :" + advisory_product_name)
            advisory_content = self._parse_advisory_content(advisory_page)
            print("THE CONTENT OF THE ADVISORY ")
            print(advisory_content)
            advisory_id = self._parse_advisory_id(advisory_content)
            print("THE ADVISORY ID " + advisory_id)
        x = 0
        for pages in advisory_pages:
            x = x + 1
            print(
                "------------------------------------------------------------------------------------------------------------")
            print(type(pages[0]))
            x1 = pages[0]
            x2 = pages[1]
            print(pages[0])
            print(type(pages[1]))
            print(pages[1])
            if x == 3:
                break
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
        x = 0
        for pages, xref, product in advisory_pages:
            x = x + 1
            print(
                "*********************************************************************************************************************")
            print(type(pages))
            y1 = pages
            y2 = xref
            print(pages)
            print(type(xref))
            print(xref)
            print(product)
            if x == 3:
                break
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)

        print(x1 == y1)
        print(x2 == y2)
        # for i, page_content in enumerate(advisory_pages, start=1):
        #   print(f"Page {i} Content:")
        #  print(page_content)
        # print("-" * 50)

    def _parse_advisory_content(self, advisory_html_page: str) -> BeautifulSoup:
        return BeautifulSoup(advisory_html_page, "html.parser")

    def _parse_advisory_id(self, advisory_content: BeautifulSoup) -> str:
        line = advisory_content.find('span', class_='alas-info').get_text(strip=True).split(':')[-1]

        print("THE LINE -------------------------------------------------------------------")
        print(line)
        print(advisory_content.title.text)
        return advisory_content.title.text
        # return self.advisory_distro_info_regex.search(line).group(0)

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
