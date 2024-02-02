import random


def get_random_winners(quantity, participants):
    if quantity > len(participants):
        return []
    ids = list(participants.keys())
    random.shuffle(ids)
    return random.sample(ids, k=quantity)


print(get_random_winners(2, {"ssgf": 3, "dlkjhfg743": 455, "c,vhsfuhg": 42, "ds,fjhdsjgss": 4444, "sdfffffff": 4403}))
