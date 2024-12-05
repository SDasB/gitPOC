import re
import requests
import concurrent.futures
from bs4 import BeautifulSoup


class XYZ:
    info_url = "https://alas.aws.amazon.com/"
    distro_regex = re.compile(r"A([0-9]{4})-([0-9]+)")
    name = "XYZ LINUX"

    def _get_ad(self) -> list[str]:
        raw_response = requests.get(self.info_url, timeout=30)
        body = BeautifulSoup(raw_response.text, "html.parser")
        trs = body.find("table", {"id": "ALAStable"}).find("tbody").find_all("tr")
        print(trs)
        return [tr.get("id") for tr in trs]

    def _get_pag(self, ad_id) -> list[str]:
        url = f"{self.info_url}{ad_id}.html"
        raw_response = requests.get(url, timeout=30)
        return raw_response.text


xyz_instance = XYZ()

# Call the _get_ad method
ad_ids = xyz_instance._get_ad()

# Call the _get_pag method with the obtained ad_ids
with concurrent.futures.ProcessPoolExecutor() as executor:
    result_pages = list(executor.map(xyz_instance._get_pag, ad_ids))

# Now, result_pages contains the list of pages retrieved by the _get_pag method
print(len(result_pages))
