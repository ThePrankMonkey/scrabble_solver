def score(dice: list) -> dict:
    scores = {
        "aces": 0,
        "twos": 0,
        "threes": 0,
        "fours": 0,
        "fives": 0,
        "sixes": 0,
        "3_of_a_kind": 0,
        "4_of_a_kind": 0,
        "full_house": 0,
        "sm_straight": 0,
        "lg_straight": 0,
        "yahtzee": 0,
        "chance": 0,
    }
    # get counts
    counts = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }
    for die in dice:
        if die == 1:
            counts[1] += 1
        if die == 2:
            counts[2] += 1
        if die == 3:
            counts[3] += 1
        if die == 4:
            counts[4] += 1
        if die == 5:
            counts[5] += 1
        if die == 6:
            counts[6] += 1
    # check lower matches
    scores["aces"] = counts[1] * 1
    scores["twos"] = counts[2] * 2
    scores["threes"] = counts[3] * 3
    scores["fours"] = counts[4] * 4
    scores["fives"] = counts[5] * 5
    scores["sixes"] = counts[6] * 6
    # check higher matches
    if 3 in counts.values() or 4 in counts.values() or 5 in counts.values():
        scores["3_of_a_kind"] = sum(dice)
    if 4 in counts.values() or 5 in counts.values():
        scores["4_of_a_kind"] = sum(dice)
    if 2 in counts.values() and 3 in counts.values():
        scores["full_house"] = 25
    sm_straight_1 = set([1,2,3,4])
    sm_straight_2 = set([2,3,4,5])
    sm_straight_3 = set([3,4,5,6])
    if sm_straight_1.issubset(set(dice)) or sm_straight_2.issubset(set(dice)) or sm_straight_3.issubset(set(dice)):
        scores["sm_straight"] = 30
    lg_straight_1 = set([1,2,3,4,5])
    lg_straight_2 = set([2,3,4,5,6])
    if lg_straight_1.issubset(set(dice)) or lg_straight_2.issubset(set(dice)):
        scores["lg_straight"] = 40
    if 5 in counts.values():
        scores["yahtzee"] = 50
    scores["chances"] = sum(dice)
    return scores