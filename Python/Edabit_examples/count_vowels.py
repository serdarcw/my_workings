# Bir kelimenin içerisindeki sesli harfleri bulmak için kullanılır


def count_vowels(txt):
  return sum([1 for x in txt.lower() if x in 'aeiou'])



  
def count_vowels(txt):
  return sum(c in "aeiou" for c in txt)



def count_vowels(txt):
  vowels = "aeiou"
  num_vow = 0
  for i in txt:
    if i in vowels:
      num_vow += 1
  return num_vow


def count_vowels(txt):
	sum = 0
	sum += txt.count('a')
	sum += txt.count('e')
	sum += txt.count('i')
	sum += txt.count('o')
	sum += txt.count('u')
	return sum


def count_vowels(txt):
	return len([letter for letter in txt if letter.lower() in 'aeiou'])



  
  