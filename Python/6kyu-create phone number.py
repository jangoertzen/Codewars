"""
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
"""

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)