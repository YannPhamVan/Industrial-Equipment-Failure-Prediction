import requests
import random, json

url = "http://localhost:9696/predict"

equipments = [{'temperature': 69.94045290787271,
               'pressure': 26.18938696984232,
               'vibration': 0.6971832984686062,
               'humidity': 52.640224489963536,
               'equipment': 'turbine',
               'location': 'atlanta'},
              {'temperature': 149,
               'pressure': 35,
               'vibration': 4,
               'humidity': 50,
               'equipment': 'turbine',
               'location': 'atlanta'}]

r = random.randint(0, 1)
response = requests.post(url, json=equipments[r]).json()
print(f"Equipment: {equipments[r]}")
print(f"Prediction: {response}")