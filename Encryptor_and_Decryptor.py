#David Bazan 2023


def make_rails(word, num_rail):
  '''
    @param word is a string
    @param num_rail is an integer
    This function will make a list the length of word and for
    each letter in the word make it go up and down a list of rails
  '''
  rows = [*range(num_rail)]  # The number of rails
  rail = []  #This will be the result of make_rails
  is_down = 1  #This variable helps us determine if we are going up or down in the rail number
  row_number = 0  #Also helps us with going up and down

  for character in word:
    rail.append(rows[row_number])
    if row_number == 0:
      #Foward
      is_down = 1
    elif row_number == num_rail - 1:
      #Backward
      is_down = -1

    row_number += is_down

  return rail


def encrypt_rail_fence(message, num_rails):
  '''
  @param message a string
  @param num_rails is an integer
  This function will encrypt message by putting each letter on a rail. 
  num_rail will determine how many rails will the message be on
  '''
  
  row = 0
  is_down = False
  row_list = []
  Box = []
  current_letter = ' '
  message = message.replace(' ', '')
  num = 0
  result = ''

  for elem in enumerate(message):
    row_list.append(' ')


#makes a list filled with each letter in word
  for index in range(num_rails):
    Box.append(row_list.copy())

  for index in range(len(message)):
    current_letter = message[index]

    if row == 0:
      is_down = True
    if row == (num_rails - 1):
      is_down = False

    Box[row][index] = current_letter
    if is_down:
      row += 1
    else:
      row -= 1
    #next step is to print out what is inside of each rail with a space.
  for list in Box:
    num += 1
    for character in list:
      if character != ' ':
        result += character
    if num == len(Box):
      result += ''
    else:
      result += ' '
  return result


def decrypt_rail_fence(message, num_rails):
  '''@param message is a string
  @param num_rails is an integer
  The function decrypts an encrypted message by oranizing it in a box and then reading it in a zig zag manner'''
  row = 0
  is_down = False
  row_list = []
  Box = []
  current_letter = '#'
  message = message.replace(' ', '')
  num = 0
  list = []
  result = ''

  #Makes an empy Box
  for elem in message:
    row_list.append(' ')
  for index in range(num_rails):
    Box.append(row_list.copy())

  #Will make the rail pattern with the placeholder #
  for index in range(len(message)):
    if row == 0:
      is_down = True
    if row == (num_rails - 1):
      is_down = False
    Box[row][index] = current_letter
    if is_down:
      row += 1
    else:
      row -= 1

#We need to replace the place holders with our message
  for index in range(num_rails):
    for elem in range(len(message)):
      if Box[index][elem] == '#':
        Box[index][elem] = message[num]
        num += 1

#We need to read the rails in a zig zag pattern and put it into a list
  row = 0
  for index in range(len(message)):
    if row == 0:
      is_down = True
    if row == (num_rails - 1):
      is_down = False
    if Box[row][index] != ' ':
      list += Box[row][index]
    if is_down:
      row += 1
    else:
      row -= 1

  #make the new list into a string
  for letter in list:
    result += letter

  return result


#print(encrypt_rail_fence("WEATHER IS QUITE NICE TODAY", 2)) Encrypts Message
#print(decrypt_rail_fence("WAHRSUTNCTDY ETEIQIEIEOA", 2)) Decrypts Message
