#!/usr/bin/env python
# coding: utf-8

# In[2]:


STEP_COUNT = 25
STEP_SIZE = 0.9 #Скорость обучения
# для работы графиков
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pylab as plt

def func(x):
    return (x - 5) ** 2

def func_derivative(x):
    return 2 * (x - 5)

previous_x, current_x = 0, 0
xn = current_x
yn = func(xn)
Y = {xn: yn}

for i in range(STEP_COUNT):
    current_x = previous_x - STEP_SIZE * func_derivative(previous_x)
    previous_x = current_x
    Y[current_x] = func(current_x)
print("After", STEP_COUNT, "steps theta=", format(current_x, ".6f"), "function value=", format(func(current_x), ".6f"))
Y


# In[8]:


# рисуем график функции
x = range(-10,20)
y = [func(xn) for xn in x]
plt.plot(x, y)
plt.show()


# In[4]:


# наносим найденные точки на график
plt.plot(list(Y.keys()), list(Y.values()), 'ro')
plt.show()


# In[6]:


#масштабируем
plt.plot(list(Y.keys()), list(Y.values()), 'ro')
plt.axis([4.95, 5.05, -0.1, 0.1])
plt.show()


# In[12]:


# выводим пару искомых минимальных X и Y (близких к минимумам)
print ('мин. Х =', '%.8f' % current_x)
print ('мин. Y =', '%.8f' % func(current_x))


# In[ ]:




