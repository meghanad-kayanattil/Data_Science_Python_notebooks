"""
Author : Meghanad

"""

from bs4 import BeautifulSoup
import requests

i = 1

price_all = []
area_all = []
room_all = [] 
while i != 31:
      url = f'https://www.immowelt.de/liste/hamburg/wohnungen/mieten?sort=relevanz&sp={i}'
      print(url)
      i = i + 1
      

      page = requests.get(url)
      print(page)

      soup = BeautifulSoup(page.content, 'html.parser')
        #print(soup())

      
      lists = soup.find_all('div', class_='KeyFacts-efbce')

      price = soup.find_all('div', attrs={"data-test":"price"})
      area = soup.find_all('div', attrs = {'data-test':'area'})
      rooms = soup.find_all('div', attrs = {'data-test':'rooms'}) 
      

      for p, a, r in zip(price, area, rooms):
          print(f'{p.text} {a.text} {r.text}')
          
          price_all.append(p.text)
          area_all.append(a.text)
          room_all.append(r.text)
          
file = open('housing_data_hamburg.txt', 'w+')

head = 'Area'+'\t'+'Rooms'+'\t'+'Rent'+'\n'

file.write(head)
for p, a, r in zip(price_all, area_all, room_all):
    file.write(str(a)+'\t'+str(r)+'\t'+str(p)+'\n')
file.close()



    
