#!/usr/bin/env python
# coding: utf-8

# In[2]:


names = []
phone_numbers = []
num = 3


for i in range(num):
    name = input("Name: ")
    phone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))

    names.append(name)
    phone_numbers.append(phone_number)

print("\nName\t\t\tPhone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("Name: {}, Phone Number: {}".format(search_term, phone_number))

else:
    print("Name Not Found")


# In[3]:


names = []
phone_numbers = []
num = 5


for i in range(num):
    name = input("Name: ")
    phone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))

    names.append(name)
    phone_numbers.append(phone_number)

print("\nName\t\t\tPhone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("Name: {}, Phone Number: {}".format(search_term, phone_number))

else:
    print("Name Not Found")


# In[ ]:


names = []
phone_numbers = []
address=[]
num = 3


for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
ContactAddress=input("Address:")
    names.append(name)
    phone_numbers.append(phone_number)
    address.append(ContactAddress)

print("\nName\t\t\tPhone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i], address[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    ContactAddress=address[index]
    print("Name: {}, Phone Number: {}, Address: {}".format(search_term, phone_number, ContactAddress))

else:
    print("Name Not Found")


# In[ ]:





# In[4]:


names = []
phone_numbers = []
address=[]
num = 3


for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    names.append(name)
    phone_numbers.append(phone_number)
    address.append(ContactAddress)

print("\nName\t\t\tPhone Number\n\t\tAddress\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i], address[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    Contact_address=address[index]
    print("Name: {}, Phone Number: {}, Address: {}".format(search_term, phone_number, Contact_address))

else:
    print("Name Not Found")


# In[5]:


names = []
phone_numbers = []
address=[]
num = 3


for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    names.append(name)
    phone_numbers.append(phone_number)
    address.append(Contact_address)

print("\nName\t\t\tPhone Number\n\t\tAddress\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i], address[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    Contact_address=address[index]
    print("Name: {}, Phone Number: {}, Address: {}".format(search_term, phone_number, Contact_address))

else:
    print("Name Not Found")


# In[6]:


names = []
phone_numbers = []
address=[]
num = 3


for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    names.append(name)
    phone_numbers.append(phone_number)
    address.append(Contact_address)

print("\nName\t\t\tPhone Number\t\tAddress\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], address[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    Contact_address=address[index]
    print("Name: {}, Phone Number: {}, Address: {}".format(search_term, phone_number, Contact_address))

else:
    print("Name Not Found")


# In[ ]:





# In[7]:


def is_valid_email(email):
    # Regular expression pattern for basic email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)


names = []
phone_numbers = []
address=[]
email=[]
num = 3



    

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    Contactemail = input("Enter your email address: ").strip()
    
    if is_valid_email(email):
        print(f"Thank you! '{email}' is a valid email address.")
    else:
        print(f"Sorry, '{email}' is not a valid email address.")
     email.append(Contactemail)
        print("\nName\t\t\tPhone Number\t\tAddress\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")


# In[8]:


names = []
phone_numbers = []
address=[]
num = 3


for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)

print("\nName\t\t\tPhone Number\t\tAddress\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], address[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    print("Name: {}, Phone Number: {}, Address: {}".format(search_term, Contactphone_number, Contact_address))

else:
    print("Name Not Found")


# In[24]:


def is_valid_email(Contactemail):
    # Regular expression pattern for basic email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, Contactemail)

names = []
phone_numbers = []
address=[]
email=[]
num = 3

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    email.append(Contactemail)
    if is_valid_email(Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
     
    print("\nName\t\t\tPhone Number\t\tAddress\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")


# In[ ]:





# In[ ]:





# In[ ]:


import re

names = []
phone_numbers = []
address=[]
email=[]
num = 3

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        email.append(Contactemail)
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    print("\nName\t\t\tPhone Number\t\tAddress\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")


# In[ ]:





# In[ ]:


import re

names = []
phone_numbers = []
address=[]
email=[]
num = 3

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        email.append(Contactemail)
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    
print("\nName\t\t\tPhone Number\t\tAddress\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")


# In[ ]:


import re

names = []
phone_numbers = []
address=[]
email=[]
num = 3

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        email.append(Contactemail)
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    
print("\nName\t\t\tPhone Number\t\tAddress\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")


# In[ ]:





# In[5]:


import re

names = []
phone_numbers = []
address=[]
email=[]
num = input("enter number of contacts you want to add:")

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        email.append(Contactemail)
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    
print("\nName\t\t\tPhone Number\t\t\tAddress\t\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")


# In[ ]:





# In[7]:


import re

names = []
phone_numbers = []
address=[]
email=[]
num = int(input("enter number of contacts you want to add:"))

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        email.append(Contactemail)
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    
print("\nName\t\t\tPhone Number\t\t\tAddress\t\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")


# In[ ]:





# In[8]:


import re

names = []
phone_numbers = []
address=[]
email=[]
num = input("enter number of contacts you want to add:")

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        email.append(Contactemail)
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    
print("\nName\t\t\tPhone Number\t\t\tAddress\t\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")


# In[9]:


import re

names = []
phone_numbers = []
address=[]
email=[]
num = input("enter number of contacts you want to add:")

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        email.append(Contactemail)
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    
print("\nName\t\t\tPhone Number\t\t\tAddress\t\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")


# In[18]:


import re


def update_contact(uname, update):
    if uname in names:
        names[uname] = update
        print(f"Contact '{uname}' updated with new name '{update}'.")
    else:
        print(f"Contact '{uname}' not found.")

def delete_contact(dname):
    if dname in names:
        del names[dname]
        print(f"Contact '{dname}' deleted.")
    else:
        print(f"Contact '{dname}' not found.")
        
names = []
phone_numbers = []
address=[]
email=[]
num = int(input("enter number of contacts you want to add:"))

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    email.append(Contactemail)
    
print("\nName\t\t\tPhone Number\t\t\tAddress\t\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")
    
print("Enter Contact name you want to update: ")
uname=input("Name:")
update=input("Enter name to update or number to update:")
update_contact(uname, update)
print("Enter Contact name you want to delete: ")
dname=input("Name:")
delete_contact(dname)
print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))


# In[ ]:





# In[ ]:


import re


def update_contact(uname, update):
    if uname in names:
        names[uname] = update
        print(f"Contact '{uname}' updated with new name '{update}'.")
    else:
        print(f"Contact '{uname}' not found.")

def delete_contact(dname):
    if dname in names:
        del names[dname]
        print(f"Contact '{dname}' deleted.")
    else:
        print(f"Contact '{dname}' not found.")
        
names = []
phone_numbers = []
address=[]
email=[]
num = int(input("enter number of contacts you want to add:"))

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    email.append(Contactemail)
    
print("\nName\t\t\tPhone Number\t\t\tAddress\t\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")
    
print("Enter Contact name you want to update: ")
uname=input("Name:")
update=input("Enter name to update or number to update:")
update_contact(uname, update)
print("Enter Contact name you want to delete: ")
dname=input("Name:")
delete_contact(dname)
print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))


# In[ ]:





# In[19]:


import re


def update_contact(uname, update):
    if uname in names:
        names[uname] = update
        print(f"Contact '{uname}' updated with new name '{update}'.")
    else:
        print(f"Contact '{uname}' not found.")

def delete_contact(dname):
    if dname in names:
        del names[dname]
        print(f"Contact '{dname}' deleted.")
    else:
        print(f"Contact '{dname}' not found.")
        
names = []
phone_numbers = []
address=[]
email=[]
num = int(input("enter number of contacts you want to add:"))

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    email.append(Contactemail)
    
print("\nName\t\t\tPhone Number\t\t\tAddress\t\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")
    
print("Enter Contact name you want to update: ")
uname=input("Name:")
update=input("Enter name to update or number to update:")
update_contact(uname, update)
print("Enter Contact name you want to delete: ")
dname=input("Name:")
delete_contact(dname)
print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))


