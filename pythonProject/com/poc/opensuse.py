import re
from datetime import datetime

import httpx


class OpenSUSE:
    pattern = r'<a href="[^"]+">(cvrf-opensuse[^<]+)</a>\s+(\d{2}-\w{3}-\d{4})'

    def get_vulnerability_information(self):
        self._get_all_advisories()

    def _get_all_advisories(self):
        response = httpx.get("https://ftp.suse.com/pub/projects/security/cvrf1.2/")
        response.raise_for_status()
        lines = response.text.splitlines()

        #print(lines)
        for line in lines:
            self.find_text_and_time(line)

    def find_text_and_time(self, text):
        # Find matches
        matches = re.findall(self.pattern, text)

        # Output the results
        for match in matches:
            inner_html, date = match
            print(f"InnerHTML: {inner_html}, Date: {date}")


if __name__ == "__main__":
    OpenSUSE().get_vulnerability_information()

    # print(lines[5])
    # CVRF_FILES = r"cvrf-(opensuse-su-\d+:\d+-\d).xml"
    # date_pattern = r"\d{2}-[A-Za-z]{3}-\d{4}"
    # 25089
    # for line in lines:
    #    match = re.match(CVRF_FILES, line)
    #    if match:
    #        cvrf_file = match(0)
    #        match_date = re.search(date_pattern, line)
    #        date = match_date(0)
    #        date_obj = datetime.strptime(date, "%d-%b-%Y")

    # print(lines)
