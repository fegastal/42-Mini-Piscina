#!/usr/bin/python3

# Allowed functions : modules requests, json, dewiki et sys

# https://github.com/daddyd/dewiki
# Python module to remove wiki markup text.
# Whenever you have data that contains wiki markup and want to convert it into human readable plain text, you can use dewiki to do so.

import sys
import requests
import dewiki
import json

# pip install -r requirement.txt

def api_request():

    dictionary = {
        # Parses content and returns parser output
        # https://www.mediawiki.org/wiki/API:Main_page#API_documentation
        "action" : "parse",
        # palavra-chave
        "page" : sys.argv[1],
        # pegando o conteúdo da página wikipedia
        "prop" : "wikitext",
        "format" : "json",
        "redirects" : "true"
    }

    try:
    # O código HTTP 200 OK é a resposta de status de sucesso que
    # indica que a requisição foi bem sucedida.
        content_url = requests.get(url="https://en.wikipedia.org/w/api.php", params=dictionary)
        content_url.raise_for_status()
       # print(content_url)
    # cai nesse primeiro caso se o link ta errado, pq n faz a conexão
    except requests.HTTPError as e:
        raise e
    try:
        object_json = json.loads(content_url.text)
        # json.decoder.JSONDecodeError:
        # Expecting property name enclosed
        # in double quotes: line 2 column 2 (char 3)
    # the JSON object must be str, bytes or bytearray, not bool
    except json.decoder.JSONDecodeError as e:
        raise e
    # se houver erro no action do dictionary (se for algo que não tem la dentro ou algo q tem mas com parametros errados)
    if object_json.get("error") != None:
        # puxa a informação do porquê de acontecer o erro (info)
        raise Exception(object_json["error"]["info"])
    #else:
        #print(object_json.get("error"))
    # retorna o uso da dewiki (biblioteca) para pegar uma string
    # formatada de acordo com parse -> wikitext -> tudo o que tem dentro
    return(dewiki.from_string(object_json["parse"]["wikitext"]["*"]))

def verify_args():
    # se a quantidade de argumentos for diferente de 2
    if (len(sys.argv) != 2):
        sys.exit("Wrong. Use: 'python3 request_wikpedia.py <title>'")
    try:
        wiki_content = api_request()
    except Exception as e:
        print(e)
        exit()
    try:
        #The name of the file must be formatted like this:
        # name_of_the_search.wiki and
        # must not contain any space.
        name_file = sys.argv[1].replace(' ', '_') + '.wiki'
        destiny_file = open(name_file, 'w')
        destiny_file.write(wiki_content)
        destiny_file.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    verify_args()