# In[ ]:





# In[ ]:


import re


def update_contact(uname, update):
    if uname in names:
        names[uname] = update
        print(f"Contact '{uname}' updated with new name '{update}'.")
    else:
        print(f"Contact '{uname}' not found.")

def delete_contact(dname):
    if dname in names:
        del names[dname]
        print(f"Contact '{dname}' deleted.")
    else:
        print(f"Contact '{dname}' not found.")
        
names = []
phone_numbers = []
address=[]
email=[]
num = int(input("enter number of contacts you want to add:"))

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    email.append(Contactemail)
    
print("\nName\t\t\tPhone Number\t\t\tAddress\t\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")
    
print("Enter Contact name you want to update: ")
uname=input("Name:")
update=input("Enter name to update or number to update:")
update_contact(uname, update)
print("Enter Contact name you want to delete: ")
dname=input("Name:")
delete_contact(dname)
print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))


# In[ ]:





# In[20]:


import re


def update_contact(uname, update):
    if uname in names:
        names[uname] = update
        print(f"Contact '{uname}' updated with new name '{update}'.")
    else:
        print(f"Contact '{uname}' not found.")

def delete_contact(dname):
    if dname in names:
        del names[dname]
        print(f"Contact '{dname}' deleted.")
    else:
        print(f"Contact '{dname}' not found.")
        
