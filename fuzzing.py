from difflib import SequenceMatcher

text_1 = input('Text 1: ')
text_2 = input('Text 2: ')

print('Match: {}'.format(SequenceMatcher(None, text_1, text_2).ratio()))
