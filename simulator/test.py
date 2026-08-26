from faker import Faker
import random

fake = Faker("en_IN")

mobile = fake.random_element(
    elements=["6", "7", "8", "9"]
) + "".join(fake.random_choices(
    elements=list("0123456789"),
    length=9
))

print(mobile)