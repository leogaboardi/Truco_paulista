import os, random

#TO DO:
# play_trick(): Currently it is assumed player[0] is human. Needs to create a property in the player object instead
# play_trick(): improve AI
# play_round() and play_game: rotate who is the first player
# play_round(): give points for the winning tricks
# play_trick(): use case for a tied trick
# general: Print formatting are all messed up.
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

rules = {
		'clean deck': False,
		'players': 4,
		'teams': 2,
		'tricks': 3,  # Number of tricks per round. Equal to number of cards dealt per player
		'win_points': 3, # Number of points in order to win the game
		}

trump_card= None
class Player():
	def __init__(self,name,team_name='Team 1'):
		self.name = name
		self.team_name = team_name
		self.cards = []

class Team():
	def __init__(self,team_name):
		self.game_points = 0
		self.round_points = 0
		self.name = team_name

def shuffle(ordered_list,seed=None):
	""" Shuffles a list"""
	random.seed(seed)
	list_shuffled_index = list(range(0,len(ordered_list)-1,1))
	random.shuffle(list_shuffled_index)
	shuffled_list = []
	for card in range(0,len(ordered_list)-1):
		shuffled_list.append(ordered_list[list_shuffled_index[card]])
	return(shuffled_list)

def draw_cards(cards):
	"""Draw the cards among the players
	Arguments:
		show_cards: set True to print all players hands, False to print only player 1 hand
	"""
	#Clean up previous round hands
	for player in players:
		player.cards = []
		
	k = 0 #Card counter
	for i in range(rules['tricks']):
		for player in players:
			player.cards.append(cards[k])
			k= k+1
	
	draw_trump_card(cards,cards[k])
	#Sort the cards from the most powerful to the least powerful
	for player in players:
		for i in range(len(player.cards)-1):
			max_value = -1
			max_card = None
			max_index = None
			temp = None
			for j in range(i, len(player.cards)):
				if player.cards[j]['value']>max_value:
					max_value = player.cards[j]['value']
					max_index = j
					max_card = player.cards[j]
			temp = player.cards[i]
			player.cards[i] = max_card
			player.cards[max_index]=temp
	return()

def draw_trump_card(cards,revealed_card):
	""" Defines the trump card (which is the following card of the revealed card) and assing corresponding values to the trump cards
	"""
	global trump_card 
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

	print('Revealed card:',revealed_card['name'],'of',revealed_card['suit'])
	print('Trump card:',trump_card,'\n')

	for card in cards:
		if card['name']==trump_card:
			if card['suit']=='Spades':card['value']=99
			if card['suit']=='Hearts':card['value']=98
			if card['suit']=='Clubs':card['value']=97
			if card['suit']=='Diamonds':card['value']=96
	return()

def print_card(card):
	string = card['name']+' of '+card['suit']
	return(string)

def print_game_score():
	""" Print score"""
	print('Game score:')
	for i, team in enumerate(teams):
		print("\t",team.name,":",team.game_points,"points")
	if rules['win_points'] > 1:
		print('First team with',rules['win_points'],'points wins')
	else:
		print('First team with',rules['win_points'],'point wins')
	print('')

def print_hands(show_cards=False):
		# Print the hands
	if show_cards:
		for player in players:
			print('\n',player.name,"hand:")
			for i,card in enumerate(player.cards):
				print('\t',i+1,'-',print_card(card))
				#if card['name']==trump_card:
				#	print(' (trump card!)', end="")
	else:
		print('\n\n',players[0].name,"hand:")
		for i,card in enumerate(players[0].cards):
			print('\t',i+1,'-',print_card(card), end="")
			#if card['name']==trump_card:
			#	print(' (trump card!)')
	print('\n')
	return()


