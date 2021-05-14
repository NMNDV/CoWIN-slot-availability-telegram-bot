"""
Developer     : Naman Dave @NMNDV
Recent Update : 14-05-2021 16:30:12
"""

import json
import time
import logging
import requests
import datetime

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# For obtaining TOKEN refer the site below
# https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token

TOKEN = "TOKEN from @BotFather"
NAME = "ASBot"
USR_NAME = "aasetu_bot"

district_ID = 770  # Ahmedabad
# for more details reference the table at the end.

tomorrow_DTO = datetime.date.today() + datetime.timedelta(days=1)
dd = str(tomorrow_DTO.day)
mm = str(tomorrow_DTO.month)
yyyy = str(tomorrow_DTO.year)

dist_g = str(district_ID)
date_g = dd + "-" + mm + "-" + yyyy


def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text(
        "Welcome to the Ahmedabad CoWIN slot-availibility bot. "
        "Developed by NMNDV (git)"
    )
    url = (
        "https://cdn-api.co-vin.in/api/v2/appointment/"
        "sessions/public/"
        "findByDistrict?district_id=" + dist_g + "&date=" + date_g
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/50.0.2661.102 Safari/537.36"
    }

    for i in range(800):
        lr = requests.get(url, headers=headers)
        finite = lr.json()
        if finite["sessions"] != []:
            tr1 = ""
            for center in finite["sessions"]:
                for entry in center:
                    print(entry, center[entry], sep=": ")
                    tr1 += str(entry) + ": " + str(center[center]) + "\n"
                    update.message.reply_text(tr1)
                    time.sleep(2.5)
        else:
            if ((i + 1) % 40) == 0:
                print("No sessions yet")
                update.message.reply_text("No sessions yet")
        time.sleep(2.5)
        # print(lr.status_code, finite)
    update.message.reply_text(
        "ASBot session completed, please type: /start or /help"
        " to start a new session"
    )


updater = Updater(TOKEN)
# updater.message.reply_text("Hello")
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", start))
updater.start_polling()
# Handle '/start' and '/help'
updater.idle()

"""
District IDs:
154 : Ahmedabad
770 : Ahmedabad Corporation
174 : Amreli
179 : Anand
158 : Aravalli
159 : Banaskantha
180 : Bharuch
175 : Bhavnagar
771 : Bhavnagar Corporation
176 : Botad
181 : Chhotaudepur
182 : Dahod
163 : Dang
168 : Devbhumi Dwaraka
153 : Gandhinagar
772 : Gandhinagar Corporation
177 : Gir Somnath
816 : gitsre
815 : gujarathDistrict
169 : Jamnagar
773 : Jamnagar Corporation
178 : Junagadh
774 : Junagadh Corporation
156 : Kheda
170 : Kutch
183 : Mahisagar
160 : Mehsana
171 : Morbi
184 : Narmada
164 : Navsari
185 : Panchmahal
161 : Patan
172 : Porbandar
173 : Rajkot
775 : Rajkot Corporation
162 : Sabarkantha
165 : Surat
776 : Surat Corporation
157 : Surendranagar
166 : Tapi
155 : Vadodara
777 : Vadodara Corporation
167 : Valsad
"""
