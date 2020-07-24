'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    count = 0
    letters = list(word)
    
    if len(letters) < 2:
        return 0
    elif letters[0] == 't' or letters[0] == 'h':
        count += 1
        
    return count + count_th(letters[1:])