names = []
phone_numbers = []
address=[]
email=[]
num = int(input("enter number of contacts you want to add:"))

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    email.append(Contactemail)
    
print("\nName\t\t\tPhone Number\t\t\tAddress\t\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")
    
print("Enter Contact name you want to update: ")
uname=input("Name:")
update=input("Enter name to update or number to update:")
update_contact(uname, update)
print("Enter Contact name you want to delete: ")
dname=input("Name:")
delete_contact(dname)
print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))


# In[1]:


import re


def update_contact(uname, update):
    if uname in names:
        names[uname] = update
        print(f"Contact '{uname}' updated with new name '{update}'.")
    else:
        print(f"Contact '{uname}' not found.")

def delete_contact(dname):
    if dname in names:
        del names[dname]
        print(f"Contact '{dname}' deleted.")
    else:
        print(f"Contact '{dname}' not found.")
        
names = []
phone_numbers = []
address=[]
email=[]
num = int(input("enter number of contacts you want to add:"))

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    email.append(Contactemail)
    
print("\nName\t\t\tPhone Number\t\t\tAddress\t\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")
    
print("Enter Contact name you want to update: ")
uname=input("Name:")
update=input("Enter name to update or number to update:")
update_contact(uname, update)
print("Enter Contact name you want to delete: ")
dname=input("Name:")
delete_contact(dname)
print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))


# In[2]:


import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="yourusername",
 password="yourpassword",
 database="mydatabase"
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")


# In[3]:


contacts = {}

def add_contact(name, phone, email):
    if name in contacts:
        print(f"{name} already exists in contacts. Use update_contact to change details.")
    else:
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Added {name} to contacts.")

def update_contact(name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts. Use add_contact to add new contact.")

def search_contact(name):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")

# Example usage:
add_contact("Alice", "1234567890", "alice@email.com")
add_contact("Bob", "9876543210", "bob@email.com")
search_contact("Alice")
search_contact("Bob")
update_contact("Bob", phone="9999999999")
search_contact("Bob")
delete_contact("Alice")
search_contact("Alice")


# In[8]:


import re


def update_contact(name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts. Use add_contact to add new contact.")


def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")
        
names = []
phone_numbers = []
address=[]
email=[]
num = int(input("enter number of contacts you want to add:"))

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    email.append(Contactemail)
    
print("\nName\t\t\tPhone Number\t\t\tAddress\t\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")
    
print("Enter Contact name you want to update: ")
uname=input("Name:")
phone=input("phone number")
update_contact("Bob", phone="9999999999")
delete_contact("Alice")
for i in range(num):
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(names[i], Contactphone_number[i], Contact_address[i], Contactemail[i]))


# In[ ]:





# In[ ]:


import re


def update_contact(name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts. Use add_contact to add new contact.")


def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")
        
names = []
phone_numbers = []
address=[]
email=[]
num = int(input("enter number of contacts you want to add:"))

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    email.append(Contactemail)
    
print("\nName\t\t\tPhone Number\t\t\tAddress\t\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")
    
print("Enter Contact name you want to update: ")
uname=input("Name:")
phone=input("phone number")
update_contact("Bob", phone="9999999999")
delete_contact("Alice")
for i in range(num):
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(names[i], Contactphone_number[i], Contact_address[i], Contactemail[i]))


# In[ ]:





# In[12]:


import re


def update_contact(name, phone=None, email=None):
    if name in names:
        if phone:
            names[name]['phone'] = phone
        if email:
            names[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts. Use add_contact to add new contact.")


def delete_contact(name):
    if name in names:
        del names[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")
        
names = []
phone_numbers = []
address=[]
email=[]
num = int(input("enter number of contacts you want to add:"))

for i in range(num):
    Contactname = input("Name: ")
    Contactphone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))
    Contact_address=input("Address:")
    Contactemail = input("Enter your email address: ").strip()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, Contactemail):
        print(f"Thank you! '{Contactemail}' is a valid email address.")
        
    else:
        print(f"Sorry, '{Contactemail}' is not a valid email address.")
    names.append(Contactname)
    phone_numbers.append(Contactphone_number)
    address.append(Contact_address)
    email.append(Contactemail)
    
