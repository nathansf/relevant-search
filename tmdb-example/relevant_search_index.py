import json
import requests


def extract():
    f = open('tmdb.json')
    if f:
        return json.loads(f.read())


def reindex(movie_dict={}):
    settings = {
        "settings": {
            "number_of_shards": 1,
        }
    }

    # if mappingSettings:
    #     settings['mappings'] = mappingSettings

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    resp = requests.delete("http://localhost:9200/tmdb")
    resp = requests.put("http://localhost:9200/tmdb", 
                        data=json.dumps(settings), headers=headers)

    bulkMovies = ""
    print("building...")
    for id, movie in movie_dict.items():
        addCmd = {
            "index": {
                "_index": "tmdb",
                "_type": "movie",
                "_id": movie["id"]
            }
        }
        bulkMovies += json.dumps(addCmd) + "\n" + json.dumps(movie) + "\n"

    print("indexing...")
    resp = requests.post("http://localhost:9200/_bulk", data=bulkMovies, headers=headers)


movie_dict = extract()
reindex(movie_dict=movie_dict)
