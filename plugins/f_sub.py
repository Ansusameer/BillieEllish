from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils import not_subscriber
import re

TEXT = """
🔆 ᴘʟᴇᴀsᴇ ғᴏʟʟᴏᴡ ᴛʜɪs ʀᴜʟᴇs 🔆

ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ ʏᴏᴜ. ♻️

ʏᴏᴜ ᴡɪʟʟ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ᴏғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ ғɪʀsᴛ.

ᴛʜᴇɴ ᴏɴʟʏ ʏᴏᴜ ɢᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ."""

@Client.on_message(filters.create(not_subscriber))
async def is_not_subscribed(client, message):
    if message.text.startswith('/'): 
        buttons = [[
            InlineKeyboardButton(text="🏮Main Channel ⟨Click Here⟩", url="https://t.me/+eP4R_u-ZXeIyZTY1")
        ] , [
            InlineKeyboardButton(text="🔆彡⟨ AVAFLiX ⟩彡🔆" , url="https://t.me/AvaflixOfficial")
        ]]
        await message.reply_text(text=TEXT, reply_markup=InlineKeyboardMarkup(buttons))
    elif message.text:
        buttons = [[
            InlineKeyboardButton(text="🏮Main Channel ⟨Click Here⟩" , url="https://t.me/+eP4R_u-ZXeIyZTY1")
        ] , [
            InlineKeyboardButton(text="🔆彡⟨ AVAFLiX ⟩彡🔆" , url="https://t.me/AvaflixOfficial")
        ]]
        await message.reply_text(text=TEXT , reply_markup=InlineKeyboardMarkup(buttons))
    else:
        return
