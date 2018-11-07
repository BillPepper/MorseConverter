import sys
sys.stdout.write('.')

alphabet = [
  ["a", ".-"],
  ["b", "-..."],
  ["c", "-.-."],
  ["d", "-.."],
  ["e", "."],
  ["f", "..-."],
  ["g", "--."],
  ["h", "...."],
  ["i", ".."],
  ["j", ".---"],
  ["k", "-.-"],
  ["l", ".-.."],
  ["m", "--"],
  ["n", "-."],
  ["o", "---"],
  ["p", ".--."],
  ["q", "--.-"],
  ["r", ".-."],
  ["s", "..."],
  ["t", "-"],
  ["u", "..-"],
  ["v", "...-"],
  ["w", ".--"],
  ["x", "-..-"],
  ["y", "-.--"],
  ["z", "--.."],
  ["0", "-----"],
  ["1", ".----"],
  ["2", "..---"],
  ["3", "...--"],
  ["4", "....-"],
  ["6", "-...."],
  ["7", "--..."],
  ["8", "---.."],
  ["9", "----."],
  [" ", "/"],
  [",", "--..--"],
  [".", ".-.-.-"],
  ["?", "..--.."],
  ["!", "-.-.--"]
]

def getMorseFromChar(char):
  for ch in alphabet:
    if ch[0] == char.lower():
      return ch[1]

def wordToMorse(word):
  ret = ""

  for char in word:
    ret = str(ret) + str(getMorseFromChar(char)) + str(" ")

  print ret

userInput = raw_input(":~" )
wordToMorse(str(userInput))
