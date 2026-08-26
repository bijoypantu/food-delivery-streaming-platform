from faker import Faker
import random

fake = Faker("en_IN")

def generate_one_customer(num):
    # personal details
    customer_id = "CUST"
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
    EMAIL_DOMAINS = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com", "@zohomail.in"]
    email_base = random.choice([first_name+last_name, last_name+first_name, first_name])
    email_base = "".join(c for c in email_base if c.isalnum()).lower()
    email = email_base + "".join(fake.random_choices(elements=list("0123456789"), length=random.randint(0, 4))) + random.choice(EMAIL_DOMAINS)

    mobile = random.choice("6789") + "".join(fake.random_choices(
        elements=list("0123456789"),
        length=9
    ))

    # location
    WEST_BENGAL_CITIES = [
        "Kolkata", "Howrah", "Durgapur", "Siliguri", "Asansol",
        "Kharagpur", "Bardhaman", "Malda", "Baharampur", "Habra"
    ]
    city = random.choice(WEST_BENGAL_CITIES)
    state = "West Bengal"
    country = "India"

    # Rough lat/long bounding box for West Bengal
    WB_LAT_RANGE = (21.5, 27.0)
    WB_LONG_RANGE = (85.8, 89.9)
    lat = round(random.uniform(*WB_LAT_RANGE), 6)
    long = round(random.uniform(*WB_LONG_RANGE), 6)

    joining_date = fake.date_between(
        start_date='2026-01-01',
        end_date='2026-08-31'
    )

def generate_customers(n=50):
    return [generate_one_customer(i+1) for i in range(n)]

def generate_one_driver():
    return

def generate_one_restaurant():
    return

def restaurant_menu_items():
    return
