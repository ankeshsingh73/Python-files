#!/usr/bin/env python
# coding: utf-8

# In[2]:


str1='How I am doing?'


# In[6]:


for ele in str1:
    print (ele, end =" ")


# In[7]:


print ('l' in str1)


# In[8]:


print ('l' not in str1)


# In[10]:


str1[1]
str1[2]='W'


# In[11]:


str1=" I am doing great ! Thanks for asking, How about you"
str1


# In[12]:


print (id(str1))


# In[13]:


str2=" I am doing great ! Thanks for asking, How about you"


# In[14]:


print (id(str2))


# In[16]:


str1=str1.lower()
str1


# In[18]:


str2=str2.upper()
str2


# In[19]:


sp1=str1.split(' ')

print (type(sp1))
print (sp1)


# In[29]:


z1='-'.join(sp1)
print (type(z1))


# In[34]:


ex1=['a','abc']
s1=' '
s1=s1.join(ex1) #instance in list (iterable) is string, what if we have int or float or say boolean ?
s1


# In[35]:


ex2=[1,2,4]
s1='#'
s1=s1.join(ex2) #doesnot work for int 


# In[36]:


ex2=[1.0,2.0,4.0]
s1='#'
s1=s1.join(ex2) #does not work with float, so bool stands no where out here 


# In[37]:


wish='Morning Pals'
print (wish.find('Pa'))


# In[41]:


#what if the string do not have those characters placed in argument of find()
wish='Morning Pals'
print (wish.find('sin'))


# In[50]:


s1='Never give your time to the bad time'
s2=reversed (s1)
if s1==s2:
    print (True)
else:
    print (False)
#


# In[54]:


s1='MADAM'
s2=reversed(s1)
print (s1)
print (s2)
if s2==s1:
    print (True)
else:
    print (False)
    
#s1 and s2 are two object and represents a value corresonding to an address, when s1==s2, it compares the address of these two objects which is not equal hence false


# s1=list('MADAM')    #when the string is converted into list, the list can compare
# s2=list (reversed(s1))
# print (s1)
# print (s2)
# if s1==s2:
#     print (True)
# else:
#     print (False)

# In[70]:


mot1='All my life, I have learnt to struggle and win'

Limot1=mot1.split(' ')
print (type(Limot1))


# In[69]:


Limot1.sort()
Limot1
for ele in Limot1:
    print (ele, end =' ')


# In[ ]:




