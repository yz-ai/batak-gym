
observation = {
	'current_player': 0, # 0, 1, 2, 3, 4
	'trump_broken': False,
	'expecting_bid': False,
	'expecting_trump': False,
	'current_trump': 'SPADES',
	'player_observations': [
		{
			'last_play': { 'type': 'DIAMONDS', 'number': 1, 'source_player': 3 },
			'hand': [
				{ 'type': 'SPADES', 'number': 1 },
				{ 'type', 'HEARTS', 'number': 3 },
				# ...
			],
			'legal_moves': [
				{ 'type': 'SPADES', 'number': 1 },
				# ...
			],
			'current_set': [
				{ 'type': 'CLUBS', 'number': 2, 'source_player': 2 },
				{ 'type': 'CLUBS', 'number': 1, 'source_player': 3 },
				# ...
			],
			# ...
		},
		# ...
	],
}
