import sys
from datetime import date, datetime, time


def usage():
    print(f"Usage: {sys.argv[0]} <csv_file> -d \"yyyy-mm-dd\"")


# This Checks to see if arguments are given or not
if len(sys.argv) != 4 or sys.argv[2] != '-d':
    usage()
    exit(1)


# Dictionary stores each cookie and number of occurrences
cookies_occurrences = {}

# This Opens file cookie_log.csv in read mode
cookie_log = open(sys.argv[1], "r")

# Convert second given date into datetime object
date_time = datetime.strptime(sys.argv[3], "%Y-%m-%d")

# Loop to read data line by line
for line in cookie_log.readlines():
    cookie, timestamp = line.split(",")
    timestamp = timestamp.replace("\n", "")
    # Convert timestamp into datetime object
    tmp_datetime = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S%z')
    if date_time.strftime('%Y-%m-%d') == tmp_datetime.strftime('%Y-%m-%d'):
        # If the key (cookie) is already exists the increment the count by 1
        if cookie in cookies_occurrences:
            cookies_occurrences[cookie] += 1
        else:
            # If the key (cookie) is not present then add the cookie with value 1
            cookies_occurrences[cookie] = 1


# This gets the maximum value in the dictionary cookies_occurrences
max_occurred = max(cookies_occurrences.values(), key= lambda x: x)

# This Prints the cookie(s) that has the highest occurrence
for cookie, occurrences in cookies_occurrences.items():
    if occurrences == max_occurred:
        print(cookie)

# File closing
cookie_log.close()