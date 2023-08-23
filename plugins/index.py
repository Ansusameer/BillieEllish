import logging
import asyncio
import re
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, ChatAdminRequired, UsernameInvalid, UsernameNotModified
from info import ADMINS
from info import INDEX_REQ_CHANNEL as LOG_CHANNEL
from database.ia_filterdb import save_file
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import temp

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
lock = asyncio.Lock()

app = Client("my_account")

@app.on_callback_query(filters.regex(r'^index'))
async def index_files(bot, query):
    if query.data.startswith('index_cancel'):
        temp.CANCEL = True
        await query.answer("Cancelling Indexing")
        return

    _, raju, chat, lst_msg_id, from_user = query.data.split("#")

    if raju == 'reject':
        await query.message.delete()
        await bot.send_message(int(from_user), f'Your Submission for indexing {chat} has been declined by our moderators.', reply_to_message_id=int(lst_msg_id))
        return

    async with lock:
        await query.answer('Processing...⏳', show_alert=True)

        if int(from_user) not in ADMINS:
            await bot.send_message(int(from_user), f'Your Submission for indexing {chat} has been accepted by our moderators and will be added soon.', reply_to_message_id=int(lst_msg_id))

        msg = query.message
        await msg.edit("Starting Indexing", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Cancel', callback_data='index_cancel')]]))
        
        try:
            chat = int(chat)
        except ValueError:
            pass

        await index_files_to_db(int(lst_msg_id), chat, msg, bot)

# ... (other functions remain the same)

@app.on_message((filters.forwarded | (filters.regex("(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")) & filters.text ) & filters.private & filters.incoming)
async def send_for_index(_, message):
    # ... (remaining code remains the same)
    
@app.on_message(filters.command('setskip') & filters.user(ADMINS))
async def set_skip_number(_, message):
    if ' ' in message.text:
        _, skip = message.text.split(" ")
        try:
            skip = int(skip)
            temp.CURRENT = int(skip)
            await message.reply(f"Successfully set SKIP number as {skip}")
        except ValueError:
            await message.reply("Skip number should be an integer.")
    else:
        await message.reply("Give me a skip number")

async def index_files_to_db(lst_msg_id, chat, msg, bot):
    total_files = 0
    duplicate = 0
    errors = 0
    deleted = 0
    no_media = 0
    unsupported = 0

    await msg.edit_text("Starting Indexing",
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Cancel', callback_data='index_cancel')]])
                        )
    
    async with lock:
        try:
            current = temp.CURRENT
            temp.CANCEL = False

            async for message in bot.iter_messages(chat, lst_msg_id, temp.CURRENT):
                if temp.CANCEL:
                    await msg.edit_text(f"Successfully Cancelled!!\n\nSaved <code>{total_files}</code> files to dataBase!\nDuplicate Files Skipped: <code>{duplicate}</code>\nDeleted Messages Skipped: <code>{deleted}</code>\nNon-Media messages skipped: <code>{no_media + unsupported}</code>(Unsupported Media - `{unsupported}` )\nErrors Occurred: <code>{errors}</code>",
                                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Cancelled', callback_data='cancelled')]])
                                        )
                    break

                # ... (remaining code remains the same)
        except Exception as e:
            logger.exception(e)
            await msg.edit_text(f'Error: {e}')
        else:
            await msg.edit_text(f'Successfully saved <code>{total_files}</code> to dataBase!\nDuplicate Files Skipped: <code>{duplicate}</code>\nDeleted Messages Skipped: <code>{deleted}</code>\nNon-Media messages skipped: <code>{no_media + unsupported}</code>(Unsupported Media - `{unsupported}` )\nErrors Occurred: <code>{errors}</code>')

# Run the app
app.run()
