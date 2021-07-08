#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[1]:


import requests


# In[ ]:





# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: This sure seems familiar.*

# In[2]:


mtl_weather = requests.get("https://api.weatherapi.com/v1/current.json?key=YOUR_KEY_HERE&q=Montreal&days=1&aqi=no&alerts=no").json()


# In[ ]:





# In[ ]:





# ## 2) What's the current wind speed, and how much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference. Same as we did last time!*

# In[3]:


wind_mph = mtl_weather['current']['wind_mph']


# In[4]:


current_temp_f = mtl_weather['current']['temp_f']


# In[5]:


feelslike_f = mtl_weather['current']['feelslike_f']


# In[6]:


print(f"The current wind speed is {wind_mph}mph. It is {current_temp_f} degrees, but feels like {feelslike_f} degrees, but is actually {current_temp_f} degrees, making a difference of {round(abs(current_temp_f - feelslike_f),2)} degrees.")


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible on next Thursday?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[7]:


mtl_moon = requests.get("https://api.weatherapi.com/v1/astronomy.json?key=YOUR_KEY_HERE&q=Montreal&dt=2021-06-21").json()


# In[8]:


moon_phase = mtl_moon['astronomy']['astro']['moon_phase']


# In[9]:


moon_illumination = mtl_moon['astronomy']['astro']['moon_illumination']


# In[10]:


print(f"The moon will be in the {moon_phase} phase illuminated at {moon_illumination}%.")


# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[11]:


mtl_weather = requests.get("https://api.weatherapi.com/v1/forecast.json?key=YOUR_KEY_HERE&q=Montreal&days=1&aqi=no&alerts=no").json()


# In[12]:


maxtemp_f = mtl_weather['forecast']['forecastday'][0]['day']['maxtemp_f']


# In[13]:


mintemp_f = mtl_weather['forecast']['forecastday'][0]['day']['mintemp_f']


# In[14]:


print(f"The difference between the highest ({maxtemp_f}ºF) and lowest ({mintemp_f}ºF) temperatures is {round(maxtemp_f - mintemp_f,2)}ºF.")


# In[ ]:





# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# In[15]:


# whatever variable(s) used to make the request if the variables weren't renamed (in this case, mtl_weather and mtl_moon)


# In[ ]:





# ## 5) Go through the daily forecasts, printing out the next week's worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[16]:


mtl_forecast = requests.get("https://api.weatherapi.com/v1/forecast.json?key=YOUR_KEY_HERE&q=Montreal&days=7&aqi=no&alerts=no").json()


# In[17]:


for date in mtl_forecast['forecast']['forecastday']:
  if date['day']['maxtemp_f'] >= 80:
    print(f"The max temperature on {date['date']} will be {date['day']['maxtemp_f']}ºF and it's going to be a hot one.")
  elif date['day']['maxtemp_f'] >= 65:
    print(f"The max temperature on {date['date']} will be {date['day']['maxtemp_f']}ºF and it's going to be toasty.")
  else:
    print(f"The max temperature on {date['date']} will be {date['day']['maxtemp_f']}ºF and it's going to be cold.")


# # 6) What will be the hottest day in the next week? What is the high temperature on that day?

# In[18]:


maxes = [date['day']['maxtemp_f'] for date in mtl_forecast['forecast']['forecastday']]


# In[19]:


print(f"The highest temperature in the next 3 days wil be {max(maxes)}ºF.")


# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[20]:


mia_weather = requests.get("https://api.weatherapi.com/v1/forecast.json?key=YOUR_KEY_HERE&q=Miami&days=1&aqi=no&alerts=no").json()


# In[21]:


for hour in mia_weather['forecast']['forecastday'][0]['hour']:
  if hour['cloud'] > 50:
    print(f"At {hour['time']}, it will be {hour['temp_f']}ºF and cloudy.")
  else:
    print(f"At {hour['time']}, it will be {hour['temp_f']}ºF.")


# # 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[22]:


count = 0


# In[23]:


for hour in mia_weather['forecast']['forecastday'][0]['hour']:
  if hour['temp_f'] > 85:
    count = count + 1
print(f"{round(count/24*100,2)}% of the next 24-ish hours in Miami will be above 85ºF.")


# ## 9) What was the temperature in Central Park on Christmas Day, 2020? How about 2012? 2007? How far back does the API allow you to go?
# 
# - *Tip: You'll need to use latitude/longitude. You can ask Google where Central Park is, it knows*
# - *Tip: Remember when latitude/longitude might use negative numbers*

# In[24]:


# I can't access this via the free version o(TヘTo)

