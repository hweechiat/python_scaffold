"""<insert what this script does here>"""


def factorial(x):
    """this function returns the factorial of n"""
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x * factorial(x - 1)
