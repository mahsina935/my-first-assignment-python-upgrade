#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question experiment with five list's in built function


# In[1]:


#append():
List = ['Mathematics', 'chemistry', 1997, 2000] 

List.append(20544) 

print(List) 


# In[2]:


#insert():
List = ['Mathematics', 'chemistry', 1997, 2000] 
# Insert at index 2 value 10087 

List.insert(2,10087)      

print(List)         


# In[3]:


#extend():
List1 = [1, 2, 3] 

List2 = [2, 3, 4, 5] 

  
# Add List2 to List1 
List1.extend(List2)         

print(List1) 

  
# Add List1 to List2 now 
List2.extend(List1)  

print(List2) 


# In[4]:


#sum():
List = [1, 2, 3, 4, 5] 

print(sum(List)) 


# In[5]:


#count():
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 

print(List.count(1)) 


# In[ ]:


#Question2:Do experiment with 5 dictionary in built functions.


# In[1]:


#Creating an empty Dictionary 
#with dict() method 

Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) 

print("\nDictionary with the use of dict(): ") 

print(Dict) 


# In[2]:


#Creating a Dictionary 
# with each item as a Pair 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 

print("\nDictionary with each item as a pair: ") 

print(Dict) 


# In[6]:


#Creating a Dictionary  
# with Mixed keys 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 

print("\nDictionary with the use of Mixed Keys: ") 

print(Dict) 


# In[7]:


#Creating a Dictionary 
# with dict() method 
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) 

print("\nDictionary with the use of dict(): ") 

print(Dict) 


# In[8]:


#Creating an empty Dictionary 
Dict = {} 

print("Empty Dictionary: ") 

print(Dict) 


# In[ ]:




