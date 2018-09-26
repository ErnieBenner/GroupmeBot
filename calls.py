# -*- coding: utf-8 -*-
import requests, json, os

# IDEA: Make a new module that contains a message object, rather than a tuple

base_url = 'https://api.groupme.com/v3/'
token = os.environ['GM_API_KEY']
bot_id = os.environ['ROOMMATE_BOT_ID']

class NotReached(Exception):
    pass

def post_message(string, url="https://api.groupme.com/v3/bots/post",
    bot_id=bot_id):
    """Posts a string to the groupchat specified by url and bot_id,
    defaults to Roomies(!)"""

    data = {
    "text": string,
    "bot_id": bot_id
    }

    r = requests.post(url, data=data)


def parse_message(json_str):
    """given json object returns messige info"""
    message = json_str['response']['messages'][0]
    return (message['text'], message['name'], message['created_at'], message['id'])

def read_message(url=(base_url + "groups/38611088/messages?&limit=1&" + token)):
    """Returns json object of the last messages details as (string, sender, time)
    if request fails raise NotReached"""

    r = requests.get(url)
    return json.loads(r.text)

def read_messages(n, url=(base_url + "groups/38611088/messages?")):
    """Returns a list of the last n messages details as (string, sender, time)
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

        error_string = "Either a groupme update broke your system, or response code isn't 200. Response code: %d" % json.loads(r.text)['meta']['code']
        raise NotReached(error_string)
    # message_list = []
    # for messes in messages:
    #
    #     message_list.append((messes['text'], messes['name'], messes['created_at'], messes['id']))
    #
def like(id, url=""):
    """Likes message by message id **unimplimented**"""
    pass

# if __name__ == '__main__':
#
#     quips = [u"To ̷͟͞in̶̴͟v̴ok͡e̡ ̢̢͝t҉̶͘h͜͡e̴ ͘ḩ̨̛i͘ve̶҉͏-͠m҉i̡͏n̨d̨ ̧͝re̵̶͜p̀r̶es҉̨e͡nt̷́̕i҉ņ͟g̶ ̸̷c͘h́a҉̴̨o̡͝s̛̕͜.̷͢͞",
#     u"̮̼̘͍W̳̖͚͈̫i̻͍͔̖ͅṱ̬̤̘h̦̮ͅ ̤̮͉̼̬̜o̹̲͙̦u̻t̳͉̘͚ ͖o͍̪͎̝̖r͙͖͖̭̠͚de̻͙r̻̼̗̜.̼͖"
#     ]
    #post_message(quips[1])
    #post_message(read_message()[0])
