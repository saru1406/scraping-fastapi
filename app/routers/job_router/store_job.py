import asyncio

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.job.job_repository import JobRepository
from app.usecase.crawler.crowdworks_usecase import StoreCrowdWorksUsecase
from app.usecase.crawler.itpro_partners_usecase import \
    StoreItproPartnersUsecase
from app.usecase.crawler.lancers_usecase import StoreLnacersUsecase

router = APIRouter()


@router.get("/scraping", tags=["案件スクレイピング"])
async def store_job(
    db: Session = Depends(get_db),
    store_crowdworks_usecase: StoreCrowdWorksUsecase = Depends(StoreCrowdWorksUsecase),
    store_lancers_usecase: StoreLnacersUsecase = Depends(StoreLnacersUsecase),
    store_itpro_partners: StoreItproPartnersUsecase = Depends(
        StoreItproPartnersUsecase
    ),
    job_repository: JobRepository = Depends(JobRepository),
):
    job_repository.delete(db=db)
    await asyncio.gather(
        store_lancers_usecase.execute(db=db),
        store_itpro_partners.execute(db=db),
        # store_crowdworks_usecase.execute(db)
    )
    db.commit()
    return "更新完了"
