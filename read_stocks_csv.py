import csv

def get_stocks(csv_name):
    stocks = []
    with open(csv_name, newline='') as fd:
        reader = csv.reader(fd)
        for row in reader:
            stocks.append({'ticker': row[0],
                           'name': row[1],
                           'market_cap': float(row[2]),
                           'sector': row[3]})
    return stocks
