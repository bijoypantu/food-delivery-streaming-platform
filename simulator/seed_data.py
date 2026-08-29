from faker import Faker
from datetime import date
import random
import json
from pprint import pprint

fake = Faker("en_IN")

EMAIL_DOMAINS = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com", "@zohomail.in"]

def load_zones():
    with open("simulator/seed_reference/kolkata_zones.json") as f:
        return json.load(f)

KOLKATA_ZONES = load_zones()

def generate_one_customer(num):
    # personal details
    customer_id = "CUST" + str(num).zfill(4)
    gender = random.choice(["male", "female"])
    first_name = ""
    last_name = ""
    if(gender == "male"):
        first_name = fake.first_name_male()
        last_name = fake.last_name()
    else:
        first_name = fake.first_name_female()
        last_name = fake.last_name()
    date_of_birth = fake.date_of_birth(minimum_age=20, maximum_age=60)

    # contact information
    email_base = random.choice([first_name+last_name, last_name+first_name, first_name])
    email_base = "".join(c for c in email_base if c.isalnum()).lower()
    email = email_base + "".join(fake.random_choices(elements=list("0123456789"), length=random.randint(0, 4))) + random.choice(EMAIL_DOMAINS)

    mobile = random.choice("6789") + "".join(fake.random_choices(
        elements=list("0123456789"),
        length=9
    ))

    # Rough lat/long bounding box for Kolkata and Howrah
    zone = random.choice(KOLKATA_ZONES)
    lat = round(zone["lat"] + random.uniform(-0.005, 0.005), 6)
    long = round(zone["long"] + random.uniform(-0.005, 0.005), 6)

    address = zone["address"]

    joining_date = fake.date_between(
        start_date=date(2026, 1, 1),
        end_date=date(2026, 8, 31)
    )

    return {
        "customer_id": customer_id,
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "date_of_birth": str(date_of_birth),
        "email": email,
        "mobile": mobile,
        "city": zone["city"],
        "district": zone["district"],
        "state": zone["state"],
        "pincode": zone["pincode"],
        "country": "India",
        "full_address": zone["address"],
        "latitude": lat,
        "longitude": long,
        "joining_date": str(joining_date)
    }

def generate_customers(n=50):
    return [generate_one_customer(i+1) for i in range(n)]

def generate_one_driver():
    return

def generate_one_restaurant():
    return

def restaurant_menu_items():
    return


pprint(generate_customers(5), sort_dicts=False)