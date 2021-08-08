from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

req = requests.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1")

content = req.content

soup = BeautifulSoup(content,'html.parser')

desc = soup.find_all('div' , class_='_4rR01T')

descriptions = []
for i in range(len(desc)):
    descriptions.append(desc[i].text) # We can even access the child tags with dot access.

commonclass = soup.find_all('li', class_='rgWa7D')  # We observe that the classnames for the different specifications are under one div.So we need to apply some method to extract the different features.

# Create empty lists for the features
processors = []
ram = []
os = []
storage = []
inches = []
warranty = []

for i in range(0, len(commonclass)):
    p = commonclass[i].text  # Extracting the text from the tags
    if ("Core" in p):
        processors.append(p)
    elif (
            "RAM" in p):  # If RAM is present in the text then append it to the ram list. Similarly do this for the other features as well
        ram.append(p)
    elif ("HDD" in p or "SSD" in p):
        storage.append(p)
    elif ("Operating" in p):
        os.append(p)
    elif ("Display" in p):
        inches.append(p)
    elif ("Warranty" in p):
        warranty.append(p)

# print(len(processors))
# print(len(warranty))
# print(len(os))
# print(len(ram))
# print(len(inches))


price = soup.find_all('div',class_='_30jeq3 _1_WHN1') # Extracting price of each laptop from the website
prices = []
for i in range(len(price)):
    prices.append(price[i].text)
# print(prices)

original_price = soup.find_all('div',class_='_3I9_wc _27UcVY')
# print(original_price)

original_prices = []
for i in range(len(original_price)):
    original_prices.append(original_price[i].text)
# print(original_prices)
# len(original_prices)


rating = soup.find_all('div',class_='_3LWZlK') # Extracting the ratings of all the laptops
ratings = []
for i in range(len(rating)):
    ratings.append(rating[i].text)
# print(ratings)
# len(ratings)


discount = soup.find_all('span')

discounts = []
for i in range(0,len(discount)):
    p=discount[i].text
    if("% off" in p): # Extracting the tags which contain the discount(all the discounts contain % off so checking with that condition we obtain all the laptops which have discounts)
        discounts.append(p)
# print(discounts)
# len(discounts)

# print("Description - ",len(descriptions))
# print("Processor - ",len(processors))
# print("RAM - ",len(ram))
# print("Operating System - ",len(os))
# print("Storage - ",len(storage))
# print("Display - ",len(inches))
# print("Warranty - ",len(warranty))
# print("Price - ",len(prices))
#
# for i in range(len(descriptions)):
#     print(descriptions[i])
# print(descriptions)

d = {'Description':descriptions,'Processor':processors,'RAM':ram,'Operating System':os,'Storage':storage,'Display':inches,'Warranty':warranty,'Price':prices}
dataset = pd.DataFrame(data = d)

# print(dataset)

dataset.to_csv('laptops.csv')
