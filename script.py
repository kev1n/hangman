from random_words import RandomWords

rw = RandomWords()
hangman_word = rw.random_word()
hangman_list = []
for letter in hangman_word:
    hangman_list.append(letter)

x = len(hangman_word)
underscored = ['_', '_','_', '_','_', '_','_', '_','_', '_','_', '_','_', '_','_', '_','_', '_','_', '_','_', '_','_', '_','_', '_','_', '_','_', '_','_', '_','_', '_','_', '_',][0:x]

trys = 6
hangmanztry0 = """
 o
-|-
 /|
"""
hangmanztry1 = """
 
-|-
 /|
"""
hangmanztry2 = """
 
-|
 /|
"""
hangmanztry3 = """
 
 |
 /|
"""
hangmanztry4 = """
 
 
 /|
"""
hangmanztry5 = """
 
 
 |
"""
print(underscored)
letter1 = input("""What first letter?
""")
if letter1 in hangman_word:
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = hangman_list.index(letter1, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    for index in index_pos_list:
        underscored[index] = letter1
        print(underscored)
        x -= 1
else:
  trys -= 1
  print("No such letter. " + str(trys) + " attempts left.")

if x == 0:
  print("You won")
  exit()

if trys == 0:
	print("You ran out of trys!")
	print(hangmanztry0)

if trys == 1:
	print(hangmanztry1)

if trys == 2:
	print(hangmanztry2)

if trys == 3:
	print(hangmanztry3)

if trys == 4:
	print(hangmanztry4)

if trys == 5:
	print(hangmanztry5)



letter2 = input("""What second letter?
""")
if letter2 in hangman_word:
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = hangman_list.index(letter2, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    for index in index_pos_list:
        underscored[index] = letter2
        print(underscored)
        x -= 1
else:
  trys -= 1
  print("No such letter. " + str(trys) + " attempts left.")
if x == 0:
	print("You won")
	exit()
if trys == 0:
	print("You ran out of trys!")
	print(hangmanztry0)

if trys == 1:
	print(hangmanztry1)

if trys == 2:
	print(hangmanztry2)

if trys == 3:
	print(hangmanztry3)

if trys == 4:
	print(hangmanztry4)

if trys == 5:
	print(hangmanztry5)

letter3 = input("""What third letter?
""")
if letter3 in hangman_word:
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = hangman_list.index(letter3, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    for index in index_pos_list:
        underscored[index] = letter3
        print(underscored)
        x -= 1
else:
  trys -= 1
  print("No such letter. " + str(trys) + " attempts left.")
if x == 0:
  print("You won")
  exit()
if trys == 0:
	print("You ran out of trys!")
	print(hangmanztry0)

if trys == 1:
	print(hangmanztry1)

if trys == 2:
	print(hangmanztry2)

if trys == 3:
	print(hangmanztry3)

if trys == 4:
	print(hangmanztry4)

if trys == 5:
	print(hangmanztry5)

letter4 = input("""What fourth letter?
""")
if letter4 in hangman_word:
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = hangman_list.index(letter4, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    for index in index_pos_list:
        underscored[index] = letter4
        print(underscored)
        x -= 1
else:
  trys -= 1
  print("No such letter. " + str(trys) + " attempts left.")
if x == 0:
  print("You won")
  exit()
if trys == 0:
	print("You ran out of trys!")
	print(hangmanztry0)

if trys == 1:
	print(hangmanztry1)

if trys == 2:
	print(hangmanztry2)

if trys == 3:
	print(hangmanztry3)

if trys == 4:
	print(hangmanztry4)

if trys == 5:
	print(hangmanztry5)
letter5 = input("""What fifth letter?
""")

if letter5 in hangman_word:
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = hangman_list.index(letter5, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    for index in index_pos_list:
        underscored[index] = letter5
        print(underscored)
        x -= 1
else:
  trys -= 1
  print("No such letter. " + str(trys) + " attempts left.")
if x == 0:
  print("You won")
  exit()
if trys == 0:
	print("You ran out of trys!")
	print(hangmanztry0)

if trys == 1:
	print(hangmanztry1)

if trys == 2:
	print(hangmanztry2)

if trys == 3:
	print(hangmanztry3)

if trys == 4:
	print(hangmanztry4)

if trys == 5:
	print(hangmanztry5)

letter6 = input("""What sixth letter?
""")
if letter6 in hangman_word:
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = hangman_list.index(letter6, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    for index in index_pos_list:
        underscored[index] = letter6
        print(underscored)
        x -= 1
else:
    trys -= 1
    print("No such letter. " + str(trys) + " attempts left.")
if x == 0:
  print("You won")
  exit()
if trys == 0:
	print("You ran out of trys!")
	print(hangmanztry0)

if trys == 1:
	print(hangmanztry1)

if trys == 2:
	print(hangmanztry2)

if trys == 3:
	print(hangmanztry3)

if trys == 4:
	print(hangmanztry4)

if trys == 5:
	print(hangmanztry5)

letter7 = input("""What seventh letter?
""")
if letter7 in hangman_word:
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = hangman_list.index(letter7, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    for index in index_pos_list:
        underscored[index] = letter7
        print(underscored)
        x -= 1
else:
  trys -= 1
  print("No such letter. " + str(trys) + " attempts left.")
if x == 0:
  print("You won")
  exit()
if trys == 0:
	print("You ran out of trys!")
	print(hangmanztry0)

if trys == 1:
	print(hangmanztry1)

if trys == 2:
	print(hangmanztry2)

if trys == 3:
	print(hangmanztry3)

if trys == 4:
	print(hangmanztry4)

if trys == 5:
	print(hangmanztry5)

letter8 = input("""What eighth letter?
""")
if letter8 in hangman_word:
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = hangman_list.index(letter8, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    for index in index_pos_list:
        underscored[index] = letter8
        print(underscored)
        x -= 1
else:
  trys -= 1
  print("No such letter. " + str(trys) + " attempts left.")
if x == 0:
  print("You won")
  exit()
if trys == 0:
	print("You ran out of trys!")
	print(hangmanztry0)

if trys == 1:
	print(hangmanztry1)

if trys == 2:
	print(hangmanztry2)

if trys == 3:
	print(hangmanztry3)

if trys == 4:
	print(hangmanztry4)

if trys == 5:
	print(hangmanztry5)

letter9 = input("""What ninth letter?
""")
if letter9 in hangman_word:
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = hangman_list.index(letter9, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    for index in index_pos_list:
        underscored[index] = letter9
        print(underscored)
        x -= 1
else:
  trys -= 1
  print("No such letter. " + str(trys) + " attempts left.")
if x == 0:
  print("You won")
  exit()
if trys == 0:
	print("You ran out of trys!")
	print(hangmanztry0)

if trys == 1:
	print(hangmanztry1)

if trys == 2:
	print(hangmanztry2)

if trys == 3:
	print(hangmanztry3)

if trys == 4:
	print(hangmanztry4)

if trys == 5:
	print(hangmanztry5)

letter10 = input("""What tenth letter?
""")
if letter10 in hangman_word:
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = hangman_list.index(letter10, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    for index in index_pos_list:
        underscored[index] = letter10
        print(underscored)
        x -= 1
else:
  trys -= 1
  print("No such letter. " + str(trys) + " attempts left.")
if x == 0:
  print("You won")
  exit()
if trys == 0:
	print("You ran out of trys!")
	print(hangmanztry0)

if trys == 1:
	print(hangmanztry1)

if trys == 2:
	print(hangmanztry2)

if trys == 3:
	print(hangmanztry3)

if trys == 4:
	print(hangmanztry4)

if trys == 5:
	print(hangmanztry5)









        
    


