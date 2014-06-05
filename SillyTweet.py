#!/usr/bin/env python
import sys
from twython import Twython
CONSUMER_KEY = 'YKa8o1zlxnSMbtEBfU4oDpEct'
CONSUMER_SECRET = '0pnDW0lRQhRekdD9lo4J6kBfKOkDIinY6SpvLUiYHZ5UVEb6Dn'
ACCESS_KEY = '2289141674-VtYo1s7kuXbi4gNc26rpzWPx2qjLdOsQNqUtPDW'
ACCESS_SECRET = 'Qm5b2RaIh79F3Z8uRL4QQPCg7gjnBzXJajvfzC7VkbBD7'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1])
