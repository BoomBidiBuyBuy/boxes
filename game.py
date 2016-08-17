import random


def change_strategy(boxes, gamer_choose, leader_choose):
    """
    Strategy when game change his position
    """
    for inx in range(3):
        if inx != gamer_choose and inx != leader_choose:
            return boxes[inx]


def non_change_strategy(boxess, gamer_choose, _):
    """
    Strategy when gamer doesn't change his position
    """
    return boxess[gamer_choose]


def game(strategy):
    """
    Common game steps
    """
    # one - where is the money
    boxes = [0, 0, 1]

    # shuffle the boxes
    random.shuffle(boxes)

    # gmaer choose
    gamer_choose = random.randint(0, 2)

    # leader choose
    leader_choose = 0

    for inx in range(3):
        if inx != gamer_choose and boxes[inx] == 0:
            leader_choose = inx
            break

    # apply strategy
    return strategy(boxes, gamer_choose, leader_choose)


def asses_game_with_strategy(strategy, assessments):
    """
    Assess strategy and return probability
    """
    wins = 0

    for _ in range(assessments):
        wins += game(strategy)

    return (wins + 0.0) / assessments

if __name__ == '__main__':
    assessments = 100000

    print "Change strategy win probability : ", asses_game_with_strategy(change_strategy, assessments)
    print "Non change strategy win probability : ", asses_game_with_strategy(non_change_strategy, assessments)
