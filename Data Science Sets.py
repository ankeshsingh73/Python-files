#!/usr/bin/env python
# coding: utf-8

# In[6]:


s={1,2,34,5,5}
print (s)
print (type(s))
print (s[1])


# In[4]:


#a variable can be analyzed as set using set()

s=set()
print (type(s))


# In[13]:


s=set()
print (type(s))
s={1,2,3,4}
print (s)
s.add(33)
s
s.update([11,2,2,3,4])
s


# In[24]:


s1={1,2,3,4,5,1}
s1
s1.remove(2)
s1
s1.remove(11)


# In[28]:


s1={3,4,5,5,'set'}

s1.discard('SET')
s1
s1.discard(4) #if 4 is not present in our set discard() won't throw an error explicitaly i.e Keyerror
s1


# In[32]:


s1={1,3,4,'set'}
s1
s1.pop() #removes any of the random element from the set
s1


# In[43]:


#set operations union and intersection

s1={1,2,'abc',4.0}
s2={2,'abc',5,6,7,4.0}
print (s1 | s2) #union includes all elments present in either of the set

print (s1 & s2)

s3={1,2,'def'}
print (s1.union(s2))

print (s1.intersection(s3))


# In[48]:


#set difference and symmety difference

s1={1,2,3,4,5}
s2={2,4,5,77,7}
print (s1-s2)
print (s1.difference(s2))

s3={1,2,3,4,5}
s4={4,5,6,7}

print (s3^s4)

print (s3.symmetric_difference(s4))


# In[50]:


#issubset

s1={1,2,4}
s2={1,4,5,5,6,7,7}
print (s1.issubset(s2))


# In[2]:


s1=frozenset ([1,2,3,4])
print (type(s1))


# In[3]:


s1.add('ankesh')

