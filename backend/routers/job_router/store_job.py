import asyncio

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.repositories.job.job_repository import JobRepository
from backend.usecase.crawler.crowdworks_usecase import StoreCrowdWorksUsecase
from backend.usecase.crawler.itpro_partners_usecase import \
    StoreItproPartnersUsecase
from backend.usecase.crawler.lancers_usecase import StoreLnacersUsecase
from backend.usecase.qdrant.qdrant_usecase import QdrantUsecase

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
    qdrant_usecase: QdrantUsecase = Depends(QdrantUsecase)
):
    await job_repository.delete(db=db)
    await asyncio.gather(
        store_lancers_usecase.execute(db=db),
        store_itpro_partners.execute(db=db),
        # store_crowdworks_usecase.execute(db)
    )
    db.flush()
    qdrant_usecase.store_qdrant_by_job(db=db)
    db.commit()
    return "更新完了"
