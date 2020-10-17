#!/usr/bin/python3
"""
initialize the models package
"""
from models.engine.db_storage import DBStorage
from models.orphan_education import Orphan_education
from datetime import datetime

dt = datetime.today()

storage = DBStorage()
storage.reload()
if dt.month == 7:
    d = storage.all("Orphan_education").values()
    for o in d:
        if o.updated and o.updated != dt.year:
            o.success_year()
