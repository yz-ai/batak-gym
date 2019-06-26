observation = {
    'current_player': 0,  # 0, 1, 2, 3
    'trump_broken': False,
    'expecting_action': 'HAND', # 'BID', 'BID_AND_TRUMP'
    'current_trump': 'SPADES',
    'current_bid_holder': {
        'source_player': 0,
        'bid': 6,
    },
    'turn_count': 2,  # number of turn passed in this game
    'current_game_count': 4,  # number of games are played so far
    'total_game_count': 10, # maximum game count until game decision
    'last_play': {'type': 'DIAMONDS', 'number': 1, 'source_player': 3},
    'current_set': [
        {'type': 'CLUBS', 'number': 2, 'source_player': 2},
        {'type': 'CLUBS', 'number': 1, 'source_player': 3},
        # ...
    ],
    'players': [
        {
            'id': 0,
            'current_player_offset': 0,
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
            'current_bid': 5,
            'game_score': 30,
        },
    ],
}

action = {
    {'type': 'HAND', 'card_type': 'SPADES', 'number': 1},
    {'type': 'BID', 'bid': 5},
    {'type': 'BID_AND_TRUMP', 'card_type': 'SPADES', 'bid': 5},
}
