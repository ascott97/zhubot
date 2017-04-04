import requests
import json
import random
import re

subreddits = ['dankmemes']
popularity = ['month', 'year', 'all']

url = ("https://reddit.com/r/" + subreddits[random.randint(0,(len(subreddits) - 1))] + "/top/.json")
headers = { 'User-Agent': 'Desktop:zhubot:v0.1.0 (by /u/zhubot)' }
params = {'limit': 50,
          't': popularity[random.randint(0,(len(popularity)-1))],}


def get_memes():
    
    response = requests.get(url, headers=headers, params=params)
    try:
        data_dict = json.loads(response.text)
    except:
        print(response)
    total_memes = len(data_dict['data']['children'])
    meme = data_dict['data']['children'][random.randint(0,(total_memes - 1))]['data']['url']
    
    #Check url from ireddituploads doesnt contain &amp; as it breaks the link
    if 'i.reddituploads' in meme and '&amp;' in meme:
        meme = re.sub('&amp;', '&', meme)
    return meme

