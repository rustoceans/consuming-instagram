# coding: utf-8
import urllib2
import json


def num_responses():
    access_token = '1525899796.5b9e1e6.48f9b8caae4d45059c9772b07fcadf55'
    url = 'https://api.instagram.com/v1/tags/pets?access_token={access_token}'.format(
        access_token=access_token)
    response = urllib2.urlopen(url)
    read = response.read()
    media_count = json.loads(read)['data']['media_count']
    return media_count


def get_responses():
    access_token = '1525899796.5b9e1e6.48f9b8caae4d45059c9772b07fcadf55'
    url = 'https://api.instagram.com/v1/tags/pets/media/recent?access_token={access_token}'.format(
        access_token=access_token)
    response = urllib2.urlopen(url)
    read = response.read()
    lenght_response = len(json.loads(read)['data'])
    users = [json.loads(read)['data'][x]['user']['username']
             for x in range(lenght_response)]
    return users
