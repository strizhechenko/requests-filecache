# coding=utf-8

import os
import requests


def get(url):
    """
    Cache miss: performs request to :param: url and caches it in file ./cache/host/path
    Cache hit: reads cached response from file ./cache/host/path
    """
    os.makedirs('cache/', exist_ok=True)
    filename = 'cache/' + url.replace('http://', '', 1).replace('https://', '', 1)
    if not filename.endswith('.html'):
        filename += '.html'
    if not os.path.exists(filename):
        data = requests.get(url).content.decode('utf-8')  # .encode('utf-8')
        with open(filename, 'w', encoding='utf-8') as fd:
            fd.write(data)
    else:
        with open(filename, encoding='utf-8') as fd:
            return fd.read()
    return data
