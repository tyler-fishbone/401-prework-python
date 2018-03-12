## function to translate individual words into pig latin

def pigLatinizeWord():
  pyg = 'ay'
  original = raw_input('Enter a word: ')
  if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:] + first + pyg
    print new_word
  else:
    print 'please input a single word made up only of letters'
    pigLatinizeWord()

pigLatinizeWord()