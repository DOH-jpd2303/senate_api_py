#Load modules
import requests
import math
import funs

#Specify your auth token for the website. This allows more downloads per hour.
api_key_fn = r'C:\Users\jondo\Documents\PyR\Upwork\LobbySearch\data\api_key.txt'
api_key = open(api_key_fn, 'r').read()

auth_header = {'Authorization': f"""Token {api_key}"""}

#Specify the filing date range of reports you want
post_start = '2021-01-01'
post_end = '2021-03-23'

#Specify the main url and filters for start/end date
url = 'https://lda.senate.gov/api/v1/filings/'
filter_start = 'filing_dt_posted_after=' + post_start
filter_end = 'filing_dt_posted_before=' + post_end
full_url = url + '?' + filter_start + '&' + filter_end 

#Send the request (with the authorization header)
resp = requests.get(full_url, headers = auth_header)

#Convert to json
dat = resp.json()

#Get page metadata
rec_count = dat['count']
rec_per_page = len(dat['results'])
n_pages = math.ceil(rec_count/rec_per_page)

#Pull out the query results for the page
results = dat['results']

lul = funs.flatten_filing_info(results)