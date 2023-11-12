# Carliana Roland 2/10/23 Comp163

# In this assignment you are to remove any vowel and double consonants.
vowel = ['a', 'e', 'i', 'o', 'u', 'y']
# The list below will be used to get rid of the double consonants.
alpha = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
vowel_dict = {}
phrase = input('Enter phrase here: ')
for v in vowel:
    vowel_dict[v] = 0
for i in phrase:
    if i in vowel:
        phrase = phrase.replace(i, '')
        vowel_dict[i] += 1
# This last for loop is going run the double consonants in the phrase and replace them with a closed space.
for i in alpha:
    if i in phrase:
        phrase = phrase.replace(i, '')
print(phrase.lower())
print(vowel_dict)
