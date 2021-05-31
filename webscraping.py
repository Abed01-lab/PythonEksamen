from re import T
from bs4 import BeautifulSoup as soup
import requests
import time

base_url = "https://versus.com/da/phone"
r = requests.get(base_url)
page_soup = soup(r.content, "html.parser")
products = page_soup.findAll("a", {"List__link___1UGZQ"})


filename = "mobil_telefoner.csv"
f = open(filename, "w")
headers = "product_name,product_display,product_camera,product_storage,product_ram,product_battery,product_price\n"

f.write(headers)
i = 1
for product in products:
    url= "https://versus.com" + product["href"]
    r = requests.get(url)
    page_soup = soup(r.content, "html.parser")
    print("https://versus.com" + product["href"])

    time.sleep(3)

    title_content = page_soup.find("div", {"class" : "nameContainer"})
    product_title = title_content.p.text

    display_content = page_soup.find("div", {"id" : "group_display"})
    display_specs = display_content.findAll("div", {"class" : "Property__property___1PAON"})

    preformence_content = page_soup.find("div", {"id" : "group_performance"})
    preformence_specs = preformence_content.findAll("div", {"class" : "Property__property___1PAON"})

    camera_content = page_soup.find("div", {"id" : "group_cameras"})
    camera_specs = camera_content.findAll("div", {"class" : "Property__property___1PAON"}) 

    battery_content = page_soup.find("div", {"id" : "group_battery"})
    battery_specs = battery_content.findAll("div", {"class" : "Property__property___1PAON"})

    price_content = page_soup.find("span", {"class" : "natural PriceTag__natural___3Ripa"})

    if price_content != None:
        price = price_content.em.text.strip().strip(".").replace(",", "")
        product_price = str(int(price) * 7.5)
    else:
        product_price = 0


    for spec in display_specs:
        value_container = spec.find("div", {"class" : "Value__value___qfSvr number"})
        text_container = spec.find("a", {"class" : "Property__propertyLabel___3GatO"}).find("span", {"Property__label___33tiu"})

        if value_container != None:
            if text_container.text.strip() == "skærmstørrelse":
                product_display = value_container.p.text.strip().strip('"')


    for spec in preformence_specs:
        value_container = spec.find("div", {"class" : "Value__value___qfSvr number"})
        text_container = spec.find("a", {"class" : "Property__propertyLabel___3GatO"}).find("span", {"Property__label___33tiu"})

        if value_container!= None:
            if text_container.text.strip() == "indbygget hukommelse":
                product_storage = value_container.p.text.strip().strip("GB")

            if text_container.text.strip() == "RAM":
                product_RAM = value_container.p.text.strip().strip("GB")


    for spec in camera_specs:
        value_container = spec.find("div", {"class" : "Value__value___qfSvr number"})
        text_container = spec.find("a", {"class" : "Property__propertyLabel___3GatO"}).find("span", {"Property__label___33tiu"})

        if value_container != None:
            if text_container.text.strip() == "megapixels (primære kamera)":
                sum = 0
                camera_container = value_container.p.text.split("&")
                for mp in camera_container:
                    number = mp.strip("MP ").replace(" ", "")
                    sum = sum + float(number)
                product_camera =  str(sum)
 

    for spec in battery_specs:
        value_container = spec.find("div", {"class" : "Value__value___qfSvr number"})
        text_container = spec.find("a", {"class" : "Property__propertyLabel___3GatO"}).find("span", {"Property__label___33tiu"})

        if value_container != None:
            if text_container.text.strip() == "batterikraft":
                product_battery = value_container.p.text.strip().strip("mAh")

    print("nr : ", i, ", Titel : " , product_title, ", display : ", product_display, ", camera : ", product_camera, ", storage : ", product_storage, ", RAM : ", product_RAM, ", price: ", product_price)
    i += 1
    f.write(str(product_title) + "," + str(product_display) + "," + str(product_camera) + "," + str(product_storage) + "," +  str(product_RAM) + "," + str(product_battery) + "," + str(product_price) + "\n")
