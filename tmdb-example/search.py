import requests
import json


def search(query):
    url = 'http://localhost:9200/tmdb/movie/_search'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    httpResp = requests.get(url, headers=headers, data=json.dumps(query))
    searchHits = json.loads(httpResp.text)['hits']
    print("Num\tRelevance Score\t\tMovie Title\t\tOverview")
    for idx, hit in enumerate(searchHits['hits']):
            print(f'{idx + 1}\t{hit["_score"]}\t\t{hit["_source"]["title"]}')

usersSearch = 'basketball with cartoon aliens'
query = {
    'query': {
        'multi_match': { 
            'query': usersSearch,
            'fields': ['title^10', 'overview'],
        },
    },
    'size': '100'
}

search(query)
