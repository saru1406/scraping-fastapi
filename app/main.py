from app.middleware import app
from app.routers.job_router import fetch_job, store_job
from app.routers.prompt_router import create_prompt, fetch_prompt
from app.routers.users_router import (fetch_user_router, find_user_router,
                                      store_user_router)

# users
app.include_router(fetch_user_router.router)
app.include_router(store_user_router.router)
app.include_router(find_user_router.router)

# job
app.include_router(store_job.router)
app.include_router(fetch_job.router)

# prompt
app.include_router(create_prompt.router)
app.include_router(fetch_prompt.router)
