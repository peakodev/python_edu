import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    if not cats:
        return []
    if isinstance(cats[0], Cat):
        return [{'nickname': cat.nickname, 'age': cat.age, 'owner': cat.owner} for cat in cats]
    else:
        return [Cat(cat['nickname'], cat['age'], cat['owner']) for cat in cats]









