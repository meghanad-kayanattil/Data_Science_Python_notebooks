"""
Author : Meghanad

"""

from bs4 import BeautifulSoup
import requests

i = 1
price_all = []
area_all = []
room_all = []
districts = []

while i != 45:
    # url = f'https://www.immowelt.de/liste/hamburg/wohnungen/mieten?sort=relevanz&sp={i}'
    url = (
        f"https://www.immowelt.de/liste/hamburg/wohnungen/mieten?d=true&sd=DESC&sf=TIMESTAMP&sp={i}"
    )
    print(f"page number = {i}")
    i = i + 1
    page = requests.get(url)
    # print(page)
    # Getting the data from the website
    soup = BeautifulSoup(page.content, "html.parser")
    # print(soup())
    # Finding all data belonging to the class keyfacts*
    # lists = soup.find_all('div', class_='KeyFacts-efbce')
    price = soup.find_all("div", attrs={"data-test": "price"})
    area = soup.find_all("div", attrs={"data-test": "area"})
    rooms = soup.find_all("div", attrs={"data-test": "rooms"})
    for p, a, r in zip(price, area, rooms):
        print(f"{p.text} {a.text} {r.text}")
        p_end = " €"
        r_end = " Zi."
        a_end = " m²"
        price_all.append(p.text[: -len(p_end)])
        area_all.append(a.text[: -len(a_end)])
        room_all.append(r.text[: -len(r_end)])
    list_location = soup.find_all("div", class_="IconFact-e8a23")
    j = 0
    for loc in list_location:
        strip = "location"
        location_tmp = loc.text
        if strip in location_tmp:
            location = location_tmp[len(strip) :]
            before, sep, after = location.partition("Hamburg")
            start = "("
            end = ")"
            district = after[after.find(start) + len(start) : after.rfind(end)]
            print(f"{j} = {district}")
            j += 1
            districts.append(district)
    # location = soup.find_all('div')
# %% Writing the scraped data into file
file = open("housing_data_hamburg_v4.txt", "w+")

head = "Area" + "\t" + "Rooms" + "\t" + "Location" + "\t" + "Rent" + "\n"

file.write(head)
for p, a, d, r in zip(price_all, area_all, districts, room_all):
    file.write(a + "\t" + r + "\t" + d + "\t" + p + "\n")
file.close()
