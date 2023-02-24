# Import required libraries

from aiogram import Bot, Dispatcher, executor, types # type: ignore
from aiogram.utils import executor  # type: ignore
from HdRezkaApi import *

# Create a bot instance
bot = Bot(token='6013880767:AAGb9y8JrgrrYzcSgkr1lFDxc7tisYFFg0E')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Referer': 'https://rezka.ag/',
    'Origin': 'https://rezka.ag',
    'X-Requested-With': 'XMLHttpRequest'
}
# Create a dispatcher instance
dp = Dispatcher(bot)


# Define a command handler to greet the user and prompt them to send a string
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Hello! Please send me a string.")


# Define a message handler to handle text messages
@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text(message: types.Message):
    # Get the text message from the user
    text = message.text
    url = 'https://rezka.ag/search/'
    # Save the text message to a variable
    search_text = text

    search_response = requests.get(url, headers=headers, params={'do': 'search',
                                                                 'subaction': 'search',
                                                                 'q': search_text}).content
    search_data = BeautifulSoup(search_response, 'html.parser')
    results = search_data.select('div.b-content__inline_item')
    a_tags = results[0].find('a')
    href = a_tags.get('href')
    rezka = HdRezkaApi(href)
    media = rezka.getStream()('720p')
    media ='https://static.hdrezka.ac/i/2022/1/22/u753ae83b328aws90n57c.jpeg'
    video = URLInputFile(
        media,
        filename="img.jpeg"
    )
    # Send a confirmation message to the user
    #await message.reply(f"{rezka.getStream()('720p')}")
    await message.reply(f"{video}")

# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
