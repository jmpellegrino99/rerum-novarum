import pgeocode
from timezonefinder import TimezoneFinder

nomi = pgeocode.Nominatim('US')
tf = TimezoneFinder()

for i in range(1, 100000):
    zipcode = f"{i:05d}"
    try:
        info = nomi.query_postal_code(zipcode)
        lat, lon = info.latitude, info.longitude
        tz = tf.timezone_at(lat=lat, lng=lon)
        print(zipcode, tz)
    except:
        continue
