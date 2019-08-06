#!/usr/bin/env python
# coding: utf-8

# In[4]:


my_dict={}
print (type(my_dict))


# In[5]:


my_dic=set()
print (type(my_dic))


# In[10]:


my_dic={1:2,3:4}
my_dic
my_dic={1:2,3:4,5:['abc','def'],['xyz']:6}
my_dic


# In[12]:


my_dic={1.0:2,3:4}
my_dic


# In[14]:


dic={'Name':"Ankesh",'Age':24,'sex':'Male'}
dic
print (dic.get('Name'))


# In[18]:


print (dic['sal']) #It is always better to use get to fetch values, as it does not throws an error. 


# In[23]:


#to add a key or to modify a key or update a key
dic
dic['Name']='Rajeev'
dic
dic['sal']=4000000
dic


# In[26]:


#to delete pop and pop iteam

dic
print(dic.pop('Age'))


# In[28]:


dic
dic.popitem() #removes any of the arbiratry key(random)


# In[29]:


dic


# In[31]:


sq={1:1,2:4,3:9,4:16}
sq
del (sq)
sq


# In[41]:


sq={'abc':1,2:4,3:9,4:16}
sq
sq1=sq.copy()


# In[50]:


sq1


# In[56]:


sq1
print (sq1.items()) #returns a list of tuples
l1=sq1.items()
print (type(l1))


# In[59]:


print (sq1.keys())
print (type(sq1))


# In[62]:


print (sq1.values())
print (type(sq1))


# In[52]:


cut_off={}.fromkeys(['Maths','Bio','Arts'],90)
cut_off


# In[63]:


d1={}
print (dir(d1))


# In[68]:


d1={1:2,2:4,3:6,'abc':'def'}
for k in d1:
    print (k)


# In[70]:


d2={1:2,2:4,3:6,'abc':'def'}

for k in d2.keys():
    print (k) 


# In[71]:


d2={1:2,2:4,3:6,'abc':'def'}

for v in d2.values():
    
    print (v)


# In[72]:


d2={1:2,2:4,3:6,'abc':'def'}

for k,v in d2.items():
    
    print ('{} is the key with {} as value'.format(k,v))


# In[77]:


#dictionary comprehension
d2={1:2,2:4,3:6,4:'def'}
d2

new_d3={k:v for k,v in d2.items() if k>2}
new_d3

