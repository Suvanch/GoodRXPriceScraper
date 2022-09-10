#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

import undetected_chromedriver.v2 as uc
driver=uc.Chrome()
driver.get('https://www.goodrx.com/dofetilide?dosage=125mcg&form=capsule&label_override=dofetilide&quantity=60&sort_type=popularity')
soup=bs(driver.page_source,'html.parser')

#cmp=[]
soup=bs(driver.page_source,'html.parser')
uls=soup.find('ul',{'aria-label':'List of best coupons by price and pharmacy.'}).findAll('li')
for ul in uls:
    loc=ul.find('div',class_='container-DmX7P').text.strip()
    price=ul.find('div',class_='container-1yeEg').text.strip()
    fnl={
        'size':'500 mcg',
        'Amount':'180 Capsules',
        'location':loc,
        'Price':price
    }
    #print(fnl)
    cmp.append(fnl)
    df=pd.DataFrame(cmp)
df.to_excel('data.xlsx',index=False)




# %%
