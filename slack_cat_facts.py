import slack
import slack.chat
import slack.users

import codecs
import random
import time

#from auth import api_token
#slack.api_token = api_token

slack.api_token = 'WEB API KEY GOES HERE LEL'

with codecs.open('cat_facts.txt', 'r', 'utf-8') as file:
    facts = file.readlines()
def cat_fact():
    return random.choice(facts).strip()

users = [x['name'] for x in slack.users.list()['members']]
def user():
    return random.choice(users)
    
def annoy():
    slack.chat.post_message('#cat_facts', cat_fact(), username='Cat Facts')