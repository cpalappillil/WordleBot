import math

words_list = open(r'sgb-words.txt', "r")
words = words_list.readlines()

class WordleBOT():
  def __init__(self, word_list):
    self.words = word_list
    self.possible_solutions = word_list

  def check_word(self, word, guess, result):
    """
    Given a guess and result array, checks if given word is a possible answer

    output: boolean true/false response indicated whether given word is possible solution to wordle

    """
    for i in range(len(result)):
      if (result[i] == 0): #char at position i not in string
        if guess[i] in word: #checks if gray character is in string
          return False
      if (result[i] == 1): #char in string, but not at position i
        if guess[i] not in word: #checks if char not in string
          return False
        if (word[i] == guess[i]): #char in wrong index
          return False
      if (result[i] == 2): #char at position i is correct
        if word[i] != guess[i]:
          return False #char at position 1 is incorrect, hence word is not an answer
    return True
  
  def find_solutions(self, guess, result):
    """
    Searches through entire word list to filter possible results
    complexity: O(n)
    """
    possible_words = []
    for word in self.possible_solutions:
      if(self.check_word(word, guess, result)):
        possible_words.append(word)
    self.possible_solutions = possible_words

  def scrabble_score(self, word):
    """
    Assigns scrabble score to input word
    Returns integer
    """
    score = 0
    for char in word:
      if char in ["a", "e", "i", "l", "n", "o", "r", "s", "t", "u"]:
        score += 1
      elif char in ["d", "g"]:
        score += 2
      elif char in ["b", "c", "m", "p"]:
        score += 3
      elif char in ["f", "h", "v", "w", "y"]:
        score += 4
      elif char in ["k"]:
        score += 5
      elif char in ["j", "x"]:
        score += 8
      elif char in ["q", "z"]:
        score += 10
    return score

  def unique_char_score(self, word):
    """
    assigns score to word based on number of unique letters
    """
    return -(len(set(word)))*3 + 15
  
  def freq_score(self, index):
    """
    assigns score to word based on frequency (order in list)
    """
    list_len = len(self.possible_solutions)
    return (index/list_len * 20)

  def guess(self):
    # Idea 1: Priortize guesses based on lowest scrabble score
    assert (len(self.possible_solutions) > 0), "no results found!"
    scores = []
    output = ""
    for i in range(len(self.possible_solutions)):
      word = self.possible_solutions[i]
      scores.append(self.scrabble_score(word) + self.unique_char_score(word) + self.freq_score(i))
    # find lowest (best) score
    min_score = 100
    for j in range(len(scores)):
      score = scores[j]
      if score < min_score:
        min_score = score
        output = self.possible_solutions[j]
    return output

wg = WordleBOT(words)

for i in range(6):
  suggested_guess = wg.guess()
  print("suggested guess: " + suggested_guess)
  confidence = int(1/len(wg.possible_solutions) * 100)
  print("confidence: " + str(confidence) + "%")
  guess = input("guess: ")
  result = list(input("enter result: "))
  print("____________________________________________________")
  for i in range(len(result)):
    result[i] = int(result[i])
  wg.find_solutions(guess, result)






      

    