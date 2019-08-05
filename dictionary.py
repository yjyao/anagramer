from collections import defaultdict
from functools import namedtuple

class Dictionary(object):
  '''Build a trie dictionary out of words defined in vocab.'''

  Match = namedtuple('Match', 'prefix isword prefix_words')

  def __init__(self, vocab=None):
    defaultdict_maker = lambda: defaultdict(defaultdict_maker)
    self._prefix_tree = defaultdict(defaultdict_maker)
    self.extend(vocab or [])

  def add(self, word):
    it = self._prefix_tree
    for ch in word:
      it = it[ch]
    it[''] = True

  def extend(self, words):
    for word in words:
      self.add(word)

  def partial_match(self, text):
    return Match()

  def prefix_words(self, text):
    it = self._prefix_tree
    for i, ch in enumerate(text):
      it = it.get(ch, None)
      if it is None:
        break
      if '' in it:
        yield text[:i+1]

  def isword(self, word):
    match = self.partial_match(word)
    return match is not None and match.isword

  def print(self):
    def print_dictionary(it=self, i=0):
      for k, v in it.items():
        if v is True:
          print('{}EOW'.format(' '*i*2))
        else:
          print('{}{}:'.format(' '*i*2, k))
          print_dictionary(v, i+1)
    print_dictionary()


