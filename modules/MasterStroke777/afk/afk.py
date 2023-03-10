# ---------------------------------------------------------------------------------
# This module was loaded in https://t.me/SharkUBmodules_bot
# Licensed under the GNU GPLv3.
# Owner of https://t.me/SharkUBmodules_bot doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------

import asyncio
import datetime
from pyrogram import Client, filters, types
from sharkub.settings.main_settings import module_list, file_list

from sharkub.settings.prefix import my_prefix
prefix = my_prefix()

afk_info = {
    "start": datetime.datetime.now(),
    "is_afk": False,
    "reason": "",
}

is_afk = filters.create(lambda _, __, ___: afk_info["is_afk"])


@Client.on_message(is_afk & ~filters.me & ((filters.private & ~filters.bot) | (filters.mentioned & filters.group)))
async def afk_handler(_, message: types.Message):
    end = datetime.datetime.now().replace(microsecond=0)
    afk_time = end - afk_info["start"]
    await message.reply_text(
        f"ā This user <b>AFK</b>.\nš¬ Reason:</b> <i>{afk_info['reason']}</i>\n<b>ā³ Duration:</b> {afk_time}"
    )


@Client.on_message(filters.command("afk", prefix) & filters.me)
async def afk(_, message):
    if len(message.text.split()) >= 2:
        reason = message.text.split(" ", maxsplit=1)[1]
    else:
        reason = "None"

    afk_info["start"] = datetime.datetime.now().replace(microsecond=0)
    afk_info["is_afk"] = True
    afk_info["reason"] = reason

    await message.edit(f"ā I'm going <b>AFK</b>.\n<b>š¬ Reason:</b> <i>{reason}</i>.")


@Client.on_message(filters.command("unafk", prefix) & filters.me)
async def unafk(_, message):
    if afk_info["is_afk"]:
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = end - afk_info["start"]
        await message.edit(f"<b>ā I'm not <b>AFK</b> anymore.\n" f"ā³ I was <b>AFK:</b> {afk_time}")
        afk_info["is_afk"] = False
    else:
        await message.edit("<b>ā You weren't afk</b>")


module_list["AFK"] = {
    "afk": "Start AFK status",
    "unafk": "Remove the AFK status",
}
file_list["AFK"] = "afk.py"