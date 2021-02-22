# TelegramChannelMessage
Crawling of Telegram channel messages

## Features
- [x] Plain text message
- [x] Picture message
- [x] File message
- [x] Telegraph message
- [ ] Support groups
- [ ] Support personal chat

## Ready to work
### Telegram Apps
* App api_id
* App api_hash
* App title

### Operating environment
* Python 3.7 or higher
* lxml
* requests
* bs4
* telethon

If you do not have these environments, you can install with the following code:
```shell
pip3 install lxml requests bs4 telethon
```

## Code
```python
from telethon import TelegramClient, utils
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterDocument
import requests
import re
from bs4 import BeautifulSoup
import os

api_id = [YOURAPPID]
api_hash = '[YOURAPIHASH]'
client = TelegramClient('[YOURAPPTITLE]', api_id, api_hash)
channel = '[YOURCHANNELURL]' # EXAMPLE: https://t.me/douban_read

async def main():
    # PLAIN TEXT MESSAGES
    print('Plain text message')
    messages = client.iter_messages(channel, limit=100) # Only 100 downloads, you can modify or delete the limit
    msges = '';
    async for message in messages:
        msg = str(message.date) + '[' + str(utils.get_display_name(message.sender)) + ':' + str(message.message) + ']\n'
        print(msg)
        msges = msges + msg
    with open('./telegram/messages.text', 'w') as file:
        file.write(msges)
    
    # PICTURE MESSAGES
    print('Picture message')
    photos = await client.get_messages(channel, None, filter=InputMessagesFilterPhotos)

    total = len(photos)
    index = 0
    for photo in photos:
        filename = "./telegram/" + str(photo.id) + ".jpg"
        index = index + 1
        print("downloading:", index, "/", total, " : ", filename)
        await client.download_media(photo, filename)
    # FILE MESSAGES
    print('File message')
    files = await client.get_messages(channel, None, filter=InputMessagesFilterDocument)

    for file in files:
        attributes = file.media.document.attributes
        if len(attributes) == 1:
            fileName = file.media.document.attributes[0].file_name
            print(fileName)
        if len(attributes) == 2:
            fileName = file.media.document.attributes[1].file_name
            print(fileName)
        await client.download_media(file, "./telegram/" + fileName)

with client:
    client.loop.run_until_complete(main())
```

If you want to crawl all the photos in the Telegraph that push the Telegraph link channel, you can do this:
```python
from telethon import TelegramClient, utils
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterDocument
import requests
import re
from bs4 import BeautifulSoup
import os

api_id = [YOURAPPID]
api_hash = '[YOURAPIHASH]'
client = TelegramClient('[YOURAPPTITLE]', api_id, api_hash)
channel = '[YOURCHANNELURL]' # EXAMPLE: https://t.me/douban_read

async def main():
    messages = client.iter_messages(channel)
    async for message in messages:
        try:
            message_name = str(message.message)
            #print(message.media.webpage.url) 
            telegraph_url = str(message.media.webpage.url)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400'}
            response = requests.get(telegraph_url, headers=headers)
            html = response.text
            bs = BeautifulSoup(html,"lxml")
            img_ls = bs.find_all('img')
            img_amount = len(img_ls)
            print("The download is ",message_name)
            os.makedirs(message_name,exist_ok=True)
            for i in range(0,img_amount):
                img_url_old = img_ls[i].get('src')
                img_url = "https://telegra.ph" + img_url_old
                src = requests.get(img_url,headers=headers).content
                with open(message_name + "/" + str(i+1) + '.jpg','wb') as f:
                    f.write(src)
                print("The file being downloaded is ",message_name,"Photo",str(i+1),str(img_amount-i-1),"Left")
                #print(img_url)
        except:
            pass
with client:
    client.loop.run_until_complete(main())
```

## Start crawling
1. First you have to enter the directory of the .py file, and then execute the following code:
```shell
python3 py-craw.py
```

2. Next, you will be prompted to enter your mobile phone number bound to Telegram.
```
Please enter your phone (or bot token): +18032330633
```

3. You will receive a verification code message from Telegram.
```
Login code: 12345. Do not give this code to anyone, even if they say they are from Telegram!

This code can be used to log in to your Telegram account. We never ask it for anything else.

If you didn't request this code by trying to log in on another device, simply ignore this message.
```

4. Enter the verification code to complete the login.
```
Please enter the code you received: 12345
```
