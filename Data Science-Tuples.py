#!/usr/bin/env python
# coding: utf-8

# In[4]:


t=()
print (t)
print (type (t))


# In[23]:


#How Can I change a tuple ???????????????????????////
t=(10,22,'Hell',[2.0,3.0,'Yeah'])
print (t)
for ele in t:
    print (type(ele))
    
t[3][1]=22
t[3]


# In[15]:


tup1=('Eng')
print (type(tup1))
tup2=('Eng',)
print (type(tup2))


# In[18]:


tupq='Ram',('Shan','dhan','Tan')
print (tupq)
print (tupq[1])
print (tupq[1][2])


# In[ ]:


t=(1,2,4,4,5,6,6)
print (t.index[5])
print (t[:-4])
print (t[:5:2])


# In[36]:


#repeating a tuple
tup1= (('yo!',)*4)



print (type(tup1))


# In[38]:


t=(2,3,4,5)
del t[2]

t1=[2,4,5,5,5,6,9]
del t1 #a whole tuple can be deleted but not a partilcular item 


# In[ ]:


num=int (input('Enter the number, Motherfucker !'))
tup=1,3,4,45,5,5,3,3,5,5,5,3,2,4,5,5,6
for ele in tup:
    if ele==num:
        print ('Found at {}'.format(tup.index(ele)))
        break;  
    


# In[7]:


t=1,2,31,4
print (t)
print (sorted(t))
print (t.sort())


# In[ ]:




