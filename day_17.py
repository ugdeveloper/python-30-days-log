## day 17 - 30 days of python challenge

# Exercises day 17

# 1. names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

try:
    names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

    names.reverse()

    ru, es, *rest = names
    print(rest, ru, es)
except Exception as e:
    print(e)