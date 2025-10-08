"""
Problem - 
Pig Latin is a language game that involves altering words via a simple set of rules. 
Write a Python function pig_latin that takes a string word and applies the following rules to 
generate a new word in Pig Latin. If the first letter in word is a consonant, append the 
consonant plus "ay" to the end of the remainder of the word. For example, pig_latin("pig") would return
"igpay". If the first letter in word is a vowel, append "way" to the end of the word. For example,
pig_latin("owl") would return "owlway". You can assume that word is in lower case. 
The provided template includes code to extract the first letter and the rest of word in Python. 
Note that, in full Pig Latin, the leading consonant cluster is moved to the end of the word. 
However, we don't know enough Python to implement full Pig Latin just yet.
"""

"""
Solution - Compute a (simplified) Pig Latin version of a word.
"""

###################################################
# Pig Latin function
def pig_latin(word):
    """
    Returns the (simplified) Pig Latin version of the word.
    """
    
    # Partial code for body
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    # Student should complete function on the next lines.
    if (first_letter == "a" or first_letter == "e" or first_letter == "i" or
        first_letter == "o" or first_letter == "u"):
        return word + "way"
    else:
        return rest_of_word + first_letter + "ay"


###################################################
# Tests
    
word = "pig"
print(pig_latin(word))

word = "owl"
print(pig_latin(word))

word = "python"
print(pig_latin(word))

###################################################
# Expected output

#igpay
#owlway
#ythonpay
