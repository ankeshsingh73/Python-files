#!/usr/bin/env python
# coding: utf-8

# In[9]:


li=["one", 2,3.0]
print (li)
li.append('FOUR')
print (li)
li.insert(2,"TWO")
print (li)
li.append("TWO")
print (li)
li.remove('TWO')
print (li)


# In[12]:


l1=["one", 2,3.0]
ele=input ('Enter the element')
if ele in l1:
    print (True)
else:
    print (False)
    


# In[17]:


l1=[]
for i in range (5):
    num=int (input('Enter the {} value for your list : '.format(i)))
    l1.append(num)
    
print (l1)
s1=sorted(l1)
print (s1)
s2=sorted(l1,reverse=True)
print (s2)


# In[24]:


li=[1,3,4,5,5,66,4,3,5,56,6,'a',5]
print (li[-4:-1])

print (li[::2])
print (li.count(5))


# In[25]:


#list comprehension in python
sq=[]
for i in range(6):
    sq.append(i**2)

print (sq)


# In[26]:


sq=[i**2 for i in range (6)]
print (sq)


# In[ ]:


li=[1,3,4,4,2,2,3,6,7,7,7,5,3,31]
new_li=[]
i=0
j=1
for i in li:
    for j in li:
        if i!=j:
            new_li=li.append(i)
        
print (new_li)   


# In[20]:



li=[1,-3,4,-4,2,2,3,-6,7,-7,7,-5,3,31]
for ele in li:
    print (ele,end=' ')

print ()
plus=(i**2  for i in li)
for i in plus:
    print (i, end=' ')

print ()
plus1=(i  for i in li if i%2==0)
for i in plus1:
    print (i, end=' ')


# In[32]:


li=[3,5,6,7,1]

lisq=[(i,i*2) for i in li]
print (lisq)
print (lisq[2])
print (type (lisq[1]))



# In[65]:


#matrix creation
m1=[[1,2,3],[4,6,9],[16,36,81]]
# print (m1[0][1])
# # print (len(m1))
# print (m1)
m1t=[]
for i in range (3):
    temp=[]
    for row in m1:
        print (row)
        temp.append(row[i])
        print (temp)
    m1t.append(temp)
        

print (m1t) 
 


# In[68]:


print (m1)
transposed=[[row[i] for row in m1]for i in range(len(m1))]
print (transposed)


# In[72]:


li=[2,3,4,5,6,6]
print (li.index(2))

