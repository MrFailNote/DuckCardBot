import config
import asyncio
import random as r
import os
import tracemalloc

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(config.token)
tracemalloc.start()

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)

@bot.message_handler(commands=['toss'])
async def coin_toss(message):
    await bot.reply_to(message,r.choice(["Выпал орёл","Выпала решка"]))
    
@bot.message_handler(content_types=['photo'])
async def photo_id(message):
    photo = max(message.photo, key=lambda x: x.height)
    await bot.reply_to(message, photo)
    
@bot.message_handler(commands=['ducks'])
async def duck_pics(message):
    rarity = r.randint(1,100)
    if 1<=rarity<=45:
        typi = r.choice(os.listdir('Common ducks'))
        with open(f'Common ducks/{typi}', 'rb') as duck:
            await bot.send_photo(message.chat.id, duck)
    elif 46<=rarity<=70:
        typi = r.choice(os.listdir('Uncommon ducks'))
        with open(f'Uncommon ducks/{typi}', 'rb') as duck:
            await bot.send_photo(message.chat.id, duck)
    elif 71<=rarity<=85:
        typi = r.choice(os.listdir('Rare ducks'))
        with open(f'Rare ducks/{typi}', 'rb') as duck:
            await bot.send_photo(message.chat.id, duck)
    elif 86<=rarity<=94:
        typi = r.choice(os.listdir('Epic ducks'))
        with open(f'Epic ducks/{typi}', 'rb') as duck:
            await bot.send_photo(message.chat.id, duck)
    elif 95<=rarity<=99:
        typi = r.choice(os.listdir('SuperEpic ducks'))
        with open(f'SuperEpic ducks/{typi}', 'rb') as duck:
            await bot.send_photo(message.chat.id, duck)
    elif rarity==100:
        typi = r.choice(os.listdir('Legendary ducks'))
        with open(f'Legendary ducks/{typi}', 'rb') as duck:
            await bot.send_photo(message.chat.id, duck)
        
    

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


asyncio.run(bot.polling())