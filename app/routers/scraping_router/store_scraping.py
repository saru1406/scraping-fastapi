from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.usecase.crowdworks.store_crowdworks_usecase import StoreCrowdWorksUsecase

router = APIRouter()

@router.get("/scraping")
async def store_scraping(
    db: Session = Depends(get_db),
    store_crowdworks_usecase: StoreCrowdWorksUsecase = Depends(StoreCrowdWorksUsecase)
):
    store_crowdworks_usecase.execute(db)
    return "更新完了"
