#!/usr/bin/python
""" holds class Subsidy"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Subsidy(BaseModel, Base):
    """Representation of Subsidy"""

    __tablename__ = 'subsidies'
    sub_type = Column(String(30), nullable=False)
    title = Column(String(30), nullable=False)
    description = Column(String(128), nullable=False)
    price_unit = Column(String(20), nullable=False)
    gender = Column(String(20), nullable=False)
    age_min = Column(String(10), nullable=False)
    age_max = Column(String(10), nullable=False)
    status = Column(String(128), nullable=False)
    amount = Column(Integer, nullable=False)
    unit = Column(String(20), nullable=True)

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
