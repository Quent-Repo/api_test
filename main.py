import requests
import random
import json
import webbrowser

num = random.randint(40,400)
api_url = "https://api.guildwars2.com/v2/items?ids="+str(num)+"&lang=en"
porn = requests.get(api_url)
x = (porn.json()[0]['icon'])
webbrowser.open(x)
