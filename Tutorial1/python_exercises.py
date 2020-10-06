"""
Intro to python exercises shell code
"""

def is_odd(x):
    if x%2 == 1:
        return True
    else:
        return False

def is_palindrome(word):
    for i in range(0, int(len(word)/2)):
        if(word[i] != word[len(word) - 1 -i]):
            return False
    return True


def only_odds(numlist):
    new_list = []
    for i in range(0,len(numlist)):
        if(numlist[i] %2 == 1):
            new_list.append(numlist[i])
    return new_list


def count_words(text):
    word_list = text.split(' ')
    d = {}
    for i in range(0,len(word_list)):
        count = 0
        for j in range(0,len(word_list)):
            if(word_list[i] == word_list[j]):
                count = count + 1
        d[word_list[i]] = count
    return d