from fastapi import FastAPI

from app.routers.users_router.fetch_user_router import router as fetch_user_router
from app.routers.users_router.store_user_router import router as store_user_router
from app.routers.users_router.find_user_router import router as find_user_router
from app.routers.scraping_router.store_scraping import router as store_scraping

app = FastAPI()

# users
app.include_router(fetch_user_router)
app.include_router(store_user_router)
app.include_router(find_user_router)

# scraping
app.include_router(store_scraping)
