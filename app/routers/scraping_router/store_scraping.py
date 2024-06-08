from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
import asyncio

from app.usecase.crowdworks.store_crowdworks_usecase import StoreCrowdWorksUsecase
from app.usecase.lancers.store_lancers_usecase import StoreLnacersUsecase
from app.usecase.itpro_partners.store_itpro_partners_usecase import ItproPartnersUsecase

router = APIRouter()

@router.get("/scraping", tags=['スクレイピング'])
async def store_scraping(
    db: Session = Depends(get_db),
    store_crowdworks_usecase: StoreCrowdWorksUsecase = Depends(StoreCrowdWorksUsecase),
    store_lancers_usecase: StoreLnacersUsecase = Depends(StoreLnacersUsecase),
    itpro_partners: ItproPartnersUsecase = Depends(ItproPartnersUsecase)
):
    await asyncio.gather(
        store_lancers_usecase.execute(db),
        itpro_partners.execute(db)
        # store_crowdworks_usecase.execute(db)
    )
    return "更新完了"
