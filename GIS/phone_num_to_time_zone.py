import phonenumbers
from phonenumbers import timezone

number = phonenumbers.parse("+13476694639", "US")  # Example NYC number
time_zones = timezone.time_zones_for_number(number)
print(time_zones)
