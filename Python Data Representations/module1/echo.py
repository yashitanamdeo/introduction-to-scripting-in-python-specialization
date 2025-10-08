"""
Problem - 
Write a function echo(call, repeats) that takes a string call and an integer repeats and prints 
repeats copies of the string call to console, each on a separate line. Do not not use a loop for 
this problem. Instead, use string muplication and the new line character '\n'.
"""

"""
Solution - Echo a string multiple times to the console
"""

def echo(call, repeats):
    """
    Echo the string call to the console repeats number of time
    Each echo should be on a separate line
    """
    answer = call + ('\n' + call) * (repeats - 1)
    print(answer)


# Tests
echo("Hello", 5)
echo("Goodbye", 3)

# Output
#Hello
#Hello
#Hello
#Hello
#Hello
#Goodbye
#Goodbye
#Goodbye