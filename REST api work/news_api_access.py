import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2025-1-19&to=2025-1-20&sortBy=popularity&language=en&apiKey=d810b914424b4ba48c9e3fef22a752fe#')
content = r.json()

print(type(content))
print(content['articles'][4]['title'])