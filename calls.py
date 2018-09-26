# -*- coding: utf-8 -*-
import requests, json, os

#This change might allow for there to be one class with general functions, which can then be subclassed to allow specific api calls. 
# a sub class for each messaging platform. 
#base_url = 'https://api.groupme.com/v3/'
#token = os.environ['GM_API_KEY']
#bot_id = os.environ['ROOMMATE_BOT_ID']

class NotReached(Exception):
    pass

class Caller(object):
    
    
    def __init__(self, base_url, token, bot_id):
        self.base_url = base_url
        self.token = token
        self.bot_id = bot_id
    
    def post_message(self, string, url=(self.base_url + "/bots/post"):
        """Posts a string to the groupchat arguments"""

        data = {
        "text": string,
        "bot_id": self.bot_id
        }

        r = requests.post(url, data=data)

    def read_messages(self, n, url=(self.base_url + "groups/38611088/messages?")):
        """Returns a list of the last n messages details as (string, sender, time, message id)
        if request fails raise NotReached"""

        limit = "&limit=%d&" % n
        url = url + limit + self.token
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

    def like(id, url=""):
        """Likes message by message id **unimplimented**"""
        pass
