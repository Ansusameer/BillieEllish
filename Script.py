class script(object):
    START_TXT = """<i><b>🎃 Helo {}, I'm <a href=https://telegram.me/{}>{}</a></i></b> \n\n<i><b>🔅 I Can Provide You Any Movies, Web-Series, Anime, K-Dramas, Animation, etc!</i></b>"""
    
    
    HELP_TXT = """🔆彡[ @HEROFLiX ]彡🔆"""

    ABOUT_TXT = """🔆彡[ @HEROFLiX ]彡🔆"""

    SOURCE_TXT = """🔆彡[ @HEROFLiX ]彡🔆"""
    MANUELFILTER_TXT = """🔆彡[ @HEROFLiX ]彡🔆"""

    BUTTON_TXT = """🔆彡[ @HEROFLiX ]彡🔆"""

    AUTOFILTER_TXT = """🔆彡[ @HEROFLiX ]彡🔆"""

    CONNECTION_TXT = """🔆彡[ @HEROFLiX ]彡🔆"""
    EXTRAMOD_TXT = """🔆彡[ @HEROFLiX ]彡🔆"""
    ADMIN_TXT = """🔆彡[ @HEROFLiX ]彡🔆"""

    STATUS_TXT = """<b>★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code></b>"""

    LOG_TEXT_G = """#NewGroup
Gʀᴏᴜᴘ = {}(<code>{}</code>)
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""

    ALRT_TXT = """🔆 Honey, It's Not For You❗
🔆 हनी, ये तुम्हारे लिए नहीं है❗"""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛ ᴀɢᴀɪɴ."""

    CUDNT_FND = """<b>❗Enter Correct Name👇</b>
<b>❗सही नाम दर्ज करें👇</b>"""

    I_CUDNT = """<b><i>💢 404 Error / No Results❗

🚫 The Reason❓[<a href="https://telegram.me/HeroFlix/1371">Click Here</a>]
🗨 Please Follow Request Tips
🔆 Request Tips › [<a href="https://telegram.me/HEROFLiX/894">Click Here</a>]</i></b>"""

    I_CUD_NT = """<b><i>💢 404 Error / No Results❗

🚫 The Reason❓[<a href="https://telegram.me/HeroFlix/1371">Click Here</a>]
🗨 Please Follow Request Tips
🔆 Request Tips › [<a href="https://telegram.me/HEROFLiX/894">Click Here</a>]</i></b>"""

    MVE_NT_FND = """<b><i>💢 404 Error / No Results❗

🚫 The Reason❓[<a href="https://telegram.me/HeroFlix/1371">Click Here</a>]
🗨 Please Follow Request Tips
🔆 Request Tips › [<a href="https://telegram.me/HEROFLiX/894">Click Here</a>]</i></b>"""

    TOP_ALRT_MSG = """🔆彡[ @HEROFLiX ]彡🔆"""

    MELCOW_ENG = """<b><i>🔆 "HEROFLiX • GROUP" 亗 🔆
•───────────────────• 
⚜Hey {}, Welcome To HeroFlix • Group. You Can Request Any Movies, Web-Series, Anime, K-Dramas, Animation etc., here....</i></b>"""

    SHORTLINK_INFO = """🔆彡[ @HEROFLiX ]彡🔆"""

    REQINFO = """🔆彡[ @HEROFLiX ]彡🔆"""

    SINFO = """🔆彡[ @HEROFLiX ]彡🔆"""

    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    CAPTION = """
 <a href="https://telegram.me/HEROFLiX"><b><i>{file_name}</i></b></a>"""

    IMDB_TEMPLATE_TXT = """
<b>Query: {query}
IMDb Data:

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
⏱️ Result Shown in: {remaining_seconds} <i>seconds</i> 🔥
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10</b>"""
    
    ALL_FILTERS = """🔆彡[ @HEROFLiX ]彡🔆"""
    
    GFILTER_TXT = """🔆彡[ @HEROFLiX ]彡🔆"""
    
    FILE_STORE_TXT = """🔆彡[ @HEROFLiX ]彡🔆"""
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    LOGO = """𝑺𝒕𝒂𝒓𝒕𝒊𝒏𝒈......."""





            









