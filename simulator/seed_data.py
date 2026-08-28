from geopy.geocoders import Nominatim
from faker import Faker
from datetime import date
import random

fake = Faker("en_IN")

EMAIL_DOMAINS = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com", "@zohomail.in"]

KOLKATA_LAT_RANGE = (22.45, 22.67)
KOLKATA_LONG_RANGE = (88.27, 88.45)

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
    lat = round(random.uniform(*KOLKATA_LAT_RANGE), 6)
    long = round(random.uniform(*KOLKATA_LONG_RANGE), 6)
    # location
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.reverse((lat, long))

    address = location.address
    addr_metadata = location.raw["address"]

    city = (
        addr_metadata.get("city")
        or addr_metadata.get("town")
        or addr_metadata.get("village")
    )
    state = addr_metadata.get("state")
    district = addr_metadata.get("state_district")
    pincode = addr_metadata.get("postcode")
    country = "India"


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
        "city": city,
        "district": district,
        "state": state,
        "pincode": pincode,
        "country": country,
        "full_address": address,
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
