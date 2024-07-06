from.setting import app

from app.routers.users_router.fetch_user_router import router as fetch_user_router
from app.routers.users_router.store_user_router import router as store_user_router
from app.routers.users_router.find_user_router import router as find_user_router
from app.routers.job_router.store_job import router as store_job
from app.routers.job_router.fetch_job import router as fetch_job
from app.routers.prompt_router.prompt_router import router as prompt

#users
app.include_router(fetch_user_router)
app.include_router(store_user_router)
app.include_router(find_user_router)

#job
app.include_router(store_job)
app.include_router(fetch_job)

# prompt
app.include_router(prompt)