# Gym-like environment for the game Batak

This game is a challenging environment for AI projects. One version of the game is the same with spades. It is similar to hearts, bid whist, contract bridge and tarneeb. We will be implementing versions of this game eventually.

## Reinforcement Learning

Batak is a POMDP problem. Its observability is limited to one's hand and the actively picked cards at turns.

## Milestones

We are planning to release this environment step by step.

1. No bidding, spades is the default trump.
2. With bidding, spades is the default trump.
3. With bidding, highest bidder sets the trump.

## Default Rules

1. Can't play another suit, if one has the current trick's suit.
2. Can't lead trump until trump is broken.
3. After all the cards have been played, points are tallied for each player.

## Activatable Rules

1. Must play bigger card.
2. Each of the four player have 13 cards default. The number of cards may change.