def play_round(round_number,tricks):
	""" Play a round (best of N tricks).
	Winner of the trick earns 1 points,
	loser gets 0 points, and a draw is 1/2 point.
	The round winner is whoever gets more than N/2 points first.
	"""

	#Reset the teams round points
	for team in teams:
		team.round_points = 0

	os.system('cls')
	print('##### Round',round_number,'#####\n')
	print_game_score() 
	input("Press any button to draw cards.\n")
	round_deck = shuffle(game_deck)
	draw_cards(round_deck)

	k = 1 # Trick counter

	while k<=tricks:
		input("Press any button to play next trick.\n")
		os.system('cls')
		print('##### Round',round_number,'#####\n')
		print_game_score()
		print('Round score (best of',tricks,'):')
		for team in teams:
			print("\t",team.name,":",team.round_points,"points")
		print('\nTrump card:',trump_card,'\n')
		print_hands(True)
		winner_team = play_trick(k)
		for team in teams:
			if winner_team == None:
				team.round_points = team.round_points + .5
			else:
				if team.name == winner_team:
					team.round_points = team.round_points + 1

		#Check if a team earned enough points to win the round
		if max(team.round_points for team in teams) > tricks/2:
			for team in teams:
				if team.round_points == max(team.round_points for team in teams):
					print(team.name, 'wins the round!') 
					input("Press any button to continue")
					return(team.name)
		else:
			k = k+1
	#If the while loop ended, it means the teams tied
	print('This round tied, no team won.') 
	input("Press any button to continue")
	return(None)

def play_trick(trick_number):
	""" Play a trick, which consists of the following steps:
	1 - Each player selects a card. 
	2 - The card with the highest score value wins.
	3 - The played cards are removed from players hands.
	Argument:
		trick_number: which trick of the round (starts at 1)
	Value:
		winner: the name of the winner team.
		If the trick was tied, None is returned
	"""
	options = [str(x) for x in (range(1,rules['tricks']-trick_number+2))]
	# 1 - Picks the played cards for the trick. Each pair of (player,card)
	# will populate the list trick_cards
	trick_cards = []
	for i,player in enumerate(players):
		if i==0: #Human player
			while True:
				option = str(input("Pick a card number: "))
				if option not in options:
					print('Incorrect input, please try again.')
				else:
					option = int(option)-1
					break
			print('You picked',print_card(player.cards[option]),'\n')
			trick_cards.append([player.name,player.team_name,player.cards[option]])
		else: # Computer player. For now, it picks the first card
			trick_cards.append([player.name,player.team_name,player.cards[0]])
		print(trick_cards[-1][0],'played',print_card(trick_cards[-1][2]))

	# 2 - Check which is the winner card
	winner_card =None
	winner_value = -1
	for card in trick_cards:
		if card[2]['value'] > winner_value:
			winner_value = card[2]['value']
			winner_card = card
	print('\n')
	print('Highest card is the ', print_card(winner_card[2]))
	print(winner_card[0],'from',winner_card[1], 'wins the trick!')

	# 3 - Remove played cards from the hand.
	for i, player in enumerate(players):
		cards_temp = player.cards
		player.cards = []
		j = 0
		for card in cards_temp:
			if card != trick_cards[i][2]:
				player.cards.append(card)
				j = j+1
	return(winner_card[1])

if __name__ == "__main__":

	#Create the deck of cards
	if rules['clean deck']==False:
		game_deck = deck
	else:
		game_deck = []
		for card in deck:
			if card['clean deck']==True:
				game_deck.append(card)

	# Create the teams
	teams = []
	for i in range(rules['teams']):
		name = 'Team '+str(i+1)
		teams.append(Team(name))
	#Create the players
	players = []
	for i in range(rules['players']):
		name = 'Player '+str(i+1)
		players.append(Player(name,teams[i%len(teams)].name))

	#Check the team with highest points:
	max_points = -1
	leading_team = None
	for i, team in enumerate(teams):
		if team.game_points > max_points:
			max_points = team.game_points
			leading_team = team.name
	i = 0
	while(max_points<rules['win_points']): #The main loop of the game
		i = i+1
		round_winner = play_round(i,rules['tricks'])
		print('Round winner:',round_winner)
		for team in teams:
			if team.name == round_winner:
				team.game_points = team.game_points + 1
		max_points = max(team.game_points for team in teams) 
		print('max_points',max_points)

	for team in teams:
		if team.game_points == max_points:
			winner_team = team.name
	os.system('cls')
	print_game_score()
	print(winner_team,"wins the game!")




