import pandas as pd


def get_shop_timestring(timestamp):
    # Return timestamp in format expected by Shop
    return timestamp.strftime('%Y%m%d%H%M%S')


def get_shop_datetime(time_string, time_zone_name):
    time_format = '%Y%m%d%H%M%S'
    time_string = time_string[0:14]
    time_string_len = len(time_string)

    # Handle the following cases '%Y%m%d%H%M%S', '%Y%m%d%H%M', %Y%m%d%H' and %Y%m%d'
    missing_digits = 14 - time_string_len
    relevant_time_format_len = len(time_format) - missing_digits

    # Make sure format string does not end with "%". These cases will still fail, but return more intelligible errors
    if relevant_time_format_len % 2 == 1:
        relevant_time_format_len -= 1

    # Return timestamp using format string inferred from input time_string
    relevant_time_format = time_format[0:relevant_time_format_len]
    if len(time_zone_name) > 0:
        timestamp = pd.to_datetime(time_string, format=relevant_time_format, tz = time_zone_name)
    else:
        timestamp = pd.to_datetime(time_string, format=relevant_time_format)
    return timestamp
