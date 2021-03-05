def search4vowels(phrase:str) -> set:
    '''Display any vowels found in a supplied phrase.'''
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

print(search4vowels('christmas'))


def search4letters(phrase:str, letters:str) -> set:
    '''return a set of the 'letters' found in 'phrase'.'''
    return set(letters).intersection(set(phrase))

search4letters('hitch-hiker', 'aeiou')

search4letters('galaxy', 'xyz')

search4letters('life, the universe, and everything', 'o')