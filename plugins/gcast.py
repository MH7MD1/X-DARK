## © copyright infringement on Telugu coders 
## © @telugucoders

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from modules.clientbot.clientbot import client as aditya
from modules.config import SUDO_USERS

@Client.on_message(filters.command(["اذاعه"]))
async def bcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("**بدات الاذاعه 💞...**")
        if not message.reply_to_message:
            await wtf.edit("**رد علي رساله  😒**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"**بدات الاذاعه** \n\n**ارسلت الي:** `{sent}` دردشه \n**خطأ في:** {failed} دردشه")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"تم الاذاعه بنجاح` \n\n**ارسلت الي:** `{sent} دردشه \n**خطا في:** {failed} دردشه")
