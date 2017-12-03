import sys, unittest
sys.path.insert(0,'..')
from main import *

player_config = [ #Default players
		{'name': 'Foo','human':False,'team':'Team 1'},
		{'name': 'Bar','human':False,'team':'Team 2'},
		]

class TestStringMethods(unittest.TestCase):

    def test_trick(self):
        self.assertEqual(play_trick(1,players))

if __name__ == '__main__':
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
	unittest.main()