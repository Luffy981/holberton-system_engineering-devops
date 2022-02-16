#!/usr/bin/python3
"""GET to api"""
import requests


def recurse(subreddit, word_list, after="", dic={}):
    """recursive function"""
    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    h = {'User-Agent': 'Reddit API test'}
    params = {'limit': 200, 'after': after}
    r = requests.get(base_url, headers=h, allow_redirects=False, params=params)
    if r.status_code != 200:
        return None
    d = r.json()
    if after is None:
        return dic
    l = d.get('data', {}).get('children')
    for i in l:
        title = i.get('data', {}).get('title').lower().split()
        for j in word_list:
            for t in title:
                if j == t:
                    if j not in dic:
                        dic[j] = 1
                    else:
                        dic[j] += 1
    p = d.get('data', {}).get('after')
    return recurse(subreddit, word_list, p, dic)


def count_words(subreddit, word_list):
    """Cound # of keywords"""
    for i, e in enumerate(word_list):
        word_list[i] = e.lower()
    d = recurse(subreddit, word_list)
    if d:
        for key, value in sorted(d.items(), key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(key, value))
    elif d is None:
        print()
