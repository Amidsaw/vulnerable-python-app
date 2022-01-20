import requests

google_key = "AIzaSyCaEAG3n587vn4m5a2zllpuURIzGJA2h4uyf73"
google_key_2 = "AIzaSyCaEAG3n587vn4m5a2zllpuURIzGJA2h4uyf74"

response = requests.get(f'https://any.thing/?key={google_key}').json()
