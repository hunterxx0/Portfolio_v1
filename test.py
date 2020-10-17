#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models.family import *
from models.subsidy import *
from models.orphan_education import *
from models import storage
"""
# creation of a Family
d = {
    'cin': '545454',
    'first_name': 'rffrf',
    'last_name': 'frfrf',
    'sex': "vfrvfrv",
    'birthdate': "151515",
    'address': "545454",
    'phone': "5454545",
    'health_ensurance': "frfrf",
    'income': 1451,
    'home_status': "45454",
    'home_owner': "frfrfr",
    'health_status': "frfnrf",
    'deceased_parent_name': "rfrrfr",
    'cause_of_death': "hruivfr",
    'sponsor_name': "dhfirf",
    "family_status": "geriof",
    "job": "rffff"
}

f = Family(**d)
f.save()


# creation of a Subsidy
d = {
    'sub_type': '545454',
    'title': 'rffrf',
    'description': "vfrvfrv",
    'price_unit': "151515",
    'gender': "frfrf",
    'age_min': "frfrfr",
    'age_max': "frfnrf",
    'status': "0346a287-67f1-49dd-ae7c-310f69d31372",
    'amount': 11,
    'unit': "034c-310f31372",
}

s = Subsidy(**d)
s.save()

print(s)
# link subsidy with family
f.subsidies.append(s)
storage.save()

print(f)
"""
# creation of a Orphan
d = {
    'first_name': '545454',
    'last_name': 'rffrf',
    'sex': "vfrvfrv",
    'birthdate': "151515",
    'health_status': "frfrf",
    'Hobbies': "frfrfr",
    'education_status': "frfnrf",
    'family_id': "d28a0698-b266-4571-a934-fbf476db3063"
}

f = Orphan(**d)
f.save()

print(f)

print(f.id)

# create orphan education
d = {
    'orphan_id': f.id,
    'school': 'rffrf',
    'grade_year': 2020,
    'success': "151515",
    'score': "frfrf",
    'updated': 5
}

f = Orphan_education(**d)
f.save()
print(f)
