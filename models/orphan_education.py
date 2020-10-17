#!/usr/bin/python
""" holds class Orphan_education"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from datetime import datetime


class Orphan_education(BaseModel, Base):
    """Representation of orphan """

    __tablename__ = 'orphans_education'
    orphan_id = Column(String(60), ForeignKey('orphans.id'), nullable=False)
    school = Column(String(128), nullable=False)
    grade_year = Column(Integer, nullable=False)
    success = Column(String(20), nullable=True)
    score = Column(String(128), nullable=False)
    updated = Column(Integer, nullable=True)

    def __init__(self, *args, **kwargs):
        """initializes orphan_education"""
        super().__init__(*args, **kwargs)

    def success_year(self):
        """c"""
        dt = datetime.now()
        if self.success == "True":
            self.grade_year += 1
            self.updated = dt.year
            self.save()
