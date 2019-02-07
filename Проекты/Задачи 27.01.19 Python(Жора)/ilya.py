import string
from time import time,sleep
start=time()
def word_letter_counter( text_string):
      """Returns tuple with number of letters and number of words in text_string."""
      # YOUR CODE HERE
      isInWord = False
      text_string+=" "
      letters = 0
      words = 0
      i = skipSpaces(text_string,0)
      sleep(1)
      while(i < len(text_string)):
          if(text_string[i] in string.whitespace):
            if(isInWord):
              words+=1
              isInWord = False
              i = skipSpaces(text_string, i)
              continue
          if(text_string[i] in string.punctuation):
            i+=1
            continue
          if(text_string[i] in string.ascii_letters):
            i+=1
            isInWord = True
            letters+=1
  
      return letters, words
def skipSpaces( text_string ,i):
      while(i < len(text_string) and text_string[i] not in string.ascii_letters):
          i+=1
      return i
print(word_letter_counter("Hi\tThere\n"))
end = time()
print(end-start)

    
