import requests

google_key = "AiZa4r4fu49fh49udh93ujodid3n"

response = requests.get(f'https://any.thing/?key={google_key}').json()
