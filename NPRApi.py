from urllib.request import urlopen
import json

#1007 Science topics
#1019 Technology topics

def main():
	url = 'http://api.npr.org/query?apiKey=' 
	urlKey = 'MDE1MDg3NzIyMDE0MDQwMzE2NDlmNDhlZA001'
	urlNumberResults = '&numResults=5'
	urlFormat = '&format=json'
	urlId = '&id=1019'
	urlRequireAssets = '&requireAssets=images,audio,text'

	url += urlKey + urlNumberResults + urlFormat + urlId + urlRequireAssets

	response = getResponse(url)
	json_obj = parseToJson(response)

	print(json_obj['list']['title']['$text'] + "\n")

	for story in json_obj['list']['story']:
		print(story['title']['$text'] + "\n")
		print(story['teaser']['$text'])
		print(story['storyDate']['$text'] + "\n")
		for paragraph in story['text']['paragraph']:
			print(paragraph['$text'] + "\n")
		print("-------------------------------" + "\n")

def getResponse(url):
	return str(urlopen(url).read().decode('utf-8'))

def parseToJson(response):
	return json.loads(response)

if __name__ == "__main__":
	main()