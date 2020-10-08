# SHELL
# import nltk
# nltk.download('machado')
# nltk.download('stopwords')

from nltk.corpus import machado
from nltk.text import Text

book = Text(machado.words('romance/marm08.txt'), name="Dom Casmurro (1899)")
print("book's name:", book.name)

# to give context for a given word
book.concordance('olhos')
print('\n')

# a list of words that appear in the same context
book.similar('chegar')
print('\n')

# words that often appear consecutively
book.collocations()
print('\n')