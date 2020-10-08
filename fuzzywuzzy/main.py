from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
  
phrase1 = "Tom Brady"
phrase2 = "thomas edward patrick brady jr"
print("FuzzyWuzzy Ratio: {}".format(fuzz.ratio(phrase1, phrase2))) # exact match
print("FuzzyWuzzy PartialRatio: {}".format(fuzz.partial_ratio(phrase1, phrase2))) # partial match
print("FuzzyWuzzy TokenSortRatio: {}".format(fuzz.token_sort_ratio(phrase1, phrase2))) # any order
print("FuzzyWuzzy TokenSetRatio: {}".format(fuzz.token_set_ratio(phrase1, phrase2))) # any quantity of words repeated
print("FuzzyWuzzy WRatio: {} \n".format(fuzz.WRatio(phrase1, phrase2))) # ignore upper and lower cases and extra characters
  
query = 'new england patriots'
choices = ["Atlanta Falcons", "New England Patriots", "New York Giants", "Dallas Cowboys"]
print("List of ratios: ")
print("{}\n".format(process.extract(query, choices)))
print("Best among the above list: {}".format(process.extractOne(query, choices)))