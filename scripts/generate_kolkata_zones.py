from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import json
import os

LOCALITIES = [
    "Salt Lake", "New Town", "Park Street", "Ballygunge", "Garia", "Jadavpur", "Tollygunge", "Behala", "Alipore",
    "Kalighat", "Bhawanipur", "New Alipore", "Kasba", "Sealdah", "Esplanade", "Dharmatala", "Shyambazar",
    "Hatibagan", "Maniktala", "Ultadanga", "Kankurgachi", "Dum Dum", "Lake Town", "Kestopur", "Baguiati", "Nimta",
    "Nagerbazar", "Belgachia", "Cossipore", "Beliaghata", "Tangra", "Topsia", "Rajarhat", "Sodepur", "Howrah Maidan",
    "Shibpur", "Santragachi", "Bally", "Belur", "Liluah", "Kadamtala", "Golabari", "Salkia", "Dasnagar", "Ramrajatala",
    "Andul", "Kona", "Domjur", "Jagacha", "Chowringhee", "Camac Street", "Theatre Road", "Burrabazar", "Jorasanko",
    "Sovabazar", "Bagbazar", "Park Circus", "Minto Park", "Rashbehari Avenue", "Dhakuria", "Gariahat", "Patuli",
    "Dum Dum Cantonment", "Baranagar", "Madhyamgram", "Shalimar", "Bamunara", "Belur Math", "Kalikapur", "Mukundapur"
]

geolocator = Nominatim(user_agent="project_required_localities")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

zones = []

for name in LOCALITIES:
    location = geocode(
        f"{name}, West Bengal, India",
        addressdetails=True
    )

    if location is None:
        print(f"Could not geocode: {name}")
        continue

    address = location.raw.get("address", {})

    city = (
        address.get("city")
        or address.get("town")
        or address.get("village")
        or address.get("municipality")
    )

    zones.append({
        "locality": name,
        "city": city,
        "district": address.get("state_district"),
        "state": address.get("state"),
        "pincode": address.get("postcode"),
        "country": address.get("country"),
        "address": location.address,
        "lat": location.latitude,
        "long": location.longitude
    })

os.makedirs("simulator/seed_reference", exist_ok=True)
with open("simulator/seed_reference/kolkata_zones.json", "w") as f:
    json.dump(zones, f, indent=2)

print(f"Saved {len(zones)} zones.")