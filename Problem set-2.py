#!/usr/bin/env python
# coding: utf-8

# In[3]:


#question 1

a = 0
def b():
 global a
 a = c(a)
def c(a):
 return a + 2

b()
b()
b()
a

#Value is 6 after executioon


# In[11]:


#question 2

def fileLength(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(len(contents))
    except FileNotFoundError:
        print(f"File {filename} not found")
        
fileLength('test.txt')
fileLength('idterm.py')


# In[13]:


#question 3

class Marsupial:
    def __init__(self):
        self.pouch = []

    def put_in_pouch(self, item):
        self.pouch.append(item)

    def pouch_contents(self):
        return self.pouch
    
m = Marsupial()
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')
m.pouch_contents()


# In[21]:


#question 4: 

def collatz(x):
    if x == 1:
        print(x)
        return
    elif x % 2 == 0:
        print(x)
        collatz(x // 2)
    else:
        print(x)
        collatz(3*x + 1)

collatz(1)
collatz(10)


# In[26]:


#question 5:

def binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return binary(n // 2) + str(n % 2)


binary(0)
binary(1)
binary(3)
binary(9)


# In[23]:


#question 6:

from html.parser import HTMLParser

class HeadingParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.indentation = 0

    def handle_starttag(self, tag, attrs):
        if tag == "h1":
            print(" " * self.indentation + self.get_text(attrs))
            self.indentation = 0
        elif tag == "h2":
            print(" " * self.indentation + self.get_text(attrs))
            self.indentation = 1
        elif tag == "h3":
            print(" " * self.indentation + self.get_text(attrs))
            self.indentation = 2
        elif tag == "h4":
            print(" " * self.indentation + self.get_text(attrs))
            self.indentation = 3
        elif tag == "h5":
            print(" " * self.indentation + self.get_text(attrs))
            self.indentation = 4
        elif tag == "h6":
            print(" " * self.indentation + self.get_text(attrs))
            self.indentation = 5

    def get_text(self, attrs):
        for attr, val in attrs:
            if attr == "class" and "title" in val:
                return val.split("title-")[1]
        return ""

infile = open('w3c.html')
content = infile.read()
infile.close()
hp = HeadingParser()
hp.feed(content)


# In[ ]:





# In[20]:


#QUestion 9

words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']


a = [y.upper() for y in words]
print(a)
b = [y.lower() for y in words]
print(b)
c = [len(y) for y in words]
print(c)
d = [[y.upper(), y.lower(), len(y)] for y in words]
print(d)
e = [y for y in words if len(y) >= 4]
print(e)


# In[ ]:




