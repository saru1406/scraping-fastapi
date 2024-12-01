from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text

from backend.database import Base


class Custom(Base):
    __tablename__ = "customs"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    body = Column(Text)
