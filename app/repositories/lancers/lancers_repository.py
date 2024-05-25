import requests
import aiohttp
import asyncio
from bs4 import BeautifulSoup

class LancersRepository:
    async def fetch_lancers(self):
        url = 'https://www.lancers.jp/work/search?open=1&ref=header_menu&work_rank%5B0%5D=2&work_rank%5B1%5D=3&work_rank%5B2%5D=0&show_description=1&page='
        page = 1
        all_link = []
        all_titles = []
        
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.get(url + str(page)) as response:
                    text = await response.text()
                    soup = BeautifulSoup(text, 'html.parser')
                    
                    links = soup.find_all('a', class_='p-search-job__latest-media-title c-media__title')
                    
                    # 各リンクのテキストを取得
                    for link in links:
                        title = link.get_text(strip=True)
                        all_titles.append(title)
                    
                    next_page_link = soup.find('div', class_='c-pager__sub')
                    if not next_page_link:
                        break
                    
                    page += 1
                    print(page)

        print(all_titles)
