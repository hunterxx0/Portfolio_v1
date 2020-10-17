#!/usr/bin/python3
""" holds class Family"""
import models
from models.base_model import BaseModel, Base
from models.orphan import Orphan
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime, Table, Integer
from sqlalchemy.orm import relationship

family_subsidy = Table('family_subsidy', Base.metadata,
                       Column('family_id', String(60),
                              ForeignKey('families.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True),
                       Column('subsidy_id', String(60),
                              ForeignKey('subsidies.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True),
                       Column("amount", Integer, nullable=False)
                       )


class Family(BaseModel, Base):
    """Representation of family """

    __tablename__ = 'families'
    cin = Column(String(20), nullable=False, unique=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    sex = Column(String(10), nullable=False)
    birthdate = Column(String(20), nullable=False)
    address = Column(String(50), nullable=False)
    phone = Column(String(30), nullable=False)
    health_ensurance = Column(String(20), nullable=False)
    job = Column(String(20), nullable=False)
    income = Column(Integer, nullable=False)
    home_status = Column(String(20), nullable=False)
    home_owner = Column(String(20), nullable=False)
    health_status = Column(String(20), nullable=False)
    deceased_parent_name = Column(String(20), nullable=False)
    cause_of_death = Column(String(128), nullable=False)
    sponsor_name = Column(String(20), nullable=True)
    family_status = Column(String(30), nullable=False)
    orphans = relationship("Orphan",
                           backref="family",
                           cascade="all, delete, delete-orphan")
    subsidies = relationship("Subsidy",
                             secondary=family_subsidy,
                             viewonly=False)

    def __init__(self, *args, **kwargs):
        """initializes family"""
        super().__init__(*args, **kwargs)
