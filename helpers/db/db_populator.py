# coding: utf-8

# In[75]:


import os, sys
sys.path.insert(0, '.')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flightly.settings")
import django
django.setup()


# In[76]:


from flightly.users.models import FlightlyUser
from flightly.flight_booking.models import Flight, Reservation


# In[77]:


import itertools
from faker import Faker
fake = Faker()
import airlines
import random
import pytz


# In[78]:


for _ in range(50):
    fname = fake.first_name()
    lname = fake.last_name()
    email =  fake.email()
    password = fake.password()
    user = FlightlyUser(email=email,first_name=fname, last_name=lname)
    user.set_password(password)
    user.save()

print(f"FlightlyUsers populates Successfully.")

# In[82]:



from django.db import IntegrityError
air_lines = airlines.get_reports(test=False)
dep_airline_in_cycle = itertools.cycle(air_lines)
random.shuffle(air_lines)
arv_airline_in_cycle = itertools.cycle(air_lines)
timezone = pytz.utc
for _ in range(4):
    try:
        dep_air_line = next(dep_airline_in_cycle)
        arv_air_line = next(arv_airline_in_cycle)
        name = f"{arv_air_line['Statistics']['Carriers']['Names'][1]} {random.randint(11,99)}"
        departure_airport = f"{dep_air_line['Airport']['Name'].split(':')[0]} ({dep_air_line['Airport']['Code']})"
        arrival_airport = f"{arv_air_line['Airport']['Name'].split(':')[0]} ({arv_air_line['Airport']['Code']})"
        departure_datetime=fake.future_datetime(end_date="+45d", tzinfo=timezone)
        capacity=fake.pyint(min=300, max=500, step=1)
        price=fake.pydecimal(right_digits=2, min_value=500, max_value=1500)

        _flight = Flight(
            name=name,
            departure_airport=departure_airport,
            arrival_airport=arrival_airport,
            departure_datetime=departure_datetime,
            capacity=capacity,
            price=price
        )
        _flight.save()
    except IntegrityError:
        # A cheap way to escape IntegrityErrors due to similar names of Flights
        continue
print(f"Flights populates Successfully.")


# In[80]:



travelers = itertools.cycle(FlightlyUser.objects.all())
flights = itertools.cycle(Flight.objects.all())
status_options = ['paid', 'unpaid', 'cancelled']
for _ in range(int(FlightlyUser.objects.all().count()*Flight.objects.all().count()/3.14)):
    traveler=next(travelers)
    flight=next(flights)
    status=random.choice(status_options)
    _reservation = Reservation(traveler=traveler, flight=flight, status=status)
    _reservation.save()

print(f"Reservations populates Successfully.")
# In[ ]:



