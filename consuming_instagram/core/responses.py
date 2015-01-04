# coding: utf-8
import urllib2
import json
from collections import Counter as c


access_token = '1525899796.5b9e1e6.48f9b8caae4d45059c9772b07fcadf55'

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
    cat_users, dog_users = [], []
    for i in range(143):
        datas = get_response(next_url)
        for u in range(len(get_users_responses())):
            if 'cat' in datas['data'][u]['tags']:
                cat_users.append(datas['data'][u]['user']['username'])
            elif 'dog' in datas['data'][u]['tags']:
                dog_users.append(datas['data'][u]['user']['username'])
        next_url = datas['pagination']['next_url']
    return cat_users, dog_users
