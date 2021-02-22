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
