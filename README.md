# WhatsAppBrodcaster
Automate bulk message sending on WhatsApp using Selenium!

# How to Setup
1. Clone the project and make sure you have a [Python Runtime](https://code.visualstudio.com/docs/languages/python)
2. Download ChromeDriver. It is needed in order for the script to be able to open and use Google Chrome.
Find the compatible version [here](https://googlechromelabs.github.io/chrome-for-testing/)
3. Once you picked and downloaded your compatible version, place chromedriver.exe into your root directory, right next to the script you cloned.
4. Last and most important - your contact list. 
In order to use the script the contacts have to be saved on your phone by the same names as in the contact list. This is because using a normal whatsapp brodcast list won't send the message to the recipient if you are not saved on their phone. The script bypasses that by sending each contact on the list a private message.

To save the contact list on your phone in one click I reccomend google contacts. Use the 'Import contacts' feature and pick the csv file, then connect your phone to the app and boom, all contacts saved on your phone!

# How to use
The script takes two inputs:
- a .txt file containing the message you want to send to your clients
- a .csv file containing the list of contact names for which you want to brodcast the message. the format needed for the csv file is a column called 'name' and values for each contact.

Once all that is done, all thats left is running the script, filling the console promts
and enjoy the hours of manual work saved!