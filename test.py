#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models.family import Family

# creation of a State
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

print(f)

"""
# creation of a City
city = City(state_id=state.id, name="San Francisco")
city.save()

# creation of a User
user = User(email="john@snow.com", password="johnpwd")
user.save()

# creation of 2 Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

storage.save()

print("OK")
"""
