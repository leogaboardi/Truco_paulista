import os, random, time
from cards import *

player_config = None
team_names = None

rules = { #Default rules
	'clean deck': False,
	'players': 4,
	'show all hands': False, #True if you want to print the hands of all players, False for human players only
	'tricks': 3,  # Number of tricks per round. Equal to number of cards dealt per player
	'win_points': 12, # Number of points in order to win the game
	}

player_config = [ #Default players
		{'name': 'Foo','human':False,'team':'Team 1'},
		{'name': 'Bar','human':False,'team':'Team 2'},
		]

class Player():
	def __init__(self,name,team_name='Team 1',human=True):
		self.human = human
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

def check_player_config():
	""" Check if the data in player_config is correct
	"""
	try:
		#Check if the length is correct
		if len(player_config)!=rules['players']:
			raise exception
		#Check if each list element has a 'name' and a 'human'
		for player in player_config:
			if 'name' not in player or 'human' not in player:
				raise exception
		for player in player_config:
			if isinstance(player['human'], bool) == False:
				raise exception
		for player in player_config:
			if isinstance(player['name'], str) == False:
				raise exception
	except:
		print('ERROR: There is something wrong with player_config.')
		sys.exit(0)
	return()

def draw_cards(cards):
	"""Draw the cards among the players
	Arguments:
		show_cards: set True to print all players hands, False to print only player 1 hand
	"""
	global revealed_card

	#Clean up previous round hands
	for player in players:
		player.cards = []
		
	k = 0 #Card counter
	for i in range(rules['tricks']):
		for player in players:
			player.cards.append(cards[k])
			k= k+1
	revealed_card = cards[k]
	draw_trump_card(cards,revealed_card)

	#Sort the cards by decreasing value
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

	for card in cards:
		if card['name']==trump_card:
			if card['suit']=='Spades':card['value']=99
			if card['suit']=='Hearts':card['value']=98
			if card['suit']=='Clubs':card['value']=97
			if card['suit']=='Diamonds':card['value']=96
	return()

def main():
	global teams, players, game_deck
	global no_input

	#Create the deck of cards
	if rules['clean deck']==False:
		game_deck = deck
	else:
		game_deck = []
		for card in deck:
			if card['clean deck']==True:
				game_deck.append(card)

	#try: 
	# Check if the number of players*tricks is higher than number of cards available
	if len(game_deck)<rules['players']*rules['tricks']+1:
		print('ERROR: There are not enough cards for the rules you set. Either decrease the number of players or tricks.')
		raise exception

	# Create the teams
	teams = [Team('Team 1'),Team('Team 2')]

	#Create the players
	players = []
	no_input = True
	if player_config == None:
		print(player_config)
		for i in range(rules['players']):
			name = 'Player '+str(i+1)
			players.append(Player(name,teams[i%len(teams)].name))
	else:
		check_player_config()
		for player_name in player_config:
			players.append(Player(player_name['name'],player_name['team'],player_name['human']))
		for player in players:
			if player.human==True: no_input = False

	input('Press enter to start the game')
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
	print('True')

	for team in teams:
		if team.game_points == max_points:
			winner_team = team.name
	os.system('cls')
	print_game_score()
	print(winner_team,"wins the game!")
	#except:
	#	print('ERROR')
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
	if no_input == False: input("Press any button to draw cards.\n")
	round_deck = shuffle(game_deck)
	draw_cards(round_deck)
	print('Revealed card:',print_card(revealed_card))
	print('Trump card:',trump_card,'\n')

	k = 1 # Trick counter
	while k<=tricks:
		if no_input == False: input("Press any button to play next trick.\n")
		os.system('cls')
		print('##### Round',round_number,'#####\n')
		print_game_score()
		print('Round score (best of',tricks,'):')
		for team in teams:
			print("\t",team.name,":",team.round_points,"points")
		print('\n##### ##### ##### ##### #####\n')
		print('Revealed card:',print_card(revealed_card))
		print('Trump card:',trump_card,'\n')
		print_hands(rules['show all hands'])

		rotated_players = turn_order(players, round_number+k-2)
		winner_team = play_trick(k,rotated_players)
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
					if no_input == False: input("Press any button to continue")
					return(team.name)
		else:
			k = k+1
	#If the while loop ended, it means the teams tied
	print('This round tied, no team won.') 
	if no_input == False: input("Press any button to continue")
	return(None)

def play_trick(trick_number,rotated_players):
	""" Play a trick, which consists of the following steps:
	1 - Each player selects a card. 
	2 - The card with the highest score value wins.
	3 - The played cards are removed from players hands.
	Argument:
		trick_number: which trick of the round (starts at 1)
		rotated_players: the list mof players, rotated based who plays first
	Value:
		winner: the name of the winner team.
		If the trick was tied, None is returned
	"""
	options = [str(x) for x in (range(1,rules['tricks']-trick_number+2))]
	# 1 - Picks the played cards for the trick. Each pair of (player,card)
	# will populate the list trick_cards
	trick_cards = []
	for player in rotated_players:
		if player.human == True:
			while True:
				option = str(input("\nPick a card number: "))
				if option not in options:
					print('Incorrect input, please try again.')
				else:
					option = int(option)-1
					break
			print('You picked',print_card(player.cards[option]),'\n')
			trick_cards.append([player.name,player.team_name,player.cards[option]])
		else: # Computer player. For now, it picks the first card
			trick_cards.append([player.name,player.team_name,player.cards[0]])
		time.sleep(1)
		print('\t',trick_cards[-1][0],'played',print_card(trick_cards[-1][2]))

	# 2 - Check which is the winner card
	winner_card =None
	winner_value = -1
	for card in trick_cards:
		if card[2]['value'] > winner_value:
			winner_value = card[2]['value']
			winner_card = card
	print('\n')
	print('Highest card is the ', print_card(winner_card[2]))
	time.sleep(1)
	print(winner_card[0],'from',winner_card[1], 'wins the trick!')
	time.sleep(1)
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
		for player in players:
			if player.human == True:
				print('\n',player.name,"hand:")
				for i,card in enumerate(player.cards):
					print('\t',i+1,'-',print_card(card))
	print('\n')
	return()

def turn_order(list_name,n):
	rotated_list = list_name[n:]+list_name[:n]
	return(rotated_list)

if __name__ == "__main__":

	player_config = [
		{'name': 'Foo','human':False,'team':'Team 1'},
		{'name': 'Bar','human':True,'team':'Team 2'},
		{'name': 'Batman','human':False,'team':'Team 1'},
		{'name': 'Robin','human': False,'team':'Team 2'},
		]
	#team_names = [
	#	{'name': 'Foobar'},
	#	{'name': 'Batman'},
	#	]

	main()



