# ---------------------------------------------------------------------------------
# This module was loaded in https://t.me/SharkUBmodules_bot
# Licensed under the GNU GPLv3.
# Owner of https://t.me/SharkUBmodules_bot doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------

import openai
import configparser
from pyrogram import Client, filters
from sharkub.settings.main_settings import module_list, file_list

from sharkub.settings.prefix import my_prefix
prefix = my_prefix()

config = configparser.ConfigParser()
config.read("config.ini")

def get_gpt_token():
    tok = config.get("ChatGPT", "gpt_token")
    return tok

@Client.on_message(filters.command('gpt_img', prefixes=prefix) & filters.me)
async def iiimg(client, message):
  await message.edit(f"<b>ChatGPT creating image wait...</b>")
  try:   
    openai.api_key = get_gpt_token()
    prompt = message.text[9:]
    if prompt.strip() == "":
        await message.edit(f"<b>Use <code>{prefix}gpt_img</code> [text for image]</b>")
        return
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
  except:
    await message.edit(f"<b>Token is invalid, change it!</b>\n<code>{prefix}gpt_token</code> <b>[Token]</b>")  
    return
  await client.send_photo(message.chat.id, image_url, caption=f"<b>ChatGPT: <code>{message.text[9:]}</code></b>")
  await message.delete()       

@Client.on_message(filters.command('gpt', prefixes=prefix) & filters.me)
async def ii(client, message): 
  await message.edit(f"<b>ChatGPT thinking wait...</b>")    
  try:
    openai.api_key = get_gpt_token()
    text = message.text[6:]
    response = openai.Completion.create( 
     engine="text-davinci-003", 
     prompt='"""{}\n"""'.format(text), 
     temperature=0, 
     max_tokens=1200, 
     top_p=1, 
     frequency_penalty=0, 
     presence_penalty=0, 
     stop=['"""'])
  except:
    await message.edit(f"Token is invalid, change it!\n<code>{prefix}gpt_token</code> <b>[Token]</b>")
    return
  await message.edit(f'<b>ChatGPT:</b>{response["choices"][0]["text"]}\n\n<b><emoji id=5819167501912640906>❔</emoji> Your question to ChatGPT:</b> <i>{message.text[6:]}</i>') 

@Client.on_message(filters.command('gpt_token', prefixes=prefix) & filters.me)
async def gpt_token(client, message):
  try:  
    await message.edit("<b>Changing token wait...</b>")
    tok = message.text[11:]
    openai.api_key = tok
    response = openai.Completion.create( 
     engine="text-davinci-003", 
     prompt='"""{}\n"""'.format("hi"), 
     temperature=0, 
     max_tokens=1200, 
     top_p=1, 
     frequency_penalty=0, 
     presence_penalty=0, 
     stop=['"""'])
    config.set("ChatGPT", "gpt_token", tok) 
    with open("config.ini", "w") as config_file:
        config.write(config_file)
    await message.edit(f"<b>Token succesfully changed!</b>")
  except:
    await message.edit(f"<b>Token is invalid!</b>")      

@Client.on_message(filters.command('gpt_check', prefixes=prefix) & filters.me)
async def change(client, message):
  try:  
    await message.edit("<b>Checking token works...</b>")
    tok = message.text[11:]
    openai.api_key = tok
    response = openai.Completion.create( 
     engine="text-davinci-003", 
     prompt='"""{}\n"""'.format("hi"), 
     temperature=0, 
     max_tokens=1200, 
     top_p=1, 
     frequency_penalty=0, 
     presence_penalty=0, 
     stop=['"""'])
    await message.edit(f"<b>Token (<code>sk-...{tok[35:]}</code>) works!</b>")
  except:
    await message.edit(f"<b>Token is invalid!</b>")      

module_list["ChatGPT"] = {
"gpt [text]": "Ask something in ChatGPT",
"gpt_token [new_token]": "Change ChatGPT token",
"gpt_img [text]": "ChatGPT draw image",
"gpt_check [token]": "Check for ChatGPT token works",
}
file_list["ChatGPT"] = "chatgpt.py"
