def date_format(date_string):
    month, day, year = date_string.split('/')
    return f"{year}-{int(month):02d}-{int(day):02d}"