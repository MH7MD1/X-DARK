from pyrogram import Client, filters



@Client.on_message(filters.command('ييي'))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**ʏᴏᴜʀ ᴘᴇʀsᴏɴᴀʟ ɪᴅ**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ID**: `{reply.from_user.id}`\n**ʏᴏᴜʀ ᴄʜᴀᴛ ɪᴅ**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**ʏᴏᴜʀ ᴘᴇʀsᴏɴᴀʟ ɪᴅ**: `{message.from_user.id}`\n**ʏᴏᴜʀ ᴄʜᴀᴛ ɪᴅ**: `{message.chat.id}`"
        )
