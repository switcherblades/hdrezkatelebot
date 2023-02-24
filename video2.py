from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Replace YOUR_BOT_TOKEN with your actual bot token
bot = Bot(token='6013880767:AAGb9y8JrgrrYzcSgkr1lFDxc7tisYFFg0E')
dp = Dispatcher(bot)

# Replace YOUR_VIDEO_LINK with the link to your video
VIDEO_NOTE_URL = 'https://stream.voidboost.cc/943d0801adba890c468f7a263098c7f0:2023022420:UVRUMW5yM0U3RTVnUnZ6ZDEzT3dHSHlsTW5sNWF4MDhTUDVQUCt1elF2UmYxUjQ0VmRxVnhxVEgxQndkalRBc3FnQXdPdE1BVVVSYzNVcDArbmlJUEE9PQ==/4/7/3/2/4/4/ncwse.mp4'

async def send_video_note(chat_id):
    # Send the video note to the chat
    video_note = types.InputFile(VIDEO_NOTE_URL)
    await bot.send_video_note(chat_id, video_note)

@dp.message_handler(commands=['send_video_note'])
async def cmd_send_video_note(message: types.Message):
    chat_id = message.chat.id
    await send_video_note(chat_id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
