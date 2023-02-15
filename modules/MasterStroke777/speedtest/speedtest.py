# ---------------------------------------------------------------------------------
# This module was loaded in https://t.me/SharkUBmodules_bot
# Licensed under the GNU GPLv3.
# Owner of https://t.me/SharkUBmodules_bot doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------

import asyncio
import time
from pyrogram import Client, filters, types
import speedtest
from time import perf_counter
from sharkub.settings.main_settings import module_list, file_list

from sharkub.settings.prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("speedtest", prefix) & filters.me)
async def avatime(client, message):
  await message.edit("`Starting SpeedTest . . .`")
  spd = speedtest.Speedtest()
  result_dow = int(spd.download())
  await message.edit("`Starting SpeedTest . . . 50%`")
  result_upl = int(spd.upload())
  await message.edit("`Starting SpeedTest . . . 90%`")

  await message.edit(f"""
**<emoji id=5280658777148760247>🌐</emoji> Speedtest Results:**

**Download:** `{round(result_dow/1000000, 2)}`** MiB/s**
**Upload: **`{round(result_upl/1000000, 2)}` **MiB/s**""")


module_list["Speedtest"] = {
"speedtest": "Check your internet connection with speedtest",
}
file_list["Speedtest"] = "speedtest.py"