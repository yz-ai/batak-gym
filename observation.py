observation = {
    'current_player': 0,  # 0, 1, 2, 3
    'trump_broken': False,
    'expecting_bid': False,
    'expecting_trump': False,
    'current_trump': 'SPADES',
    'current_bid': 0,  # 0 for simple, 4 or more for batak env.
    'last_play': {'type': 'DIAMONDS', 'number': 1, 'source_player': 3},
    'game_count': 4,  # number of games are played so far
    'current_set': [
        {'type': 'CLUBS', 'number': 2, 'source_player': 2},
        {'type': 'CLUBS', 'number': 1, 'source_player': 3},
        # ...
    ],
    'player_observations': [
        {
            'current_player': 0,  # 0, 1, 2, 3,
            'current_player_offset': 0,
            'id': 0,
            'turn_count': 2,  # number of turn passed in this game
            'hand': [
                {'type': 'SPADES', 'number': 1},
                {'type': 'HEARTS', 'number': 3},
                # ...
            ],
            'legal_moves': [
                {'type': 'SPADES', 'number': 1},
                # ...
            ],
            'current_score': 3,
            'minimum_score': 5,
            'game_score': 30
        },
    ]
}
