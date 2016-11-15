"""Grasshopper - Personalized Message
https://www.codewars.com/kata/grasshopper-personalized-message

# Personalized greeting

Create a function that gives a personalized greeting. This function takes two
parameters: `name` and `owner`.

Use conditionals to return the proper message:
case | return
--- | ---
name equals owner | 'Hello boss'
otherwise | 'Hello guest'
"""


def greet(name, owner):
    return 'Hello %s' % ('boss' if name == owner else 'guest')
