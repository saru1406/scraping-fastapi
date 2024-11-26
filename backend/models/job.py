from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text

from backend.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    link = Column(String(255))
    tags = Column(String(255))
    show = Column(Text)
    price = Column(String(255))
    limit = Column(String(255))

    def __repr__(self):
        return f"Job(id={self.id}, title={self.title}, link={self.link}, tags={self.tags}, show={self.show}, price={self.price}, limit={self.limit})"
