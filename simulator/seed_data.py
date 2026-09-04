from faker import Faker
from datetime import date
import random
import json
from pprint import pprint
from .config import VEHICLE_DATABASE, EMAIL_DOMAINS

fake = Faker("en_IN")

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

def generate_one_driver(num):
    driver_id = "DRIV" + str(num).zfill(4)

    # Personal Information
    gender = random.choice(["male", "female"])
    first_name = ""
    last_name = ""
    if (gender == "male"):
        first_name = fake.first_name_male()
        last_name = fake.last_name()
    else:
        first_name = fake.first_name_female()
        last_name = fake.last_name()
    dob = fake.date_of_birth(minimum_age=21, maximum_age=45)

    # contact information
    email_base = random.choice([first_name+last_name, last_name+first_name, first_name])
    email_base = "".join(c for c in email_base if c.isalnum()).lower()
    email = email_base + "".join(fake.random_choices(elements=list("0123456789"), length=random.randint(0, 4))) + random.choice(EMAIL_DOMAINS)

    mobile = random.choice("6789") + "".join(fake.random_choices(
        elements=list("0123456789"),
        length=9
    ))

    #Vehicle Information
    vehicle = random.choices(VEHICLE_DATABASE, weights=[0.55, 0.40, 0.05], k=1)[0]
    vehicle_type = vehicle["category"]
    vehicle_model = random.choice(vehicle["models"])

    # Vehicle Number
    rto_code = f"{random.randint(1, 99):02d}"
    series_and_number = fake.bothify(text="?? ####").upper()
    vehicle_number = f"WB {rto_code} {series_and_number}"

    #Geographic Information
    zone = random.choice(KOLKATA_ZONES)
    lat = round(zone["lat"] + random.uniform(-0.005, 0.005), 6)
    long = round(zone["long"] + random.uniform(-0.005, 0.005), 6)

    joining_date = fake.date_between(
        start_date=date(2026, 1, 1),
        end_date=date(2026, 8, 31)
    )

    return {
        "driver_id":        driver_id,
        "first_name":       first_name,
        "last_name":        last_name,
        "gender":           gender,
        "date_of_birth":    str(dob),
        "email":            email,
        "mobile_no":        mobile,
        "city":             zone["city"],
        "district":         zone["district"],
        "state":            zone["state"],
        "pincode":          zone["pincode"],
        "country":          zone["country"],
        "full_address":     zone["address"],
        "lat":              lat,
        "long":             long,
        "vehicle_type":     vehicle_type,
        "vehicle_model":    vehicle_model,
        "vehicle_number":   vehicle_number,
        "joining_date":     str(joining_date)
    }

def generate_drivers(n=50):
    return [generate_one_driver(i+1) for i in range(n)]

def generate_one_restaurant():
    return

def restaurant_menu_items():
    return


pprint(generate_drivers(5), sort_dicts=False)