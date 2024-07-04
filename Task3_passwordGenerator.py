#!/usr/bin/env python
# coding: utf-8

# In[2]:


import string
import random

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for password from these : 
		1. Digits
		2. Letters
		3. Special characters
		4. Exit''')

characterList = ""

# Getting character set for password
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		
		# Adding letters to possible characters
		characterList += string.ascii_letters
	elif(choice == 2):
		
		# Adding digits to possible characters
		characterList += string.digits
	elif(choice == 3):
		
		# Adding special characters to possible
		# characters
		characterList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please pick a valid option!")

password = []

for i in range(length):

	# Picking a random character from our 
	# character list
	randomchar = random.choice(characterList)
	
	# appending a random character to password
	password.append(randomchar)

# printing password as a string
print("The random password is " + "".join(password))


# In[3]:


import string
import random

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for password from these : 
		1. Digits
		2. Letters
		3. Special characters
		4. Exit''')

characterList = ""

# Getting character set for password
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		
		# Adding letters to possible characters
		characterList += string.ascii_letters
	elif(choice == 2):
		
		# Adding digits to possible characters
		characterList += string.digits
	elif(choice == 3):
		
		# Adding special characters to possible
		# characters
		characterList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please pick a valid option!")

password = []

for i in range(length):

	# Picking a random character from our 
	# character list
	randomchar = random.choice(characterList)
	
	# appending a random character to password
	password.append(randomchar)

# printing password as a string
print("The random password is " + "".join(password))


# In[4]:


import string
import random

# Vartika Singh
# Task 2

print("Welcome to random password generator"):
len = int(input("Enter password length: "))

print('''Choose character set for password from these : 
1. Digits
2. Letters
3. Special characters
4. Exit''')

characterList = ""

# Getting character set for password
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		charList += string.ascii_letters
	elif(choice == 2):
		
		# Adding digits to possible characters
		charList += string.digits
	elif(choice == 3):
		
		# Adding special characters to possible
		# characters
		charList += string.punctuation
elif(choice == 4):
break
else:
print("Chosen option is not valid. Please pick a valid option!")

pswd = []

for i in range(length):

	# Picking a random character from our 
	# character list
	randchar = random.choice(charList)
	
	# appending a random character to password
	password.append(randchar)

# printing password as a string
print("The random password is " + "".join(pswd))


# In[5]:


import string
import random

# Vartika Singh
# Task 2

print("Welcome to random password generator")
len = int(input("Enter password length: "))

print('''Choose character set for password from these : 
1. Digits
2. Letters
3. Special characters
4. Exit''')

characterList = ""

# Getting character set for password
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		charList += string.ascii_letters
	elif(choice == 2):
		
		# Adding digits to possible characters
		charList += string.digits
	elif(choice == 3):
		
		# Adding special characters to possible
		# characters
		charList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Chosen option is not valid. Please pick a valid option!")

pswd = []

for i in range(length):

	# Picking a random character from our 
	# character list
	randchar = random.choice(charList)
	
	# appending a random character to password
	password.append(randchar)

# printing password as a string
print("The random password is " + "".join(pswd))


# In[7]:


import string
import random

# Vartika Singh
# Task 2

print("Welcome to random password generator")
len = int(input("Enter password length: "))

print('''Choose character set for password from these : 
1. Digits
2. Letters
3. Special characters
4. Exit''')

charList = ""

# Getting character set for password
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		charList += string.ascii_letters
	elif(choice == 2):
		
		# Adding digits to possible characters
		charList += string.digits
	elif(choice == 3):
		
		# Adding special characters to possible
		# characters
		charList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Chosen option is not valid. Please pick a valid option!")

pswd = []

for i in range(length):

	# Picking a random character from our 
	# character list
	randchar = random.choice(charList)
	
	# appending a random character to password
	pswd.append(randchar)

# printing password as a string
print("The random password is " + "".join(pswd))


# In[9]:


import string
import random

# Vartika Singh
# Task 2

print("Welcome to random password generator program")
len = int(input("Enter password length: "))

print('''Choose character set for password from these : 
1. Digits
2. Letters
3. Special characters
4. Exit''')

charList = ""

# Getting character set for password
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		charList += string.ascii_letters
	elif(choice == 2):
		
		# Adding digits to possible characters
		charList += string.digits
	elif(choice == 3):
		
		# Adding special characters to possible
		# characters
		charList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Chosen option is not valid. Please pick a valid option!")

pswd = []

for i in range(length):

	# Picking a random character from our 
	# character list
	randchar = random.choice(charList)
	
	# appending a random character to password
	pswd.append(randchar)

# printing password as a string
print("The random password is " + "".join(pswd))


# In[ ]:


import string
import random

# Vartika Singh
# Task 2

print("Welcome to random password generator program")
len = int(input("Enter password length: "))

print('''Choose character set for password from these : 
1. Digits
2. Letters
3. Special characters
4. Exit''')

charList = ""

# Getting character set for password
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		charList += string.ascii_letters
	elif(choice == 2):
		
		# Adding digits to possible characters
		charList += string.digits
	elif(choice == 3):
		
		# Adding special characters to possible
		# characters
		charList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Chosen option is not valid. Please pick a valid option!")

pswd = []

for i in range(length):

	# Picking a random character from our 
	# character list
	randchar = random.choice(charList)
	
	# appending a random character to password
	pswd.append(randchar)

# printing password as a string
print("The random password is " + "".join(pswd))


# In[10]:


import string
import random

# Vartika Singh
# Task 2

print("Welcome to random password generator program")
len = int(input("Enter password length: "))

print('''Choose character set for password from these : 
1. Digits
2. Letters
3. Special characters
4. Exit''')

charList = ""

# Getting character set for password
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		charList += string.ascii_letters
	elif(choice == 2):
		
		# Adding digits to possible characters
		charList += string.digits
	elif(choice == 3):
		
		# Adding special characters to possible
		# characters
		charList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Chosen option is not valid. Please pick a valid option!")

pswd = []

for i in range(length):

	# Picking a random character from our 
	# character list
	randchar = random.choice(charList)
	
	# appending a random character to password
	pswd.append(randchar)

# printing password as a string
print("The random password is " + "".join(pswd))


# In[ ]:




