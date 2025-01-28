import requests


def get_news(country ,apikey='d810b914424b4ba48c9e3fef22a752fe#'):
    #topic_parsed = topic.replace(" ","%20")
    url = f'https://newsapi.org/v2/top-heahlines?{country}&apiKey={apikey}'
    r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2025-1-19&to=2025-1-20&sortBy=popularity&language=en&apiKey=d810b914424b4ba48c9e3fef22a752fe#')

    content = r.json()
    #print(type(content))
    #print(content['articles'][4]['title'])
    articles = content['articles']
    results = []
    print(type(articles))
    #for article in articles:
    #    results.append(f'TITLE\n{article['title']}\nDescription\n{article['description']}\n')

    #return results
    for article in articles:
        print(f'TITLE\n{article['title']}\nDescription\n{article['description']}\n')


print(get_news(country='india'))