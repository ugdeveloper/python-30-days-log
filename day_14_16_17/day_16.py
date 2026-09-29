## Day 16- 30DaysOfPythonChallenge

## Exercises

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module

from datetime import datetime, date

now = datetime.now()

timestamp = now.timestamp()

# 2. Format the current date using this format "%m/%d/%Y, %H:%M:%S"

t = now.strftime("%m/%d/%Y, %H:%M:%S")
print(t)

# 3. Today is 5 December, 2019. Change this time string to time.

date_string = "5 December, 2019"

time = datetime.strptime(date_string, "%d %B, %Y")

print(time)

# 4. Calculate the time difference between now and new year

now = date(year=2026, month=9, day=28)
ny = date(2027, month=1, day=1)

print(ny - now)

# 5. Calculate the time difference between 1 January 1970 and now.

then = date(year=1970, month=1, day=1)

print(now - then)

# 6. Think what you can use the datetime modules for:
    # Time series analysis
    # Timestamp of activities in application
    # adding posts on blog
    # In application time
    # Countdown
    # Data analysis with time as x-axis
    
