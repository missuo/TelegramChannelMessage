from telethon import TelegramClient, utils
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterDocument

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
