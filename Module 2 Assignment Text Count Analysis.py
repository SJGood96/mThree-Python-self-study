#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Module 2 Assignment: Text Count Analysis                   5/19/21
# Spencer Good

import string #import the string module 
#use the built-in string.punctuation method to create a list of all punctuation marks
punctuation_list =  list(string.punctuation)


s = """Imagine a vast sheet of paper on which straight Lines, 
Triangles, Squares, Pentagons, Hexagons, and other figures, instead of remaining fixed in their places, 
move freely about, on or in the surface, but without the power of rising above or sinking below it, very much like 
shadows - only hard and with luminous edges - and you will then have a pretty correct notion of my country and countrymen. 
Alas, a few years ago, I should have said "my universe": but now my mind has been opened to higher views of things."""
 
#do not change any code above this line
#your code here

#these are the variables and empty list/dict
s_lower = s.lower()
words = list()  
w_clean = list()
freq = dict()
 

s = str.split(s_lower)

for x in s:
    words.append(x)

word_set = set(s)

#code to find the token/frequency key value pair

for key in s:
    if key in freq:
        freq[key] += 1
    else:
        freq[key] = 1


#this stripped the punctuation
s = [''.join(c for c in x if c not in punctuation_list) for x in s]
for i in s:
    w_clean.append(i)
    if i =='':
        w_clean.remove(i)
        

cfreq = dict()
        
for key in s:
    if key in cfreq:
        cfreq[key] += 1
    else:
        cfreq[key] = 1



print(s_lower)
print(words)
print(len(s))
print(len(word_set))
print(freq)
print(words)
print(w_clean)
print(len(w_clean))
print(cfreq)


# In[ ]:




