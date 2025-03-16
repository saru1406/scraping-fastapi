import aiohttp
from bs4 import BeautifulSoup


class ItproPartnersRepository:

    async def fetch_itpro_partners(self):
        url = "https://itpropartners.com/job?page="
        page = 1
        all_link = []
        all_title = []
        all_tags = []
        all_show = []
        all_price = []
        all_limit = []

        async with aiohttp.ClientSession() as session:
            while True:
                async with session.get(url + str(page)) as response:
                    text = await response.text()
                    soup = BeautifulSoup(text, "html.parser")
                    jobs = soup.find_all("div", class_="c-job-card pc-show")
                    for job in jobs:
                        title = job.find("h2", class_="c-job-card__title")
                        all_title.append(title.get_text(strip=True))

                        link = job.find("a")
                        all_link.append(link.get("href"))

                        table = job.find("table", class_="c-job-table")
                        if table:
                            # show = table.find('td', class_='c-job-table__text')
                            all_show.append(table.get_text(strip=True))
                        else:
                            all_show.append(None)

                        price = job.find("div", class_="c-job-price")
                        if price:
                            all_price.append(price.get_text(strip=True))
                        else:
                            all_price.append(None)

                        tag = job.find("div", class_="c-job-card__info-icon")
                        if tag:
                            all_tags.append(tag.get_text(strip=True))
                        else:
                            all_tags.append(None)

                    pagenate = soup.find("ul", class_="c-job-pagenation")
                    if pagenate:
                        next_page_link = pagenate.find(
                            "li",
                            class_="c-job-pagenation__item c-job-pagenation__item--string",
                        )
                        if not next_page_link:
                            break
                    else:
                        break

                page += 1

        return {
            "titles": all_title,
            "links": all_link,
            "tags": all_tags,
            "prices": all_price,
            "show": all_show,
        }
