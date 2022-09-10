import requests
import json
r = requests.get("https://us-central1-costplusdrugs-publicapi.cloudfunctions.net/main").json()
for x in r["results"]:

    

    drug = x['medication_name']
    print(drug)
    if '/' in drug:
        drug = drug.split('/')[0] + '-' + drug.split('/')[1]
        print(drug)
    dosage = x['strength']
    form = x['pill_nonpill']
    if form == 'Nonpill':
        form = ''
    quantity = 1
    sortType = "price"


    website = 'https://www.goodrx.com/'+drug+'?dosage='+str(dosage)+'mcg&form='+form+'&quantity='+str(quantity)+'&sort_type='+sortType
    #print(website)