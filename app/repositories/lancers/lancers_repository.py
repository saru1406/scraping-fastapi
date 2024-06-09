import aiohttp
from bs4 import BeautifulSoup

class LancersRepository:
    
    def __init__(self):
        self.base_url = 'https://www.lancers.jp'

    async def fetch_lancers(self):
        url = self.base_url + '/work/search?open=1&ref=header_menu&work_rank%5B0%5D=2&work_rank%5B1%5D=3&work_rank%5B2%5D=0&show_description=1&page='
        page = 1
        all_link = []
        all_title = []
        all_tags = []
        all_show = []
        all_price = []
        # all_type = []
        all_limit = []
        
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.get(url + str(page)) as response:
                    text = await response.text()
                    soup = BeautifulSoup(text, 'html.parser')
                    
                    jobs = soup.find_all('div', class_='p-search-job-media c-media c-media--item')                    
                    for job in jobs:
                        
                        # タイトル、リンク取得
                        job_link = job.find('a', class_='p-search-job-media__title c-media__title')
                        if job_link:
                            link = job_link.get('href')
                            all_link.append(self.base_url + link)
                            
                            all_title.append(job_link.get_text(strip=True))
                            
                        # 詳細取得
                        job_shows = job.find_all('div', class_='c-media__description')
                        if job_shows:
                            for job_show in job_shows:
                                job_show_ui = job_show.find('ul')
                                if job_show_ui:
                                    all_show.append(None)
                                else:
                                    all_show.append(job_show.get_text(strip=True))
                                
                        # 価格取得
                        job_prices = job.find('div', class_='c-media__job-stats-item')
                        if job_prices:
                            job_price = job_prices.get_text(strip=True)
                            all_price.append(job_price)
                        else:
                            all_price.append(None)
                            
                        # 応募数取得
                        job_limits = job.find('div', class_='p-search-job-media__job-status')
                        if job_limits:
                            job_limit = job_limits.find('div', class_='c-media__job-stats-item')
                            if job_limit:
                                all_limit.append(job_limit.get_text(strip=True))
                            else:
                                all_limit.append(None)
                        else:
                            all_limit.append(None)
                                
                        # タグ取得
                        job_tags = job.find('ul', class_='p-search-job__divisions')
                        if job_tags:
                            all_tags.append(job_tags.get_text(strip=True))
                        else:
                            all_tags.append(None)
                    
                    next_page_link = soup.find('div', class_='c-pager__sub')
                    if not next_page_link:
                        break
                    
                    page += 1

            return {'titles': all_title, 'links': all_link, 'tags': all_tags, 'prices': all_price, 'show': all_show, 'limits': all_limit}
