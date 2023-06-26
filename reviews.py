'''
Notes: 
	this program takes your amazon search query and gathers all the asins(products) from the first page of results (26ish)
	it then goes to each products page and downloads all the reviews(top 100 recent and top 100 relevant)
	it then takes all those reviews and uses ai to summaries the reviews and rank the product based on your key qualities you are interested in

set up
	step 1 - create your openai api key 
	step 2 - save key to ~/.bash_profile with var name OPENAI_API_KEY
	step three fill in search_text and key_qualities

'''


search_text='quiet portable ac unit'
key_qualities=['noise level','size','price']






from requests_html import HTMLSession
import json
from selectorlib import Extractor
import requests
import time 
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()


#helper functions
def scrape_asins(url,extractor):
	headers = {
		'authority': 'www.amazon.com',
		'pragma': 'no-cache',
		'cache-control': 'no-cache',
		'dnt': '1',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'sec-fetch-site': 'none',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-dest': 'document',
		'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	}
	r = requests.get(url, headers=headers)

	if r.status_code > 500:
		if "To discuss automated access to Amazon data please contact" in r.text:
			print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
		else:
			print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
		return None

	return extractor.extract(r.text)

#helper functions
def get_asins(url):
	s = HTMLSession()
	r = s.get(url)
	r.html.render(sleep=1)
	items = r.html.find('div[data-asin]')

	asins = []
	for item in items:
		if item.attrs['data-asin'] != '':
			asins.append(item.attrs['data-asin'])
	return asins

#helper functions
def chat_with_chatgpt(prompt, model="gpt-3.5-turbo-0301"):
	try:
		response = openai.ChatCompletion.create(
		  model="gpt-3.5-turbo",
		  messages=[{"role": "user", "content": prompt}]
		)
	except:
		time.sleep(22)
		response = openai.ChatCompletion.create(
		  model="gpt-3.5-turbo",
		  messages=[{"role": "user", "content": prompt}]
		)
	return response



search_url        = 'https://www.amazon.com/s?k='+search_text.replace(' ','+')
asins             = get_asins(search_url)
asin_reviews      = {}
key_qualities_str =','.join(key_qualities)

# gather reviews for all the asins
for asin in asins:
	asin_url=f'https://www.amazon.com/bd/{asin}'
	page_no=0
	gathered = []
	while True:
		page_no += 1
		asin_review_page_url1=f'https://www.amazon.com/product-reviews/{asin}/ref=cm_cr_arp_d_viewopt_srt?sortBy=recent&pageNumber={page_no}'
		asin_review_page_url2 = f'https://www.amazon.com/product-reviews/{asin}/ref=?pageNumber={page_no}'

		extractor_reviews = Extractor.from_yaml_file('selectors.yml')
		data1 = scrape_asins(asin_review_page_url1,extractor_reviews)
		data2 = scrape_asins(asin_review_page_url2,extractor_reviews)

		if not data1['reviews'] or not data2['reviews']:
			break

		for review in data1['reviews']:
			gathered.append(review['content'])
		for review in data2['reviews']:
			gathered.append(review['content'])

	reviews=list(set(gathered))

# f=open('asin_reviews.json','w')
# f.write(json.dumps(asin_reviews))
# asin_reviews=json.loads(open('asin_reviews.json').read())
# for asin,reviews in asin_reviews.items():

	has_features=lambda text,key_qualities: any(quality in text.lower() for quality in key_qualities)

	reviews=[r for r in reviews if has_features(r,key_qualities)]
	prompt=f'''please summarize the following product reviews delimited by "x|x" into a very short summary and rate the product these qualities:'{key_qualities_str}'.  reviews:'''+'x|x'.join(reviews)
	response=chat_with_chatgpt(prompt[:17000])
	print(f'https://www.amazon.com/dp/{asin}',response['choices'][0]['message']['content'])
	time.sleep(22)#free version maxes out at 3 calls per minute
