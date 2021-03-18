import sys
from trello import TrelloApi
from trello import Boards
from trello import Actions
from trello import Lists


def add_card(tlist, name, description=None):
    try:
        lists = Lists(trello_key, trello_token)
        list_id = tlist[0]['id']
        print(list_id)
        print(lists.new_card)
        card = lists.new_card(list_id,name, due="3/19/2021",desc=description)
        return card
    except Exception as e:
        print(f" error {e}")
        raise

trello_key='9f4dbd353b6f9d815ff76bce29fb3ffa'
trello_secret = 'cf0c804e47bbb38dc4c57369727b605c974caa68ee95bde67a2eb0210f9391f7'
trello_token = '77850847cbd43e62004e89b0714b2885c3595c5cd73edeb44ad29cccf076b8db'
boards = Boards(trello_key,trello_token)

list = boards.get_list("20wnIRuI")
print(list)

card = add_card(list,"Remote Access","Remote access is test")
