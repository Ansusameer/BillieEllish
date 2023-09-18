import io
from pyrogram import filters, Client, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.filters_mdb import(
   add_filter,
   get_filters,
   delete_filter,
   count_filters,
   del_all
)

from database.connections_mdb import active_connection
from utils import get_file_id, parser, split_quotes
from info import ADMINS

@Client.on_message(filters.command(['add']) & filters.incoming & filters.user(ADMINS))
async def addfilter(client, message):
    args = message.text.html.split(None, 1)

    if len(args) < 2:
        await message.reply_text("Command Incomplete :(", quote=True)
        return

    extracted = split_quotes(args[1])
    text = extracted[0].lower()

    if not message.reply_to_message and len(extracted) < 2:
        await message.reply_text("Add some content to save your filter!", quote=True)
        return

    if (len(extracted) >= 2) and not message.reply_to_message:
        reply_text, btn, alert = parser(extracted[1], text)
        fileid = None
        if not reply_text:
            await message.reply_text("You cannot have buttons alone, give some text to go with it!", quote=True)
            return

    elif message.reply_to_message and message.reply_to_message.reply_markup:
        try:
            rm = message.reply_to_message.reply_markup
            btn = rm.inline_keyboard
            msg = get_file_id(message.reply_to_message)
            if msg:
                fileid = msg.file_id
                reply_text = message.reply_to_message.caption.html
            else:
                reply_text = message.reply_to_message.text.html
                fileid = None
            alert = None
        except:
            reply_text = ""
            btn = "[]" 
            fileid = None
            alert = None

    elif message.reply_to_message and message.reply_to_message.media:
        try:
            msg = get_file_id(message.reply_to_message)
            fileid = msg.file_id if msg else None
            reply_text, btn, alert = parser(extracted[1], text) if message.reply_to_message.sticker else parser(message.reply_to_message.caption.html, text)
        except:
            reply_text = ""
            btn = "[]"
            alert = None
    elif message.reply_to_message and message.reply_to_message.text:
        try:
            fileid = None
            reply_text, btn, alert = parser(message.reply_to_message.text.html, text)
        except:
            reply_text = ""
            btn = "[]"
            alert = None
    else:
        return

    await add_filter('filters', text, reply_text, btn, fileid, alert)

    await message.reply_text(
        f"**🆕 Filter** `{text}` **Added ✔**",
        quote=True,
        parse_mode=enums.ParseMode.MARKDOWN
    )

@Client.on_message(filters.command(['filters']) & filters.incoming & filters.user(ADMINS))
async def get_all_filters(client, message):
    texts = await get_filters('filters')
    count = await count_filters('filters')
    if count:
        filterlist = f"**🗃 Total Filters** [ {count} ]\n\n"

        for text in texts:
            keywords = "`{}`\n".format(text)

            filterlist += keywords

        if len(filterlist) > 4096:
            with io.BytesIO(str.encode(filterlist.replace("`", ""))) as keyword_file:
                keyword_file.name = "keywords.txt"
                await message.reply_document(
                    document=keyword_file,
                    quote=True
                )
            return
    else:
        filterlist = f"<b>📂 There Are No Filters</b>"

    await message.reply_text(
        text=filterlist,
        quote=True,
        parse_mode=enums.ParseMode.MARKDOWN
    )
        
@Client.on_message(filters.command('del') & filters.incoming & filters.user(ADMINS))
async def deletefilter(client, message):
    try:
        cmd, text = message.text.split(" ", 1)
    except:
        await message.reply_text(
            "<b><i>❓How To Delete A Filter❓</i></b>\n\n"
            "<b><i>🔆Send /del Filter Name</i></b>",
            quote=True
        )
        return

    query = text.lower()

    await delete_filter(message, query, 'filters')

@Client.on_message(filters.command('delall') & filters.user(ADMINS))
async def delallfill(client, message):
    await message.reply_text(
            f"<b>❓Delete All Filters❓</b>",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text="Accept ✅",callback_data="gconforme")],
                [InlineKeyboardButton(text="Reject ❌",callback_data="close_data")]
            ]),
            quote=True
        )

@Client.on_callback_query(filters.regex("gconforme"))
async def dellacbd(client, message):
    await del_all(message.message, 'filters')
    return await message.reply("👍 Done")
