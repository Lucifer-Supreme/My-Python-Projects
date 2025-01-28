import requests


def get_news(topic, from_date,to_date,language='en',apikey='d810b914424b4ba48c9e3fef22a752fe#'):
    topic_parsed = topic.replace(" ","%20")
    url = f'https://newsapi.org/v2/everything?qInTitle={topic_parsed}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={apikey}'
    r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2025-1-19&to=2025-1-20&sortBy=popularity&language=en&apiKey=d810b914424b4ba48c9e3fef22a752fe#')

    content = r.json()
    #print(type(content))
    #print(content['articles'][4]['title'])
    articles = content['articles']
    results = []
    print(type(articles))
    for article in articles:
        results.append(f'TITLE\n{article['title']}\nDescription\n{article['description']}\n')

    return results


print(get_news(topic='space',from_date='2025-1-15',to_date='2025-1-20'))