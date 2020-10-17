#!/usr/bin/python
""" holds class Orphan"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Orphan(BaseModel, Base):
    """Representation of orphan """

    __tablename__ = 'orphans'
    family_id = Column(String(60), ForeignKey('families.id'), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    sex = Column(String(128), nullable=False)
    birthdate = Column(String(128), nullable=False)
    health_status = Column(String(128), nullable=False)
    Hobbies = Column(String(128), nullable=False)
    education_status = Column(String(128), nullable=False)
    # pupil / jobless / employee / etc
    if education_status == "pupil":
        orphan_education = relationship("Orphan_education",
                                        backref="orphans",
                                        cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
