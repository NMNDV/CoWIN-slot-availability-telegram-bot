"""
Developer     : Naman Dave @NMNDV
Recent Update : 14-05-2021 17:30:12
"""


import time
import requests
import datetime

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# For obtaining TOKEN refer the site below
# https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token

TOKEN = "TOKEN from @BotFather"
NAME = "ASBot"
USR_NAME = "aasetu_bot"
GROUP_NAME = "CoWINbot"

district_ID = 770  # Ahmedabad
# for more details reference the table at the end.

tomorrow_DTO = datetime.date.today() + datetime.timedelta(days=1)
dd = str(tomorrow_DTO.day)
mm = str(tomorrow_DTO.month)
yyyy = str(tomorrow_DTO.year)

# The natural delay for the signal
# The delay to obtain the data and send the user on telegram
# RTT of data server + RTT of telegram server
# This you will have to observe and note.
delay = 0.5  # second

# Telegram bot total session time
total_time = 40 * 60  # seconds

# Refresh time
refresh_time = 1.5 - delay  # seconds

# Time to wait after the slots are found
# Otherwise you will get message after each refresh_time
time_slot_wait = 2.0 - delay  # seconds

# Time to respond the 'No sessions' message
# So that you know the bot is working 😂
no_sess_msg_time = 20  # seconds


if refresh_time < 0:
    refresh_time = 0

total_ticks = int(total_time / refresh_time)
no_sess_tick = int(no_sess_msg_time / refresh_time)

dist_g = str(district_ID)
date_g = dd + "-" + mm + "-" + yyyy


def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text(
        "Welcome to the CoWIN slot-availibility bot. "
        "Developed by NMNDV (git)"
    )
    url = (
        "https://cdn-api.co-vin.in/api/v2/appointment/"
        "sessions/public/"
        "findByDistrict?district_id=" + dist_g + "&date=" + date_g
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/90.0.4430.212 Safari/537.36"
    }

    priority_dict = {
        'pincode': "Pincode",
        'available_capacity': "Available Capacity",
        'min_age_limit': 'Minimum age limit',
        'name': 'Name',
        'address': 'Address'
    }
    take_other_priority = False
    time_stemp = 0
    s_time = time.time()
    while (time.time() - s_time) < total_time:
        lr = requests.get(url, headers=headers)
        try:
            finite = lr.json()
            if finite["sessions"] != []:
                update.message.reply_text("Hey!!! I found some sessions 🤗")
                tr1 = ""
                for center in finite["sessions"]:
                    for pri_val in priority_dict:
                        try:
                            tr1 += str(priority_dict[pri_val]) + ": " + str(center[pri_val]) + "\n"
                        except:
                            pass
                    if take_other_priority:
                        for entry in center:
                            if entry not in priority_dict:
                                print(entry, center[entry], sep=": ")
                                tr1 += str(entry) + ": " + str(center[entry]) + "\n"
                print(tr1, datetime.datetime.now().strftime("%H:%M:%S"))
                update.message.reply_text(tr1)
                time.sleep(time_slot_wait)
            else:
                if ((time_stemp + 1) % no_sess_tick) == 0:
                    print("No sessions yet "
                    "" + datetime.datetime.now().strftime("%H:%M:%S")
                    )
                    update.message.reply_text("No sessions yet 😐")
        except:
            if ((time_stemp + 1) % no_sess_tick) == 0:
                update.message.reply_text(
                    "Server's response failure,"
                    " reasons: high traffic, try changing your bot's"
                    " User-Agent header, maybe the server is crashed 🤔"
                )
                print("Error message ", datetime.datetime.now().strftime(
                    "%H:%M:%S"
                    ))
            time.sleep(refresh_time)
        time.sleep(refresh_time)
        time_stemp += 1
        #print(lr.status_code, finite)
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
