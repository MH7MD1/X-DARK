## ©t_8_t_t
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
from modules.clientbot.queues import queues, clear          
import asyncio
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from modules.clientbot.clientbot import client
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream
from modules.clientbot import clientbot
from modules.config import GROUP, NETWORK, BOT_USERNAME

 

menu_keyboard = InlineKeyboardMarkup(
    [
        [
            
            InlineKeyboardButton("▷", callback_data="resume_vc"),
            InlineKeyboardButton("II", callback_data="pausevc"),
            ],[
            InlineKeyboardButton("‣‣I", callback_data="skip_vc"),
            InlineKeyboardButton("▢", callback_data="stop_vc"),
            ],[
            InlineKeyboardButton("🗑 حذف", callback_data="set_close"), 
        ], 
     ]
 ) 
    


@Client.on_callback_query(filters.regex("home_start"))
async def start_set(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👋🏻 **مرحبا {query.message.from_user.mention()} انا بوت تشغيل الموسيقي في المكالمات.. 

اعمل بجوده عاليه وبدون تقطيع ..

""", 
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("الاوامر", callback_data="command_list"), 
            ],[
            InlineKeyboardButton("المالك", url="https://t.me/Telugucodersdonations_bot"), 
            ],[
            InlineKeyboardButton("✉️الدعم", url=f"https://t.me/{GROUP}"), 
            InlineKeyboardButton("📡التحديثات", url=f"https://t.me/{NETWORK}"), 
            ],[
            InlineKeyboardButton("✚ اضفني الي مجموعتك ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ]]
            ) 
        ) 
   

@Client.on_callback_query(filters.regex("command_list"))
async def commands_set(_, query: CallbackQuery):
    await query.answer("تم فتح قائمة الاوامر", show_alert=True) 
    await query.edit_message_text(
        f"""💗 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 
➠ هنا تستطيع الاختيار من الكيبور في الاسفل.. 
 
""", 
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("📚الاوامر العامه", callback_data="general_list"), 
            ],[
            InlineKeyboardButton("تخطي", callback_data="skip_list"), 
            InlineKeyboardButton("ايقاف", callback_data="pause_list"), 
            ],[
            InlineKeyboardButton("استئناف", callback_data="resume_list"), 
            InlineKeyboardButton("انهاء", callback_data="stop_list"), 
            ],[
            InlineKeyboardButton("التشغيل", callback_data="play_list"), 
            InlineKeyboardButton("sᴏᴜʀᴄᴇ", callback_data="source"), 
            ],[
            InlineKeyboardButton("◁", callback_data="home_start"), 
            ]]
            ) 
        ) 
    

@Client.on_callback_query(filters.regex("general_list"))
async def general_list(_, query: CallbackQuery):
    await query.answer("تم فتخ الاوامر العامه", show_alert=True)
    await query.edit_message_text(
        f"""🥳 مرحبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ تشغيل (اسم الاغنيه) - \n
➠ اغنيه (اسم الاغنيه) - للتحميل\n
➠ بحث (كلام) -للبحث علي يوتيوب\n
➠ بينج - لاظهار حالة البنج\n
➠ مدة التشغيل - لاظهار مدة تشغيل البوت\n
 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("skip_list"))
async def skip_list(_, query: CallbackQuery): 
    await query.answer("تخطي الاغاني")
    await query.edit_message_text(
        f"""🚩 مرحبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ ** تخطي:- لتخطي المسار الحالي وتشغيل الاغنيه التاليه**
*""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("pause_list"))
async def pause_list(_, query: CallbackQuery):
    await query.answer("ايقف التشغيل")
    await query.edit_message_text(
        f"""💘 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **ايقاف :- لايقاف التشغيل مؤقتا**
""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("resume_list")) 
async def resume_list(_, query: CallbackQuery): 
    await query.answer("استئناف التشغيل")
    await query.edit_message_text(
        f"""❤ مرحبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **استئناف :- لاستئناف تشغيل اغنيه**
""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("stop_list"))
async def stop_list(_, query: CallbackQuery):
    await query.answer("انهاء التشغيل")
    await query.edit_message_text(
        f"""💓 مرحبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **انهاء :- لانهاء تشغيل اغنيه**
""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("play_list"))
async def play_list(_, query: CallbackQuery):
    await query.answer("اوامر التشغيل")
    await query.edit_message_text(
        f"""✨ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **تشغيل :- اسم الاغنيه لبدا لتشغيل**
**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("source"))
async def source(_, query: CallbackQuery): 
    await query.answer("معلومات عن البوت")
    await query.edit_message_text(
        f"""❣️ **مرحبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
➠  **انا بوت استطيع تشغيل الموسيقي في المحادثات الصوتيه في تلجرام بجود فائقه**""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🗑 حذف", callback_data="close_panel")]]
        ),
    )


@Client.on_callback_query(filters.regex("info"))
async def info(_, query: CallbackQuery):
    await query.answer("information")
    await query.edit_message_text(
        f"""✨ مرحبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

💘 نحن تيم اكس دارك \n
""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🗑 حذف", callback_data="close_panel")]]
        ),
    ) 


@Client.on_callback_query(filters.regex("pausevc"))
async def pausevc(_, query: CallbackQuery, message: Message):
    if query.message.sender_chat:
        return await query.answer("انت ادمن مجهول!\n\n» ارجع الي حسابك.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💞 مشرفين المجموعه وحدهم يستطيعون الضغط علي هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if queues.Queue(chat_id):
        try:
            await clientbot.pytgcalls.pause_stream(message.chat.id)
            await query.edit_message_text(
                " تم ايقاف التشغيل", 
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **خطأ:**\n\n`{e}`")
    else:
        await query.answer("🚫 لا شي يشتغللاالان", show_alert=True)


@Client.on_callback_query(filters.regex("set_close"))
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💞 مشرفين المجموعه وحدهم يستطيعون الضغط علي هذا الزر !", show_alert=True)
    await query.message.delete()

@Client.on_callback_query(filters.regex("close_panel"))
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()

@Client.on_callback_query(filters.regex("menu")) 
async def menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.edit_message_text(
        text=f"""مرحبا بك""",
        disable_web_page_preview=True, 
        reply_markup=menu_keyboard
    ) 



