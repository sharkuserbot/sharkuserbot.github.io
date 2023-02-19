from pyrogram import Client, filters, enums
from datetime import datetime
from sharkub.settings.main_settings import module_list, file_list

from sharkub.settings.prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("stats", prefixes=prefix) & filters.me)
async def stats(client, message):
    await message.edit("<b>Collecting stats...</b>")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    Meh = await client.get_me()
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            u += 1
        elif dialog.chat.type == enums.ChatType.BOT:
            b += 1
        elif dialog.chat.type == enums.ChatType.GROUP:
            g += 1
        elif dialog.chat.type == enums.ChatType.SUPERGROUP:
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
            if user_s.status in (
                enums.ChatMemberStatus.OWNER,
                enums.ChatMemberStatus.ADMINISTRATOR,
            ):
                a_chat += 1
        elif dialog.chat.type == enums.ChatType.CHANNEL:
            c += 1

    end = datetime.now()
    ms = (end - start).seconds
    await message.edit(
        """<b><emoji id=5334882760735598374>📝</emoji> Your Stats collected in <code>{}</code> seconds</b>

<b>You have <code>{}</code> Private Messages.</b>
<b>You are in <code>{}</code> Groups.</b>
<b>You are in <code>{}</code> Super Groups.</b>
<b>You Are in <code>{}</code> Channels.</b>
<b>You Are Admin in <code>{}</code> Chats.</b>
<b>Bots: </b> <code>{}</code>""".format(
            ms, u, g, sg, c, a_chat, b
        )
    )


module_list["Stats"] = {
    "stats": "Get your account stats",
}
file_list["Stats"] = "stats.py"