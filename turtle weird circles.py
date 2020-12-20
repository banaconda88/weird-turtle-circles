#!/usr/bin/env python
# coding: utf-8

# In[7]:


def turtle_weirder_circles():
    t = input("How many sides do you want the shapes that make up your circle to have?")
    t = int(t)
    y = 360 / t
    for i in range(36):
        for j in range(t):
            x.forward(50)
            x.left(y)
        x.right(10) 


# In[8]:


import turtle # nested loops
x=turtle.Turtle()
x.shape('turtle')
x.color('lightBlue')
x.shapesize(1,0.5)
turtle_weirder_circles()


# In[ ]:




