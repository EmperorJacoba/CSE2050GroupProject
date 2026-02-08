def truncate_float(num: float, decimal_places: int):
    round_num = 10 ** decimal_places
    return int(num * round_num) / round_num