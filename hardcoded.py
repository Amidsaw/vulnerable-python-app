import requests

google_key = "AIzaSyCaEAG3n587vn4m5a2zllpuURIzGJA2h4uyf73"

response = requests.get(f'https://any.thing/?key={google_key}').json()
