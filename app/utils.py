import requests
#from decouple import config

#NEWS_API_KEY = config('NEWS_API_KEY')
NEWS_API_KEY = 'fda7d484033e41d9a0c9d3125c25da4e'
COUNTRY = 'br'


def get_latest_news():
    news_data = requests.get(
    #    f'https://newsapi.org/v2/top-headlines?q=Covid&country={COUNTRY}&apiKey={NEWS_API_KEY}').json()
        f'https://newsapi.org/v2/everything?q=covid&%pageSize=3&from=2024-08-01&to=2024-08-30&sortBy=popularity&apiKey={NEWS_API_KEY}').json() #alterar conforme o mes e ano corrente
       # f'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/sp').json()    
    return news_data['articles']


#fiocruz manual ---

a = get_latest_news()
