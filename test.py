import arrow

hour = arrow.now().to('PST').floor('hour')

print(hour)
