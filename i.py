import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from openpyxl import load_workbook
import undetected_chromedriver.v2 as uc


def pullEveryting(soup):
    cmp=[]
    uls=soup.find('ul',{'aria-label':'List of best coupons by price and pharmacy.'}).findAll('li')
    for ul in uls:
        loc=ul.find('div',class_='container-DmX7P').text.strip()
        price=ul.find('div',class_='container-1yeEg').text.strip()
        fnl={
            'Drug': drug,
            'Label Override':labelOverride,
            'Dosage': str(dosage)+' mcg',
            'Form':form,
            'Quantity':str(quantity)+' Capsules',
            'location':loc.split(": ")[1][:-1],
            'Price':price.split(".w")[0].split("is")[1]
        }
        print(fnl)
        cmp.append(fnl)
    df=pd.DataFrame(cmp)
    df.to_csv('data.csv',mode='a',index=False)

def pullWebData(soup):
    webForm=soup.find('div', {'id': 'uat-dropdown-form'}).text
    print(webForm)

    webBrand=soup.find('div', {'id': 'uat-dropdown-brand'}).text
    print(webBrand)


    webQuantity=soup.find('div', {'id': 'uat-dropdown-quantity'}).text
    print(webQuantity)

    webConcentration=soup.find('div', {'id': 'uat-dropdown-dosage'}).text
    print(webConcentration)


if __name__ == '__main__': 
    driver=uc.Chrome()
    drug = 'dofetilide'
    dosage = 434
    form = "capsule"
    labelOverride = "dofetilide"
    quantity = 60
    sortType = "price"

    
    website = 'https://www.goodrx.com/'+drug+'?dosage='+str(dosage)+'mcg&form='+form+'&label_override='+labelOverride+'&quantity='+str(quantity)+'&sort_type='+sortType
    driver.get(website)

    soup=bs(driver.page_source,'html.parser')
    

    pullWebData(soup)
        
    pullEveryting(soup)