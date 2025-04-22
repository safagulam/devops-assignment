from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Setup
driver = webdriver.Chrome()
driver.maximize_window()

# Replace with the URL you want to test
driver.get("file:///C:/portfolio/safa.html")
time.sleep(2)  # Wait for the page to load

# Define tags you want to test
tags_to_check = ['input', 'button', 'a', 'img', 'select', 'textarea', 'label', 'div', 'span']

print(f"\n🔍 Testing Web Elements on {driver.current_url}:\n")

for tag in tags_to_check:
    elements = driver.find_elements(By.TAG_NAME, tag)
    print(f"\n📌 Found {len(elements)} <{tag}> elements\n")
    
    for idx, el in enumerate(elements, start=1):
        try:
            is_visible = el.is_displayed()
            text = el.text.strip() or el.get_attribute('value') or el.get_attribute('alt') or "<no text>"
            print(f"  {idx}. <{tag}> | Text: '{text}' | Visible: {is_visible}")
        except Exception as e:
            print(f"  {idx}. <{tag}> | Error accessing element: {e}")

# Done
print("\n✅ Test completed.\n")
driver.quit()
