import logging
import re
from concurrent.futures import ThreadPoolExecutor
import time

from bs4 import BeautifulSoup
import requests
from typing import List, Tuple

logger = logging.getLogger(__name__)

class Amazon2:

    base_url = "https://alas.aws.amazon.com/"
    info_urls = ("https://alas.aws.amazon.com/", "https://alas.aws.amazon.com/alas2.html")

    advisory_distro_info_regex = re.compile(r"ALAS-([0-9]{4})-([0-9]+)")

    product_name = "Amazon_Linux"

    def _get_advisory_ids(self) -> list[tuple[str, str]]:
        advisory_ids = []
        for url in self.info_urls:
            try:
                baseUrl=()
                raw_response = requests.get(url, timeout=60)
                body = BeautifulSoup(raw_response.text, "html.parser")
                trs = body.find("table", {"id": "ALAStable"}).find("tbody").find_all("tr")
                advisory_ids.extend([(tr.get("id"), tr.a.get("href")) for tr in trs if tr.a])
            except requests.RequestException as e:
                logger.debug("Could not find the advisory ids. Skipping", url, e)
        print(len(advisory_ids))
        return advisory_ids

    def _get_advisory_pages(self) -> List[str]:
        advisory_ids = self._get_advisory_ids()
        with ThreadPoolExecutor() as executor:
            advisory_pages = list(executor.map(self._get_advisory_page, advisory_ids))

        return advisory_pages

    def _get_advisory_page(self, advisory_id: Tuple[str, str]) -> str:
        url = f"{self.base_url}{advisory_id[1]}"

        try:
            raw_response = requests.get(url, timeout=60)
            return raw_response.text
        except requests.RequestException as e:
            logger.debug("Could not fetch advisory page. Skipping", url, e)
            return ""

    def print_advisory_pages(self):
        start_time = time.time()
        advisory_pages = self._get_advisory_pages()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
        #for i, page_content in enumerate(advisory_pages, start=1):
         #   print(f"Page {i} Content:")
          #  print(page_content)
           # print("-" * 50)

# Create an instance of the Amazon class

amazon_instance = Amazon2()

# Call the print_advisory_pages method
amazon_instance.print_advisory_pages()
