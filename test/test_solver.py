
rolls = {
    "EARLY": [2,1,4,3,5],
    "IDIOM": [2,3,2,3,3],
    "CORES": [2,3,4,2,3],
    "MACAW": [3,1,2,1,4],
    "DRONE": [3,4,3,4,2],
    "PENNY": [4,2,4,4,5],
    "STICK": [3,4,2,2,2],
    "ROOMS": [4,3,3,3,3],
    "EAVES": [2,1,4,2,3],
    "URBAN": [3,4,2,1,4],
    "BURQA": [2,3,4,5,1],
    "SLUSH": [3,3,3,3,3],
    "YOLKS": [5,3,3,2,3],
}

for roll in rolls:
    dice = rolls[roll]
    scores = score(dice)
    print(f"Scoring {roll} with {dice}")
    scores_sorted = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}
    print(scores_sorted)
    print("\n\n\n\n\n")
