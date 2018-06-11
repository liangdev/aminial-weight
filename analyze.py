import numpy as np
import arrow
import db


birthday_str = '2018-01-01'
date_str_size = len(birthday_str)


def get_days(date_str):
    birthday = arrow.get(birthday_str)
    return (arrow.get(date_str) - birthday).days


def calculate():
    sql = 'select * from animal_weights'
    results = db.select_all(sql)
    dates = [get_days(x['weigh_date'][:date_str_size]) for x in results]
    weights = [float(x['weight']) for x in results]
    x = np.array(dates)
    y = np.array(weights)
    print(x, y)
    A = np.vstack([x, np.ones(len(x))]).T
    a, b = np.linalg.lstsq(A, y, rcond=None)[0]
    return a, b


def estimate_weight(date_str):
    date = date_str[:date_str_size]
    a, b = calculate()
    return round(a * get_days(date) + b, 1)


def animal_health():
    sql = 'select * from animal_weights'
    results = db.select_all(sql)
    total_score = 0
    for result in results:
        expected_weight = estimate_weight(result['weigh_date'][:date_str_size])
        weight = float(result['weight'])
        daily_score = (1 - abs(expected_weight - weight) /
                       expected_weight) * 100
        print(expected_weight, weight, daily_score)
        total_score += daily_score
    health_score = total_score / len(results)
    return health_score
