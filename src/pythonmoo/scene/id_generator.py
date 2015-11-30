from itertools import count

id_generator = count()


def get_next_id() -> int:
    return next(id_generator)