from functools import lru_cache
from itertools import permutations
from dictionary import Dictionary
import sys


@lru_cache(maxsize=None)
def vocabulary(filename):
  with open(filename, 'r') as f:
    return {word.strip() for word in f}


def leading_words(text, vocab):
  '''Returns all possible words from vocab that text starts with.'''
  text = text.strip()
  for i in range(len(text)):
    match = vocab.partial_match(text[:i+1])
    if not match:
      return ''
    elif match.isword:
      yield prefix


def break_words(text, vocab):
  '''Partition text to words defined in vocab.'''
  text = text.strip()
  results = set()
  def add_results(text_left, words=''):
    if not text_left:
      results.add(words.strip())
    else:
      for word in leading_words(text_left, vocab):
        add_results(text_left[len(word):], '{} {}'.format(words, word))
  add_results(text)
  return results


def main(argv):
  # vocab = vocabulary('5000-words.txt')
  # vocab = Dictionary(vocab)
  # vocab.print()

  vocab = Dictionary(['the', 'a', 'are', 'army'])
  print(vocab.partial_match('ar'))
  print(vocab.partial_match('are'))
  print(vocab.partial_match('army'))
  print(vocab.partial_match('ac'))

  code = argv[1].replace(' ', '')
  anagrams = map(''.join, permutations(code))

  # for anagram in anagrams:
  #   print(anagram)
  #   phrases = break_words(anagram, vocab)
  #   if phrases:
  #     print(phrases)

if __name__ == '__main__':
  main(sys.argv)
