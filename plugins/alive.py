
###########################################################################################################################################

import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from modules.config import GROUP, NETWORK, BOT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

    
#####################################################################################################################################


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fdbaab61d8b1543030897.jpg",
        caption=f"""**👋🏻 مرحبا {message.from_user.mention()} انا بوت تشغيل الموسيقي في المكالمات الصوتيه

واعمل بسرعه كبيره وجوده عاليه
**
""",
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("الاوامر", callback_data="command_list"), 
            ],[
            InlineKeyboardButton("السورس", url="https://t.me/x_dark1"), 
            ],[
            InlineKeyboardButton("✉️الدعم", url=f"https://t.me/{GROUP}"), 
            InlineKeyboardButton("📡التحديثات", url=f"https://t.me/{NETWORK}"), 
            ],[
            InlineKeyboardButton("✚ اضفني الي مجموعتك ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ]]
            ) 
        ) 
     
    
@Client.on_message(commandpro(["/alive"]) & filters.group & ~filters.edited)
async def alive(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fdbaab61d8b1543030897.jpg",
        caption=f"""ʜᴇʟʟᴏ {message.from_user.mention()} ɪᴀᴍ ᴀʟɪᴠᴇ ɴᴏᴡ 👻""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="info")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["نصب", "تنصيب"]) & filters.group & ~filters.edited)
async def repo(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fdbaab61d8b1543030897.jpg",
        caption=f"""اضغط للتنصيب""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضغط هنا", url="https://t.me/X_DARK1")
                ]
            ]
        ),
    )


@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fdbaab61d8b1543030897.jpg",
        caption=f""" ✨ **ʜᴇʟʟᴏ {message.from_user.mention()} !**\n
💘 **اضغط اسفل للحصول علي الاوامر ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "قائمة الاوامر", callback_data="command_list")
                ]
            ]
        ),
    )




@Client.on_message(command("مدة التشغيل") & filters.group & ~filters.edited)
async def get_uptime(c: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fdbaab61d8b1543030897.jpg", 
        caption=f""" 💞 **ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs ʙᴏᴛ ᴜᴘᴛɪᴍᴇ**:\n
➠ **ᴜᴘᴛɪᴍᴇ:** **{uptime}**\n
➠ **ᴜsᴇʀ:** **{message.from_user.mention()}**\n
➠ **sᴛᴀʀᴛ ᴛɪᴍᴇ:** **{START_TIME_ISO}**\n
""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗑 حذف", callback_data="set_close")
                ]
            ]
        ),
    )
                 

@Client.on_message(command("بينج") & filters.group & ~filters.edited)
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("**بينجج...**")
    delta_ping = time() - start
    await m_reply.edit_text("💝 **ᴘᴏɴɢ!!**\n" f"💖 **{delta_ping * 1000:.3f} ms**")
