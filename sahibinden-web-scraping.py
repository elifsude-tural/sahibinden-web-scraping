import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import csv
import time
from datetime import date

driver = uc.Chrome(version_main=145)
driver.get("https://www.sahibinden.com/kiralik-daire/corum")
time.sleep(10)

rows = driver.find_elements(By.CSS_SELECTOR, "tr.searchResultsItem")
print(f"Toplam ilan: {len(rows)}")

with open(f"corum_{date.today()}.csv", mode="w", newline="", encoding="utf-8-sig") as csvfile:
    yazici = csv.writer(csvfile)
    yazici.writerow(["Date", "Price", "District", "Rooms"])

    for row in rows:
        try:
            price    = row.find_element(By.CSS_SELECTOR, ".searchResultsPriceValue").text.strip()
            location = row.find_element(By.CSS_SELECTOR, ".searchResultsLocationValue").text.strip()
            attrs    = row.find_elements(By.CSS_SELECTOR, ".searchResultsAttributeValue")
            rooms    = attrs[1].text.strip()

            yazici.writerow([date.today(), price, location, rooms])
            print(f"{location} | {rooms} | {price}")
        except Exception as e:
            print(f"Hata: {e}")
            continue

print("CSV kaydedildi!")
driver.quit()
