import requests
import json

def main():
    url = 'http://api.npr.org/query'
    apiKey = 'MDE1MTU3NTg5MDE0MDU0Mjg3ODUxZDQ1NA001'
    numberResults = 5
    responseformat = 'json'
    id = 1019
    requireAssets = 'images,audio,text'
    params = {'apiKey':apiKey, 'numResults':numberResults, 'format':'json', 'id':id, 'requireAssets':requireAssets}

    r = requests.get(url, params=params)

    json_obj = json.loads(r.text)

    print json_obj['list']['title']['$text']
    for story in json_obj['list']['story']:
	print story['title']['$text']
	print story['teaser']['$text']
	for paragraph in story['text']['paragraph']:
	    print paragraph['$text']
	print '-------------------------------'

main()
