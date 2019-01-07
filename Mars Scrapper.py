
# coding: utf-8

# In[93]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
from splinter import Browser


# In[94]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[95]:


url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[96]:


html = browser.html
soup = BeautifulSoup(html,'html.parser')


# In[97]:


news_title = soup.find_all('div',class_='content_title')


# In[98]:


print(news_title[0].text)


# In[99]:


news_p = soup.find_all('div',class_='article_teaser_body')


# In[100]:


print(news_p[0].text)


# In[130]:


featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(featured_image_url)


# In[131]:


featured_image_html = browser.html
featured_image_soup = BeautifulSoup(featured_image_html,'html.parser')


# In[142]:


featured_image = featured_image_soup.find_all('div','fancybox-wrap fancybox-dark fancybox-type-image fancybox-desktop fancybox-dark-desktop fancybox-open')


# In[143]:


featured_image


# In[101]:


weather_url = "https://twitter.com/marswxreport?lang=en"
browser.visit(weather_url)


# In[102]:


weather_html = browser.html
weather_soup = BeautifulSoup(weather_html,'html.parser')


# In[123]:


mars_weather = weather_soup.find_all('div',class_='js-tweet-text-container')


# In[126]:


print(mars_weather[0].text)


# In[127]:


mars_facts_url = 'http://space-facts.com/mars/'


# In[128]:


tables = pd.read_html(mars_facts_url)


# In[129]:


tables[0]

