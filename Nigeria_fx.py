#!/usr/bin/env python
# coding: utf-8

# In[13]:
import requests
import pandas as pd
from bs4 import BeautifulSoup 
import datetime
import os


# In[17]:


# API endpoint (replace with the exact URL you found)
URL = "https://www.cbn.gov.ng/api/GetAllExchangeRatesGRAPH"

Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

scrape_time = datetime.date.today().isoformat()
file_path = "Nigeria_fx.csv"

# Step 1: Fetch JSON
response = requests.get(URL, headers=Headers)
data = response.json()
df_new = pd.DataFrame(data)

# Step 2: Keep only major currencies
major_currencies = ["US DOLLAR", "POUNDS STERLING", "EURO", "YUAN/RENMINBI","RIYAL","YEN"]
df_new = df_new[df_new["currency"].isin(major_currencies)]

# Add scrape timestamp
df_new["scrape_date"] = scrape_time

# Step 3: Load old dataset if exists
if os.path.exists(file_path):
    df_old = pd.read_csv(file_path)
    df = pd.concat([df_old, df_new], ignore_index=True)
else:
    df = df_new.copy()

# Step 4: Drop duplicates (keep the last scrape if conflict)
df = df.drop_duplicates(subset=["ratedate", "currency"], keep="last")

# Step 5: Save cleaned dataset
df.to_csv(file_path, index=False)


# In[ ]:





# In[25]:






# In[ ]:




