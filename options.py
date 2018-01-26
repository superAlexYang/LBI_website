from collections import OrderedDict

GENDER = [
    "Male",
    "Female",
    "Unknown"
]

RACE = [
    "American Indian",
    "Asian",
    "Black or African American",
    "Native Hawaiian or Other Pacific Islander",
    "White",
    "Unknown"
]

ATTRATIVENESS = [
    "Eyes",
    "Hair",
    "Face Shape",
    "Skin Colors",
    "Cloths"
]

GROUP_1 = OrderedDict()
GROUP_1["Gender"] = GENDER
GROUP_1["Race"] = RACE
GROUP_1["Attractiveness"] = ATTRATIVENESS
