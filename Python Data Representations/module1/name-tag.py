"""
Problem - 
Write a function make_nametag(name, topic) that takes two strings first_name and topic and returns
the string "Hi! My name is XXX. This lecture covers YYY." where XXX is replaced by first_name and YYY
is replaced by topic.
"""

"""
Solution - Function that uses format to create a nametag
"""


def make_nametag(first_name, topic):
    """
    Given two strings first_name and topic,
    return a string of the form ""Hi! My name 
    is XXX. This lecture covers YYY." where
    XXX and YYY are first_name and topic.
    """
    
    template = "Hi! My name is {0}. This lecture covers {1}."
    return template.format(first_name, topic)
    
# Tests

print(make_nametag("Scott", "Python"))
print(make_nametag("Joe", "games"))
print(make_nametag("John", "programming tips"))


# Output

#Hi! My name is Scott. This lecture covers Python.
#Hi! My name is Joe. This lecture covers games.
#Hi! My name is John. This lecture covers programming tips.