from faker import Faker
import random

fake = Faker("en_IN")

EMAIL_DOMAINS = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com", "@zohomail.in"]
WEST_BENGAL_CITIES = [
    "Kolkata", "Howrah", "Durgapur", "Siliguri", "Asansol",
    "Kharagpur", "Bardhaman", "Malda", "Baharampur", "Habra"
]
WB_LAT_RANGE = (21.5, 27.0)
WB_LONG_RANGE = (85.8, 89.9)
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

    # location    
    city = random.choice(WEST_BENGAL_CITIES)
    state = "West Bengal"
    country = "India"

    # Rough lat/long bounding box for West Bengal
    lat = round(random.uniform(*WB_LAT_RANGE), 6)
    long = round(random.uniform(*WB_LONG_RANGE), 6)

    joining_date = fake.date_between(
        start_date='2026-01-01',
        end_date='2026-08-31'
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
        "state": state,
        "country": country,
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
