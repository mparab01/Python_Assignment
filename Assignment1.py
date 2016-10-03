
# coding: utf-8

# Q. Print only the words that start with s in this sentence

# In[1]:

s = 'Print only the words that start with s in this sentence'


# In[2]:

for i in s.split():
    if i[0]=='s':
        print i
    


# Q. Use range to print all even numbers from 0 to 10

# In[4]:

l = range(0,11,2)
print l


# Q. Use list comprehension to create a list of numbers between 1 to 50 that are divisible by 3

# In[6]:

l2 = [i for i in range(1,51)if i%3==0]
print l2


# Go through the string below and if the length of a word is even print "even!"

# In[7]:

st = 'Print every word in this sentence that has an even number of letters'
for i in st.split():
    if len(i)%2==0:
        print i


# Q. Write a program that prints the integer from 1 to 100. But for multiple of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For the numbers which are multiples of both three and five print "FizzBuzz"

# In[ ]:

for i in range(1, 101):
    if (i%5==0) and (i%3==0):
        print "FizzBuzz"
    elif (i%3==0):
        print "Fizz"
    elif (i%5==0):
        print "Buzz"
    else:
        print i


# Q. Use list Comprehension to create a list of the first letters of every letters of every word in the string below:

# In[10]:

st = 'Create a list of the first letter of every word in this string'


# In[12]:

l2 = [s[0] for s in st.split()]
print l2


# In[ ]:



