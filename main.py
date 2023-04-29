import requests

from bs4 import BeautifulSoup

# Send an HTTP GET request to the website URL

url = 'https://receive-smss.com/sms/19175177576/'

response = requests.get(url)

# Parse the HTML response and extract the text data

soup = BeautifulSoup(response.text, 'html.parser')

message = soup.find('div', class_='sms-text').text.strip()

# Send an HTTPS POST request to the target URL with the extracted text data as parameters

target_url = 'https://tempnumber.biz/api/receive/76gblrpovfcweh9stnjym8axuqkdi/'

params = {

    'to': '+1XXXXXXXXXX',   # Replace with the actual phone number to which the message is sent

    'from': '+1XXXXXXXXXX', # Replace with the actual phone number from which the message is sent

    'msg': message,

    'uuid': '12345'         # Replace with a unique ID of the message

}

response = requests.post(target_url, data=params, verify=True)

# Verify the HTTPS response and handle any errors that occur

if response.status_code == 200:

    print('Data sent successfully.')

else:

    print('Error occurred:', response.status_code)

