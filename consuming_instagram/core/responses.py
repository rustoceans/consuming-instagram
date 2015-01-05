# coding: utf-8
import urllib2
import json
from collections import Counter as c
from django.conf import settings


access_token = settings.ACCESS_TOKEN

url_default = 'https://api.instagram.com/v1/tags/pets/media/recent?access_token={access_token}'.format(
    access_token=access_token)

url_to_length = 'https://api.instagram.com/v1/tags/pets?access_token={access_token}'.format(
    access_token=access_token)


def _length_urls():
    return None


def get_response(url):
    response = urllib2.urlopen(url)
    read = response.read()
    json_response = json.loads(read)
    return json_response


def num_responses():
    response = urllib2.urlopen(url_to_length)
    read = response.read()
    media_count = json.loads(read)['data']['media_count']
    return media_count


def get_users_responses():
    response = urllib2.urlopen(url_default)
    read = response.read()
    lenght_response = len(json.loads(read)['data'])
    users = [json.loads(read)['data'][x]['user']['username']
             for x in range(lenght_response)]
    return users


def get_length_users():
    counter_users = c(consuming_instagram())
    return len(counter_users)


def consuming_instagram():
    datas = get_response(url_default)
    next_url = datas['pagination']['next_url']
    users, cat_users, dog_users = [], [], []
    for i in range(1):
        datas = get_response(next_url)
        for u in range(len(get_users_responses())):
            users.append(datas['data'][u]['user']['username'])
            if 'cat' in datas['data'][u]['tags']:
                cat_users.append(datas['data'][u]['user']['username'])
            elif 'dog' in datas['data'][u]['tags']:
                dog_users.append(datas['data'][u]['user']['username'])
        next_url = datas['pagination']['next_url']
    res = lambda x=(len(c(users)), len(c(cat_users)), len(c(dog_users))): x
    return _research(res())


def _research(*args):
    request = args[0]
    users, cat_users, dog_users = request[0], request[1], request[2]
    other_users = lambda x=users: users - (cat_users + dog_users)
    return users, cat_users, dog_users, other_users()
