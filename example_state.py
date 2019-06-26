#
# STATE #1
# 
# Expecting bid and trump

state_1 = {
    'current_player': 2,
    'expecting_action': 'BID_AND_TRUMP',
    'hand': [
        {'type': 'SPADES', 'number': 2},
        {'type': 'HEARTS', 'number': 12},
        # ...
    ],
    'players': [
        {
            'id': 0,
            'bid': 5,
        },
        {
            'id': 1,
            'bid': 6,
        },
    ],
}

#
# STATE #2
#
# 