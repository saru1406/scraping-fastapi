from sqlalchemy.orm import Session
import requests

class CrowdWorksRepository:
    def fetch_crowdworks(self):
        response = requests.get('https://crowdworks.jp/public/jobs/search?hide_expired=true')
        return response.status_code
