import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com")

laptops = []

# Click on "Laptops" section
driver.find_element(By.LINK_TEXT, "Laptops").click()
time.sleep(3)

while True:
    products = driver.find_elements(By.CLASS_NAME, "card-block")

    for product in products:
        name = product.find_element(By.TAG_NAME, "h4").text.strip()
        price = product.find_element(By.TAG_NAME, "h5").text.strip()
        description = product.find_element(By.CLASS_NAME, "card-text").text.strip()

        laptops.append({
            "name": name,
            "price": price,
            "description": description
        })

    try:
        next_button = driver.find_element(By.ID, "next2")
        if "disabled" in next_button.get_attribute("class"):
            break
        next_button.click()
        time.sleep(3)
    except:
        break

driver.quit()

with open("laptops.json", "w", encoding="utf-8") as file:
    json.dump(laptops, file, indent=4, ensure_ascii=False)

print("Laptop data saved to laptops.json")
