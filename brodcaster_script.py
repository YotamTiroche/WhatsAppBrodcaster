from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time, csv

# Setup Variables
message_filename = input('Please enter message filename (txt file only)') 
contacts_filename = input('Please enter contacts list filename (csv file only)')

# Pre-written function used to paste content using JS (required when using chrome)
def paste_content(driver, el, content): 
    driver.execute_script( 
    f'''
    const text = `{content}`;
    const dataTransfer = new DataTransfer();
    dataTransfer.setData('text', text);
    const event = new ClipboardEvent('paste', {{
    clipboardData: dataTransfer,
    bubbles: true
    }});
    arguments[0].dispatchEvent(event)
    ''', el)

# Parse message file into a string variable
with open(message_filename, 'r', encoding='utf-8') as file:
    message = file.read()

# Start chrome and open whatsapp web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
input("Scan the QR code and press Enter after you're logged in.")

# Parse Contact CSV file into a dictionary
with open(contacts_filename, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    contacts = [] # Initialize an empty list to store filtered data
    for row in reader:
        name = row['Name']
        if name.strip():  # Check if the name is neither empty or whitespace
            contacts.append(name)

# Set Counters
sucsessful_count = 0
failed_count = 0

# Loop through the contacts and send messages
for contact in contacts:
    search_box = driver.find_element(By.CSS_SELECTOR, "#side > div._3gYev > div > div > div._2vDPL > div > div.to2l77zo.gfz4du6o.ag5g9lrv.bze30y65.kao4egtt.qh0vvdkp > p")
    search_box.clear()
    search_box.send_keys(contact)
    time.sleep(1)  # Wait for the search results to load
    search_box.send_keys(Keys.ENTER)
    time.sleep(1)  # Wait for the chat to load
    try:
        contact_box = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[title="' + contact + '"]'))).click()
        time.sleep(3)  # Add a delay to avoid rapid sending
        # Select the message box and send the message
        message_box = driver.find_element(By.CSS_SELECTOR, "#main > footer > div._2lSWV._3cjY2.copyable-area > div > span:nth-child(2) > div > div._1VZX7 > div._3Uu1_ > div > div.to2l77zo.gfz4du6o.ag5g9lrv.bze30y65.kao4egtt > p")
        
        #paste_content(driver, message_box, message)
        ActionChains(driver).send_keys_to_element(message_box, message).perform()
        time.sleep(3)
        message_box.send_keys(Keys.ENTER)
        sucsessful_count = sucsessful_count + 1
        time.sleep(3)
    except:
        print("Contact not found: " + contact)
        search_box.send_keys(Keys.CONTROL + "a")
        search_box.send_keys(Keys.DELETE)
        failed_count = failed_count + 1
        continue


# Close the browser
time.sleep(10)
print(f'Sucsessfully sent message to {sucsessful_count} Clients!')
print(f'Couldn\'t send message to {failed_count} Clients!')
driver.quit()
