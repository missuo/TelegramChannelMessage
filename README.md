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
**You can download this repository and have obtained the code.**

**Please modify the key information in the code before running the code, such as appid,api_hash,apptitle,channel_url etc.**

## Start crawling
1. First you have to enter the directory of the .py file, and then execute the following code: 

Crawl text, pictures, and files of channel messages
```
python3 normal.py
```

Crawl all pictures of Telegraph
```
python3 telegraph.py
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
