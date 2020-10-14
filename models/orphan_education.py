#!/usr/bin/python
""" holds class Orphan_education"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Orphan_education(BaseModel, Base):
    """Representation of orphan """

    __tablename__ = 'orphans_education'
    orphan_id = Column(String(60), ForeignKey('orphans.id'), nullable=False)
    school = Column(String(128), nullable=False)
    grade_year = Column(int, nullable=False)
    success = Column(String(20), nullable=True)
    score = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

    def success_year(self):
        """c"""
        if self.success == "True":
            self.grade_year += 1
