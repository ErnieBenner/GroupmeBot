# -*- coding: utf-8 -*-
import requests, json, os


base_url = 'https://api.groupme.com/v3/'
token = os.environ['GM_API_KEY']
bot_id = os.environ['ROOMMATE_BOT_ID']
group_id = os.environ['GROUP_ID']

class NotReached(Exception):
    pass


def post_message(string, url="https://api.groupme.com/v3/bots/post", bot_id=bot_id):
    """Posts a string to the groupchat arguments"""

    data = {
    "text": string,
    "bot_id": bot_id
    }

    r = requests.post(url, data=data)

def read_messages(n, url=(base_url + "groups/38611088/messages?")):
    """Returns a list of the last n messages details as (string, sender, time, message id)
    if request fails raise NotReached"""

    limit = "&limit=%d&" % n
    url = url + limit + token
    r = requests.get(url)
    
    try:

        messages = json.loads(r.text)['response']["messages"]
        return [(messes['text'], messes['name'], messes['created_at'], messes['id']) for messes in messages]

    except TypeError:

        raise NotReached("read_message request call returned 'None'")

    except KeyError:

        error_string = "Either a groupme update broke your system, or response code isn't 200. Response code: 
        %d" % json.loads(r.text)['meta']['code']
        raise NotReached(error_string)

def like(message_id, url=(base_url + "/messages/"),group_id=group_id):
    """Likes message by message id"""
    url = url + str(group_id) + '/' + str(message_id) + '/like'
    r = request.post(url)

# def read_since(n, since, url=(base_url + "what ever the gm api says")):
#     """read's n messages since the given time"""
#     pass

# def read_before(n, before, url=(base_url + "GM API STUFF"))
#     """Reads n messages before the specified time"""
#     pass
                ""
