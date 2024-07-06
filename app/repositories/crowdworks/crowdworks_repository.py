import requests
from bs4 import BeautifulSoup


class CrowdWorksRepository:
    async def fetch_crowdworks(self):
        base_url = "https://crowdworks.jp/public/jobs/search?hide_expired=true&page="
        page = 1
        all_jobs = []

        while True:
            response = requests.get(base_url + str(page))
            soup = BeautifulSoup(response.text, "html.parser")
            print(soup)

            jobs = soup.find_all("div", class_="RtPEC")
            all_jobs.extend(jobs)

            next_page_link = soup.find("a", class_="pc5kI jD9FX")
            if not next_page_link:
                break

            page += 1

        return all_jobs
