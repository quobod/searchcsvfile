
import re


def is_only_digits(arg):
    results = re.search(r"^([0-9]{1,})$", arg)
    return results != None and results.group()[0:] != None


def is_underscore(arg):
    results = re.search(r"^([_]{1,})$", arg)
    return results != None and results.group()[0:] != None


def is_single_letter(arg):
    results = re.search(r"^([a-zA-Z]{1})$", arg)
    return results != None and results.group()[0:] != None
