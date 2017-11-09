import random

deck = [
		{'name': '4', 'suit':'Spades','clean deck':False,'value':1},
		{'name': '5', 'suit':'Spades','clean deck':False,'value':2},
		{'name': '6', 'suit':'Spades','clean deck':False,'value':3},
		{'name': '7', 'suit':'Spades','clean deck':False,'value':4},
		{'name': 'Queen', 'suit':'Spades','clean deck':True,'value':5},
		{'name': 'Jack', 'suit':'Spades','clean deck':True,'value':6},
		{'name': 'King', 'suit':'Spades','clean deck':True,'value':7},
		{'name': 'A', 'suit':'Spades','clean deck':True,'value':8},
		{'name': '2', 'suit':'Spades','clean deck':True,'value':9},
		{'name': '3', 'suit':'Spades','clean deck':True,'value':10},

		{'name': '4', 'suit':'Hearts','clean deck':False,'value':1},
		{'name': '5', 'suit':'Hearts','clean deck':False,'value':2},
		{'name': '6', 'suit':'Hearts','clean deck':False,'value':3},
		{'name': '7', 'suit':'Hearts','clean deck':False,'value':4},
		{'name': 'Queen', 'suit':'Hearts','clean deck':True,'value':5},
		{'name': 'Jack', 'suit':'Hearts','clean deck':True,'value':6},
		{'name': 'King', 'suit':'Hearts','clean deck':True,'value':7},
		{'name': 'A', 'suit':'Hearts','clean deck':True,'value':8},
		{'name': '2', 'suit':'Hearts','clean deck':True,'value':9},
		{'name': '3', 'suit':'Hearts','clean deck':True,'value':10},

		{'name': '4', 'suit':'Clubs','clean deck':False,'value':1},
		{'name': '5', 'suit':'Clubs','clean deck':False,'value':2},
		{'name': '6', 'suit':'Clubs','clean deck':False,'value':3},
		{'name': '7', 'suit':'Clubs','clean deck':False,'value':4},
		{'name': 'Queen', 'suit':'Clubs','clean deck':True,'value':5},
		{'name': 'Jack', 'suit':'Clubs','clean deck':True,'value':6},
		{'name': 'King', 'suit':'Clubs','clean deck':True,'value':7},
		{'name': 'A', 'suit':'Clubs','clean deck':True,'value':8},
		{'name': '2', 'suit':'Clubs','clean deck':True,'value':9},
		{'name': '3', 'suit':'Clubs','clean deck':True,'value':10},

		{'name': '4', 'suit':'Diamonds','clean deck':False,'value':1},
		{'name': '5', 'suit':'Diamonds','clean deck':False,'value':2},
		{'name': '6', 'suit':'Diamonds','clean deck':False,'value':3},
		{'name': '7', 'suit':'Diamonds','clean deck':False,'value':4},
		{'name': 'Queen', 'suit':'Diamonds','clean deck':True,'value':5},
		{'name': 'Jack', 'suit':'Diamonds','clean deck':True,'value':6},
		{'name': 'King', 'suit':'Diamonds','clean deck':True,'value':7},
		{'name': 'A', 'suit':'Diamonds','clean deck':True,'value':8},
		{'name': '2', 'suit':'Diamonds','clean deck':True,'value':9},
		{'name': '3', 'suit':'Diamonds','clean deck':True,'value':10},
		]

rules = {'clean deck': True}


def shuffle(ordered_list,seed=None):
	""" Shuffles a list"""
	random.seed(seed)
	list_shuffled_index = list(range(0,len(ordered_list)-1,1))
	random.shuffle(list_shuffled_index)
	shuffled_list = []
	for card in range(0,len(ordered_list)-1):
		shuffled_list.append(ordered_list[list_shuffled_index[card]])
	return(shuffled_list)

def draw_cards(cards, show_cards=False):
	#Draw the cards among the players
	player1_cards = []
	player2_cards = []
	player3_cards = []
	player4_cards = []
	for i in range(3):
		player1_cards.append(cards[0+i])
		player2_cards.append(cards[3+i])
		player3_cards.append(cards[6+i])
		player4_cards.append(cards[9+i])
	#Draw the trump card
	trump_card_name = trump_card(cards,cards[12])
	
	print('Your deck:', end="")
	for cards in player1_cards:
		print('\n\t',cards['name'],'of',cards['suit'], end="")
		if cards['name']==trump_card_name:
			print(' (trump card!)', end="")
	print('\n')


def trump_card(cards,revealed_card):
	""" Defines the trump card (which is the following card of the revealed card) and assing corresponding values to the trump cards
	"""
	if revealed_card['name']=='4': 	trump_card = '5'
	if revealed_card['name']=='5': 	trump_card = '6'
	if revealed_card['name']=='6': 	trump_card = '7'
	if revealed_card['name']=='7': 	trump_card = 'Queen'
	if revealed_card['name']=='Queen': 	trump_card = 'Jack'
	if revealed_card['name']=='Jack': 	trump_card = 'King'
	if revealed_card['name']=='King': 	trump_card = 'A'
	if revealed_card['name']=='A': 	trump_card = '2'
	if revealed_card['name']=='2': 	trump_card = '3'
	if revealed_card['name']=='3' and rules['clean deck']==False: 	trump_card = '4'
	if revealed_card['name']=='3' and rules['clean deck']==True: 	trump_card = 'Queen'

	print('The revealed card:',revealed_card['name'],'of',revealed_card['suit'])
	print('The trump card:',trump_card,'\n')

	for card in cards:
		if card['name']==trump_card:
			if card['suit']=='Spades':card['value']=99
			if card['suit']=='Hearts':card['value']=98
			if card['suit']=='Clubs':card['value']=97
			if card['suit']=='Diamonds':card['value']=96
	return(trump_card)

if __name__ == "__main__":
	if rules['clean deck']==False:
		game_deck = deck
	else:
		game_deck = []
		for card in deck:
			if card['clean deck']==True:
				game_deck.append(card)
	
	round_deck = shuffle(game_deck)
	draw_cards(round_deck)
