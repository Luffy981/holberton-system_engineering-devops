#!/usr/bin/python3
"""This module makes a request to reddit api"""
import requests as rq

url = 'https://www.reddit.com/r/{}/hot/.json'


def fill_repetitions(posts=[], ind=0, word_count={}):
    """Count words repetition"""
    if ind >= len(posts):
        return
    post = posts[ind].get('data', {})
    title = post.get('title', '').lower()
    for t in title.split():
        if t in word_count.keys():
            word_count[t] += 1
    fill_repetitions(posts, ind + 1, word_count)


def get_posts(subreddit, word_count={}, params={}):
    """"Fetches a lis of posts"""
    headers = {'User-Agent': 'New agent 1.0'}
    res = rq.get(url.format(subreddit), headers=headers, params=params,
                 allow_redirects=False)

    if res.status_code != 200:
        return None

    try:
        body = res.json().get('data', None)
        if body is None:
            return None
    except ValueError:
        return None

    updated_params = {
        'after': body.get('after', None),
        'count': body.get('dist', 0) + params.get('count', 0),
        'limit': 100
    }

    fill_repetitions(body.get('children', []), 0, word_count)

    if updated_params.get('after') is None:
        return

    return get_posts(subreddit, word_count, updated_params)


def count_words(subreddit, word_list, word_count={}, params={}):
    """This function fetches a reddit posts and prints
    a word count"""
    wl = [w.lower() for w in word_list]

    word_list = list(set(wl))
    word_count = {w: 0 for w in word_list}

    get_posts(subreddit, word_count)

    wc = {}
    for w in wl:
        wc[w] = wc.get(w, 0) + 1

    reps = {}
    for word, count in sorted(word_count.items()):
        if count > 0:
            ls = reps.get(count, [])
            ls.append(word)
            reps[count] = ls

    for count, wlist in sorted(reps.items(), reverse=True):
        for word in sorted(wlist):
            print('{}: {}'.format(word, count * wc.get(word, 1)))