print("\nName\t\t\tPhone Number\t\t\tAddress\t\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], address[i], email[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    Contactphone_number = phone_numbers[index]
    Contact_address=address[index]
    Contactemail=email[index]
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(search_term, Contactphone_number, Contact_address, Contactemail))

else:
    print("Name Not Found")
    
update_contact("Bob", phone="9999999999")
delete_contact("Alice")
for i in range(num):
    print("Name: {}, Phone Number: {}, Address: {}, Email: {}".format(names[i], Contactphone_number, Contact_address, Contactemail))


# In[15]:


contacts = {}

def add_contact(name, phone, email):
    if name in contacts:
        print(f"{name} already exists in contacts. Use update_contact to change details.")
    else:
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Added {name} to contacts.")

def update_contact(name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts. Use add_contact to add new contact.")

def search_contact(name):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")

# Example usage:
num=int(input("enter number of contacts you want to add:"))
name=input("Name")
phone=input("Phone")
address=input("Address")
email=input("email")
add_contact(name, phone, email)
for i in range(num):
    print("{}\t\t\t{}\t\t\t{}".format(name[i], phone, email))
search_contact("Alice")
search_contact("Bob")
update_contact("Bob", phone="9999999999")
search_contact("Bob")
delete_contact("Alice")
search_contact("Alice")


# In[22]:


contacts = {}
names = []
phone_numbers = []
address=[]
email=[]

def add_contact(name, phone, address, email):
    if name in contacts:
        print(f"{name} already exists in contacts. Use update_contact to change details.")
    else:
        contacts[name] = {'phone': phone, 'address': address, 'email': email}
        print(f"Added {name} to contacts.")

def update_contact(name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts. Use add_contact to add new contact.")

def search_contact(name):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Address: {contacts[name]['address']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")
def print_contact_details(name):
    print(f"Name: {name}")
    print(f"Phone: {contacts[name]['phone']}")
    print(f"Email: {contacts[name]['email']}")
    print()  
    
num=int(input("enter number of contacts you want to add:"))
for i in range(num):
    name=input("Name")
    phone=input("Phone")
    address=input("Address")
    email=input("email")
    add_contact(name, phone, address, email)
    
for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(name, phone, address, email))
    
name=input("Enter name you want to search from contact list")    
search_contact(name)
name=input("Enter name to update phone number")
phone=input("phone")
update_contact(name, phone)
name=input("Enter name to delete contact from contact list")
delete_contact(name)


# In[ ]:





# In[26]:


def add_contact(name, phone, address, email):
    if name in contacts:
        print(f"{name} already exists in contacts. Use update_contact to change details.")
    else:
        contacts[name] = {'phone': phone, 'address': address, 'email': email}
        print(f"Added {name} to contacts.")

def update_contact(name, phone=None, address=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if address:
            contacts[name]['address'] = address
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts. Use add_contact to add new contact.")

def search_contact(name):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Address: {contacts[name]['address']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")
        
def print_contact_details(name):
    print(f"Name: {name}")
    print(f"Phone: {contacts[name]['phone']}")
    print(f"Email: {contacts[name]['email']}")
    print() 


while True:
    print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Search Contact")
        print("4. Search Contact")
        print("5. View Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
            email = input("Enter email: ")
            add_contact(name, phone, address, email)
        
        elif choice == '2':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank to skip): ")
            address = input("Enter new phone number (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            update_contact(name, phone, address, email)
        
        elif choice == '3':
            search_contact()
            
        elif choice == '4':
            print_contact_details()
            
        elif choice == '5':
            name = input("Enter name to delete: ")
            delete_contact(name)
        
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


# In[ ]:





# In[27]:


def add_contact(name, phone, address, email):
    if name in contacts:
        print(f"{name} already exists in contacts. Use update_contact to change details.")
    else:
        contacts[name] = {'phone': phone, 'address': address, 'email': email}
        print(f"Added {name} to contacts.")

def update_contact(name, phone=None, address=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if address:
            contacts[name]['address'] = address
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts. Use add_contact to add new contact.")

def search_contact(name):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Address: {contacts[name]['address']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")
        
def print_contact_details(name):
    print(f"Name: {name}")
    print(f"Phone: {contacts[name]['phone']}")
    print(f"Email: {contacts[name]['email']}")
    print() 


while True:
    print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Search Contact")
        print("4. Search Contact")
        print("5. View Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
            email = input("Enter email: ")
            add_contact(name, phone, address, email)
        
        elif choice == '2':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank to skip): ")
            address = input("Enter new phone number (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            update_contact(name, phone, address, email)
        
        elif choice == '3':
            search_contact()
            
        elif choice == '4':
            print_contact_details()
            
        elif choice == '5':
            name = input("Enter name to delete: ")
            delete_contact(name)
        
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


# In[28]:


contacts = {}

def add_contact(name, phone, address, email):
    if name in contacts:
        print(f"{name} already exists in contacts. Use update_contact to change details.")
    else:
        contacts[name] = {'phone': phone, 'address': address, 'email': email}
        print(f"Added {name} to contacts.")

def update_contact(name, phone=None, address=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if address:
            contacts[name]['address'] = address
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts. Use add_contact to add new contact.")

def search_contact(name=None):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Address: {contacts[name]['address']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")
        
def print_contact_details():
    if contacts:
        for name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Address: {contacts[name]['address']}")
            print(f"Email: {contacts[name]['email']}")
            print()  # Extra line for spacing
    else:
        print("No contacts found.")


    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Search Contact")
        print("4. View All Contacts")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
            email = input("Enter email: ")
            add_contact(name, phone, address, email)
        
        elif choice == '2':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank to skip): ")
            address = input("Enter new address (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            update_contact(name, phone, address, email)
        
        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)
            
        elif choice == '4':
            print_contact_details()
            
        elif choice == '5':
            name = input("Enter name to delete: ")
            delete_contact(name)
        
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")



# In[ ]:





# In[29]:


contacts = {}

def add_contact(name, phone, address, email):
    if name in contacts:
        print(f"{name} already exists in contacts. Use update_contact to change details.")
    else:
        contacts[name] = {'phone': phone, 'address': address, 'email': email}
        print(f"Added {name} to contacts.")

def update_contact(name, phone=None, address=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if address:
            contacts[name]['address'] = address
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts. Use add_contact to add new contact.")

def search_contact(name=None):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Address: {contacts[name]['address']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")
        
def print_contact_details():
    if contacts:
        for name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Address: {contacts[name]['address']}")
            print(f"Email: {contacts[name]['email']}")
            print()  # Extra line for spacing
    else:
        print("No contacts found.")


    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Search Contact")
        print("4. View All Contacts")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
            email = input("Enter email: ")
            add_contact(name, phone, address, email)
        
        elif choice == '2':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank to skip): ")
            address = input("Enter new address (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            update_contact(name, phone, address, email)
        
        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)
            
        elif choice == '4':
            print_contact_details()
            
        elif choice == '5':
            name = input("Enter name to delete: ")
            delete_contact(name)
        
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")



# In[ ]:





# In[30]:


contacts = {}

def add_contact(name, phone, address, email):
    if name in contacts:
        print(f"{name} already exists in contacts. Use update_contact to change details.")
    else:
        contacts[name] = {'phone': phone, 'address': address, 'email': email}
        print(f"Added {name} to contacts.")

def update_contact(name, phone=None, address=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if address:
            contacts[name]['address'] = address
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts. Use add_contact to add new contact.")

def search_contact(name=None):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Address: {contacts[name]['address']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")
        
def print_contact_details():
    if contacts:
        for name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Address: {contacts[name]['address']}")
            print(f"Email: {contacts[name]['email']}")
            print()  # Extra line for spacing
    else:
        print("No contacts found.")


    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Search Contact")
        print("4. View All Contacts")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
            email = input("Enter email: ")
            add_contact(name, phone, address, email)
        
        elif choice == '2':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank to skip): ")
            address = input("Enter new address (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            update_contact(name, phone, address, email)
        
        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)
            
        elif choice == '4':
            print_contact_details()
            
        elif choice == '5':
            name = input("Enter name to delete: ")
            delete_contact(name)
        
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")



# In[ ]:





# In[ ]:





# In[31]:


contacts = {}

def add_contact(name, phone, address, email):
    if name in contacts:
        print(f"{name} already exists in contacts. Use update_contact to change details.")
    else:
        contacts[name] = {'phone': phone, 'address': address, 'email': email}
        print(f"Added {name} to contacts.")

def update_contact(name, phone=None, address=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if address:
            contacts[name]['address'] = address
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts. Use add_contact to add new contact.")

def search_contact(name=None):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Address: {contacts[name]['address']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")
        
def print_contact_details():
    if contacts:
        for name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Address: {contacts[name]['address']}")
            print(f"Email: {contacts[name]['email']}")
            print()  # Extra line for spacing
    else:
        print("No contacts found.")


    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Search Contact")
        print("4. View All Contacts")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
            email = input("Enter email: ")
            add_contact(name, phone, address, email)
        
        elif choice == '2':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank to skip): ")
            address = input("Enter new address (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            update_contact(name, phone, address, email)
        
        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)
            
        elif choice == '4':
            print_contact_details()
            
        elif choice == '5':
            name = input("Enter name to delete: ")
            delete_contact(name)
        
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


# In[ ]:





# In[32]:


contacts = {}

def add_contact(name, phone, address, email):
    if name in contacts:
        print(f"{name} already exists in contacts. Use update_contact to change details.")
    else:
        contacts[name] = {'phone': phone, 'address': address, 'email': email}
        print(f"Added {name} to contacts.")

def update_contact(name, phone=None, address=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if address:
            contacts[name]['address'] = address
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts. Use add_contact to add new contact.")

def search_contact(name=None):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Address: {contacts[name]['address']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")
        
def print_contact_details():
    if contacts:
        for name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Address: {contacts[name]['address']}")
            print(f"Email: {contacts[name]['email']}")
            print()  # Extra line for spacing
    else:
        print("No contacts found.")


print("\n===== Contact Book Menu =====")
print("1. Add Contact")
print("2. Update Contact")
print("3. Search Contact")
print("4. View All Contacts")
print("5. Delete Contact")
print("6. Exit")
  
while True:
	choice = input("Enter your choice (1-6): ")
	if choice == '1':
		name = input("Enter name: ")
		phone = input("Enter phone number: ")
		address = input("Enter address: ")
		email = input("Enter email: ")
		add_contact(name, phone, address, email)
        
	elif choice == '2':
		name = input("Enter name to update: ")
		phone = input("Enter new phone number (leave blank to skip): ")
		address = input("Enter new address (leave blank to skip): ")
		email = input("Enter new email (leave blank to skip): ")
		update_contact(name, phone, address, email)
        
	elif choice == '3':
		name = input("Enter name to search: ")
		search_contact(name)
            
	elif choice == '4':
		print_contact_details()
            
	elif choice == '5':
		name = input("Enter name to delete: ")
		delete_contact(name)
        
	elif choice == '6':
		print("Exiting program. Goodbye!")
		break
        
	else:
		print("Invalid choice. Please enter a number between 1 and 6.")


# In[33]:


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


# In[34]:


#vartika Singh
#Task 3 Contact Book

contacts = {}

def add_contact(name, phone, address, email):
    if name in contacts:
        print(f"{name} already exists in contacts list.")
    else:
        contacts[name] = {'phone': phone, 'address': address, 'email': email}
        print(f"Added {name} to contacts list.")

def update_contact(name, phone=None, address=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if address:
            contacts[name]['address'] = address
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts list.")

def search_contact(name=None):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Address: {contacts[name]['address']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")
        
def print_contact_details():
    if contacts:
        for name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Address: {contacts[name]['address']}")
            print(f"Email: {contacts[name]['email']}")
            print()  # Extra line for spacing
    else:
        print("No contacts found.")


print("\n===== Contact Book Menu =====")
print("1. Add Contact to Contact Book")
print("2. Update Contact to Contact Book")
print("3. Search Contact from Contact Book")
print("4. View All Contacts from Contact Book")
print("5. Delete Contact ")
print("6. Exit")
  
while True:
	choice = input("Enter your choice (1-6): ")
	if choice == '1':
		name = input("Enter name: ")
		phone = input("Enter phone number: ")
		address = input("Enter address: ")
		email = input("Enter email: ")
		add_contact(name, phone, address, email)
        
	elif choice == '2':
		name = input("Enter name to update: ")
		phone = input("Enter new phone number (leave blank to skip): ")
		address = input("Enter new address (leave blank to skip): ")
		email = input("Enter new email (leave blank to skip): ")
		update_contact(name, phone, address, email)
        
	elif choice == '3':
		name = input("Enter name to search: ")
		search_contact(name)
            
	elif choice == '4':
		print_contact_details()
            
	elif choice == '5':
		name = input("Enter name to delete: ")
		delete_contact(name)
        
	elif choice == '6':
		print("Exiting program. Goodbye!")
		break
        
	else:
		print("Invalid choice. Please enter a number between 1 and 6.")


# In[35]:


#vartika Singh
#Task 3 Contact Book

contacts = {}

def add_contact(name, phone, address, email):
    if name in contacts:
        print(f"{name} already exists in contacts list.")
    else:
        contacts[name] = {'phone': phone, 'address': address, 'email': email}
        print(f"Added {name} to contacts list.")

def update_contact(name, phone=None, address=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if address:
            contacts[name]['address'] = address
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts list.")

def search_contact(name=None):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Address: {contacts[name]['address']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")
        
def print_contact_details():
    if contacts:
        for name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Address: {contacts[name]['address']}")
            print(f"Email: {contacts[name]['email']}")
            print()  # Extra line for spacing
    else:
        print("No contacts found.")


print("\n===== Contact Book Menu =====")
print("1. Add Contact to Contact Book")
print("2. Update Contact to Contact Book")
print("3. Search Contact from Contact Book")
print("4. View All Contacts from Contact Book")
print("5. Delete Contact ")
print("6. Exit")
  
while True:
	choice = input("Enter your choice (1-6): ")
	if choice == '1':
		name = input("Enter name: ")
		phone = input("Enter phone number: ")
		address = input("Enter address: ")
		email = input("Enter email: ")
		add_contact(name, phone, address, email)
        
	elif choice == '2':
		name = input("Enter name to update: ")
		phone = input("Enter new phone number (leave blank to skip): ")
		address = input("Enter new address (leave blank to skip): ")
		email = input("Enter new email (leave blank to skip): ")
		update_contact(name, phone, address, email)
        
	elif choice == '3':
		name = input("Enter name to search: ")
		search_contact(name)
            
	elif choice == '4':
		print_contact_details()
            
	elif choice == '5':
		name = input("Enter name to delete: ")
		delete_contact(name)
        
	elif choice == '6':
		print("Exiting program. Goodbye!")
		break
        
	else:
		print("Invalid choice. Please enter a number between 1 and 6.")


# In[ ]:





# In[ ]:


#vartika Singh
#Task 3 Contact Book

contacts = {}

def add_contact(name, phone, address, email):
    if name in contacts:
        print(f"{name} already exists in contacts list.")
    else:
        contacts[name] = {'phone': phone, 'address': address, 'email': email}
        print(f"Added {name} to contacts list.")

def update_contact(name, phone=None, address=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if address:
            contacts[name]['address'] = address
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts list.")

def search_contact(name=None):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Address: {contacts[name]['address']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")
        
def print_contact_details():
    if contacts:
        for name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Address: {contacts[name]['address']}")
            print(f"Email: {contacts[name]['email']}")
            print()  # Extra line for spacing
    else:
        print("No contacts found.")


print("\n===== Contact Book Menu =====")
print("1. Add Contact to Contact Book")
print("2. Update Contact to Contact Book")
print("3. Search Contact from Contact Book")
print("4. View All Contacts from Contact Book")
print("5. Delete Contact ")
print("6. Exit")
  
while True:
	choice = input("Enter your choice (1-6): ")
	if choice == '1':
		name = input("Enter name: ")
		phone = input("Enter phone number: ")
		address = input("Enter address: ")
		email = input("Enter email: ")
		add_contact(name, phone, address, email)
        
	elif choice == '2':
		name = input("Enter name to update: ")
		phone = input("Enter new phone number (leave blank to skip): ")
		address = input("Enter new address (leave blank to skip): ")
		email = input("Enter new email (leave blank to skip): ")
		update_contact(name, phone, address, email)
        
	elif choice == '3':
		name = input("Enter name to search: ")
		search_contact(name)
            
	elif choice == '4':
		print_contact_details()
            
	elif choice == '5':
		name = input("Enter name to delete: ")
		delete_contact(name)
        
	elif choice == '6':
		print("Exiting program. Goodbye!")
		break
        
	else:
		print("Invalid choice. Please enter a number between 1 and 6.")


# In[ ]:





# In[ ]:


#vartika Singh
#Task 3 Contact Book

contacts = {}

def add_contact(name, phone, address, email):
    if name in contacts:
        print(f"{name} already exists in contacts list.")
    else:
        contacts[name] = {'phone': phone, 'address': address, 'email': email}
        print(f"Added {name} to contacts list.")

def update_contact(name, phone=None, address=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if address:
            contacts[name]['address'] = address
        if email:
            contacts[name]['email'] = email
        print(f"Updated {name}'s contact information.")
    else:
        print(f"{name} not found in contacts list.")

def search_contact(name=None):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Address: {contacts[name]['address']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")
        
def print_contact_details():
    if contacts:
        for name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Address: {contacts[name]['address']}")
            print(f"Email: {contacts[name]['email']}")
            print()  # Extra line for spacing
    else:
        print("No contacts found.")


print("\n===== Contact Book Menu =====")
print("1. Add Contact to Contact Book")
print("2. Update Contact to Contact Book")
print("3. Search Contact from Contact Book")
print("4. View All Contacts from Contact Book")
print("5. Delete Contact ")
print("6. Exit")
  
while True:
	choice = input("Enter your choice (1-6): ")
	if choice == '1':
		name = input("Enter name: ")
		phone = input("Enter phone number: ")
		address = input("Enter address: ")
		email = input("Enter email: ")
		add_contact(name, phone, address, email)
        
	elif choice == '2':
		name = input("Enter name to update: ")
		phone = input("Enter new phone number (leave blank to skip): ")
		address = input("Enter new address (leave blank to skip): ")
		email = input("Enter new email (leave blank to skip): ")
		update_contact(name, phone, address, email)
        
	elif choice == '3':
		name = input("Enter name to search: ")
		search_contact(name)
            
	elif choice == '4':
		print_contact_details()
            
	elif choice == '5':
		name = input("Enter name to delete: ")
		delete_contact(name)
        
	elif choice == '6':
		print("Exiting program. Goodbye!")
		break
        
	else:
		print("Invalid choice. Please enter a number between 1 and 6.")

