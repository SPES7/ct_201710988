
# coding: utf-8

# <h1>안녕 이건 큰  글씨야!!</h1>
# <h2>안녕 이건 조금 작은 큰 글씨야!!</h2>
# <h3>안녕 이건 조금 더 작은 큰 글씨야!!</h3>

# # 큰 글씨
# ## 작은 글씨
# ### 더 작은 글씨

# * 도시
#     * 서울
#     * 시드니
#     * 뉴욕
#         * 1번가
#         * 33번지
#         

# In[2]:

print "hello"
print "1+2=",1+2


# In[3]:

from PIL import Image


# In[4]:

m = Image.open("C:\\Users\\400T6B\\Downloads\\italy-1587287_1920.jpg")


# In[5]:

m.show()


# In[6]:

get_ipython().magic(u'matplotlib inline')
from matplotlib.pyplot import imshow
imshow(m)


# * jpg파일을 gif파일로 변환하기
#     * 파일확장자를 gif로 적어준다.

# In[7]:

m.save("C:\\Users\\400T6B\\Downloads\\italy-1587287_1920.gif")


# In[8]:

m.save("C:\\Users\\400T6B\\Downloads\\italy-1587287_1920.png")


# In[9]:

mg = Image.open("C:\\Users\\400T6B\\Downloads\\italy-1587287_1920.gif")


# In[10]:

mg.show()


# In[11]:

get_ipython().magic(u'matplotlib inline')
from matplotlib.pyplot import imshow
imshow(mg)


# In[12]:

mp = Image.open("C:\\Users\\400T6B\\Downloads\\italy-1587287_1920.png")


# In[ ]:




# In[13]:

mp.show()


# In[14]:

get_ipython().magic(u'matplotlib inline')
from matplotlib.pyplot import imshow
imshow(mp)


# * Operator overloading
#     * '+'가 숫자를 만나면 합산, 문자를 만나면 합성, 경우에 따라서 여러 가지 기능을 수행하는 것

# In[15]:

print 1+2


# In[17]:

s = "hello " + "world"
print s


# In[18]:

print 2*3


# In[19]:

print "hello "*3


# * startswith() 기능 배우기

# In[21]:

s ="Hello World"
s.startswith('H')


# In[22]:

"Hello World".startswith('h')


# In[23]:

s = Hello World


# In[24]:

type(s)


# In[28]:

s1="123"
s2="111"
type(s1)


# In[29]:

int(s1)+int(s2)


# In[31]:

print s[0]=='H'


# In[35]:

msg = 'She says "Good morning!"'
print msg


# In[38]:

s[0] = 'Q'


# In[39]:

s.endswith('d')


# In[40]:

len(s)


# In[42]:

for ch in s:
    print ch,


# In[45]:

for i in range(0,11):
    print s[i],


# In[46]:

for i in range(0,len(s)):
    print s[i],


# In[47]:

s.index("Wor")


# In[48]:

s.strip('rld')


# In[51]:

s1 = "Hello\n\tworld\n"
print s1


# In[52]:

print s1.strip()


# In[54]:

print s[-1]


# In[58]:

print(s[len(s)-1])


# In[59]:

print s[0:5]


# In[61]:

print s[0:-1]


# In[63]:

print s[:]

