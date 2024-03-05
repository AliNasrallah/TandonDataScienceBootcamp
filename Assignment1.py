'''Ali Nasrallah, Data Science Bootcamp Assignment 1'''

#Number 1: 

def count_vowels(word):
  vowels=('a','e','i','o','u')
  num_vowels=0
  for char in word:
    if char in vowels:
      num_vowels+=1
  return num_vowels


#Number 2: 
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for animal in animals:
  print(animal.upper())

#Number 3:

for i in range(1, 21):
  if i%2==0:
    print(i, " is even.\n")
  else:
    print(i, " is odd.n\")

#Number 4:

def sum_of_integers(a,b):
  return a+b
